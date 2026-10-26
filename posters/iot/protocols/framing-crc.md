---
title: "Binary Framing and Checksums"
subtitle: Turn a raw byte stream into self-synchronising, error-checked packets
byline: Embedded protocol engineering and data integrity
orientation: portrait
paper: a1
width: 1200
document_number: PO-006
colours:
  accent: "#0284c7"
footer:
  left: Framing and CRC
  centre: IoT Protocols Reference
  qr: https://en.wikipedia.org/wiki/Consistent_Overhead_Byte_Stuffing
  qr-label: COBS on Wikipedia
---

## Key figures {.stats style=tiles}

| Value | Label |
|---|---|
| 1 byte | Most COBS adds to 254 bytes of payload |
| 0x00 | The one byte COBS never sends inside a frame |
| 100 % | Bursts of up to 16 bits that CRC-16 catches |
| 7 | Parameters that define any CRC (Rocksoft model) |

## Introduction {.abstract}

A UART or TCP stream delivers bytes with no packet boundaries, and noise flips bits on the way. Lose one byte, or mistake a payload byte for a start marker, and every packet after it breaks. Reliable protocols solve this in two layers: **framing** marks where each packet starts and ends, and a **Cyclic Redundancy Check (CRC)** proves that every bit arrived intact.

## 1. The problem: why a sync byte and a length are not enough {.wide}

Send `[0xAA][Length][Payload]` with no byte stuffing, and three things go wrong as soon as noise hits the wire or a receiver joins mid-stream:

```cards cols=3 style=top
False sync | A payload byte of 0xAA looks like a start marker to a receiver that joined mid-packet | red
Length hang | A flipped length byte (4 becomes 250) makes the receiver wait for 246 bytes that never come | amber
Silent corruption | A simple sum misses swapped bytes, and a +1 in one byte cancels a -1 in the next | navy
```

```flow
[Payload|navy] -append-> [Payload and CRC|blue] -stuff-> [COBS frame|green] -end with-> [0x00|amber] -split, unstuff-> [Frame] -check CRC-> [Accept or drop|green]
Compute the CRC over the payload before stuffing, and check it after unstuffing.
```

## 2. Three framing schemes {cols=2}

```figure
@segments
title: Sync, length and CRC: recovery needs a silence timeout
2 | Sync 0xAA55 | 2 B | navy
1 | Len | 1 B | blue
5 | Payload (may contain 0xAA55) | N bytes | amber
2 | CRC-16 | 2 B | teal
+++
@segments
title: SLIP: escapes 0xC0 as 0xDB 0xDC
1 | 0xC0 | start | navy
7 | Payload and CRC, up to twice the size | N to 2N | blue
1 | 0xC0 | end | navy
+++
@segments
title: COBS: each zero replaced by the distance to the next
1 | Code | offset | green
7 | Payload and CRC with no zero bytes | N + 1 B | navy
1 | 0x00 | end | amber
```

| Property | Sync and length | SLIP | COBS |
|---|---|---|---|
| Delimiter | Header and count | `0xC0` | `0x00` |
| Overhead on 100 B | 4 to 6 B, fixed | 2 B to 102 B | 2 B, always |
| Recovers at | A silence timeout | The next `0xC0` | The next `0x00` |

## 3. COBS: how the zeros disappear

COBS replaces every `0x00` with a code byte: the distance to the next zero. The encoded frame has no zeros left, so `0x00` can only mean "end of frame".

```hex-dissect title="11 22 00 33 00, encoded with COBS" ascii=no
bytes: 03 11 22 02 33 01 00
0 | Code 3 | Two data bytes, then a zero | green
1-2 | Data | 11 22 | navy
3 | Code 2 | One data byte, then a zero | green
4 | Data | 33 | navy
5 | Code 1 | No data, then a zero | green
6 | Delimiter | End of frame | amber
```

```structogram
while Bytes arrive
  if Byte is 0x00?
    Decode the frame
    if CRC matches?
      Pass the frame on
    else
      Drop it and count the error
    Clear the buffer
  else
    Append the byte to the buffer
```

> [!TIP]
> COBS adds at most one byte in 254, so DMA buffers can be sized at compile time.

## 4. Error detection: why polynomial division wins

A CRC treats the message as a polynomial over GF(2), and divides it by a generator polynomial with carry-less XOR arithmetic. The remainder is the check value:

```equation
title: The CRC
\mathrm{CRC} = \left( M(x) \cdot x^{n} \right) \bmod G(x)
M(x) | The message, as a polynomial with one bit a coefficient |
G(x) | The generator polynomial, of degree n | 0x1021 for CRC-16/CCITT
n | The width of the CRC | bits
```

```compare
| 8-bit sum | Fletcher-16 | CRC-16
Single-bit errors | All | All | **All**
Two-bit errors | Misses cancelling pairs | Misses some | **All**, in frames up to 4 KB
Swapped bytes | Misses all | Catches | **Catches**
Bursts of 16 bits or fewer | About 99.6 % | About 99.998 % | **All**
```

```logscale title="Chance that random corruption goes unnoticed"
3.9e-3 | 8-bit sum
1.5e-5 | CRC-16
2.3e-10 | CRC-32
```

## 5. The Rocksoft model: seven parameters {style=card colour=blue}

Two "CRC-16" functions give different results unless all seven parameters match:

| Parameter | Meaning | CRC-16/CCITT-FALSE | CRC-16/MODBUS | CRC-32 |
|---|---|---|---|---|
| width | Bits | 16 | 16 | 32 |
| poly | Generator | `0x1021` | `0x8005` | `0x04C11DB7` |
| init | Start value | `0xFFFF` | `0xFFFF` | `0xFFFFFFFF` |
| refin, refout | Reflect bits | no, no | yes, yes | yes, yes |
| xorout | Final XOR | `0x0000` | `0x0000` | `0xFFFFFFFF` |
| check | CRC of "123456789" | `0x29B1` | `0x4B37` | `0xCBF43926` |

> [!IMPORTANT]
> Test every CRC function, in C and in Python, against the nine ASCII bytes "123456789" and its check value.

## 6. Designing a protocol: the workflow {.wide}

```steps cols=3
Version and opcode | Start each payload with a one-byte version and a one-byte command
Fix the byte order | Little-endian fields, named for their size: uint16_le, float32_le | blue
Append the CRC | Over the header and payload, before stuffing
Encode with COBS | Remove every 0x00 and end the frame with one | navy
Pin the check value | Assert the CRC of "123456789" in C and Python unit tests | green
Fuzz the decoder | Feed it random, truncated and bit-flipped frames in CI | amber
```

## 7. Glossary {.wide}

```glossary cols=4
ASCII | American Standard Code for Information Interchange
CBOR | Concise Binary Object Representation, a binary payload format
COBS | Consistent Overhead Byte Stuffing
CRC | Cyclic Redundancy Check
DMA | Direct Memory Access: copies bytes to RAM without the CPU
GF(2) | The field of two elements, 0 and 1, where addition is XOR
SLIP | Serial Line Internet Protocol, framing with 0xC0
UART | Universal Asynchronous Receiver-Transmitter
```

## In short {.summary}

Never send a raw struct down a serial line: append a CRC, stuff the frame with COBS, and end it with 0x00.

### Resynchronise in one byte

A COBS frame has no zero inside it, so after any glitch the receiver is back in step at the next 0x00.

### Size buffers at compile time

SLIP can double a frame. COBS adds at most one byte in 254.

### Pin the CRC

Fix all seven Rocksoft parameters and test them against "123456789", so firmware and host tools agree.

## References {.references}

1. S. Cheshire and M. Baker, *Consistent Overhead Byte Stuffing*, IEEE/ACM Transactions on Networking, 1999.
2. R. N. Williams, *A Painless Guide to CRC Error Detection Algorithms*, 1993.
3. P. Koopman, *Best CRC Polynomials*, Carnegie Mellon University.
