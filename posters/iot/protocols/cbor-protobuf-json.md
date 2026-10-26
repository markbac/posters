---
title: "Binary Serialisation and Compact Data Formats"
subtitle: Packing telemetry and commands into few bytes, without losing schema evolution
byline: IoT protocols
orientation: portrait
columns: 2
paper: a1
width: 1200
document_number: PO-022
colours:
  accent: "#4f46e5"
  secondary: "#4338ca"
footer:
  left: CBOR, Protobuf and JSON
  centre: IoT Protocols Reference
  qr: https://cbor.io/
  qr-label: cbor.io
---

## Key figures {.stats style=tiles}

| Value | Label |
|---|---|
| 31 bytes | The example reading as JSON |
| 10 bytes | The same in CBOR, with integer keys |
| 9 bytes | The same in Protocol Buffers |
| 0 | Breakage when a new field is added to CBOR or Protobuf |

## Introduction {.abstract}

Why not cast a C `struct` to bytes and send it? Because padding, byte order and new firmware versions all change its layout. **JSON** avoids that, but spends battery formatting numbers as text and repeating key names. **CBOR** and **Protocol Buffers** are compact, independent of byte order, and let a schema grow safely.

## 1. JSON: 31 bytes {cols=3}

The reading `{"id": 42, "temp": 21.5, "ok": true}`, byte by byte, three ways.

```hex-dissect cols=8 title="JSON: 31 bytes of text"
bytes: 7b 22 69 64 22 3a 34 32 2c 22 74 65 6d 70 22 3a 32 31 2e 35 2c 22 6f 6b 22 3a 74 72 75 65 7d
0-5 | Key "id" | With quotes and colon | grey
6-7 | 42 | Two ASCII digits | blue
8-15 | Key "temp" | | grey
16-19 | 21.5 | Four ASCII characters | purple
20-25 | Key "ok" | | grey
26-30 | true, and the closing brace | | green
```

## 2. CBOR: 10 bytes

```hex-dissect cols=8 title="CBOR, integer keys" ascii=no
bytes: a3 01 18 2a 02 f9 4d 60 03 f5
0 | Map of 3 | 0xA3: major type 5, count 3 | navy
1-3 | 1: 42 | Key 1; 0x18 means one byte follows | blue
4-7 | 2: 21.5 | Key 2; 0xF9: a half-precision float, 0x4D60 | purple
8-9 | 3: true | Key 3; 0xF5 is true | green
```

## 3. Protocol Buffers: 9 bytes

```hex-dissect cols=8 title="Protocol Buffers" ascii=no
bytes: 08 2a 15 00 00 ac 41 18 01
0-1 | Field 1: 42 | Tag 0x08: field 1, varint | blue
2-6 | Field 2: 21.5 | Tag 0x15: field 2, 32-bit; float 0x41AC0000, little-endian | purple
7-8 | Field 3: true | Tag 0x18: field 3, varint | green
```

## 4. How CBOR works (RFC 8949)

Each item starts with one byte: a 3-bit **major type** and a 5-bit **additional information** field.

| Major type | Meaning | Example |
|---|---|---|
| 0 | Unsigned integer | 0x0A = 10: values 0 to 23 fit in the first byte |
| 1 | Negative integer | 0x20 = −1 |
| 2 | Byte string | Raw keys, hashes, signatures: no Base64 |
| 3 | UTF-8 text | Length first: no scanning for a null |
| 4 | Array | 0x83: three items |
| 5 | Map | 0xA3: three pairs |
| 6 | Tag | Gives meaning to the next item, such as a date |
| 7 | Simple values, floats | 0xF4 false, 0xF5 true, 0xF9 half float |

> [!TIP]
> Use **integer keys**, or a CDDL schema with zcbor, instead of repeating `"temperature"`. CBOR then comes within a byte or two of Protobuf, and stays self-describing.

## 5. How Protocol Buffers work

There are no names and no brackets on the wire. Both ends compile one `.proto` file (nanopb generates static C structs, with no malloc). Each field is a tag, `(field number << 3) | wire type`, then its value.

```protobuf
syntax = "proto3";
message Telemetry {
  uint32 uptime_s  = 1;   // varint: 1 to 5 bytes
  sint32 temp_mc   = 2;   // ZigZag: small negatives stay small
  bytes  signature = 3;   // bounded in .options: max_size 64
}
```

> [!WARNING]
> Use `sint32` for values that can be negative. A plain `int32` sends −1 as **10 bytes**; `sint32` sends it as one.

## 6. Four ways compared {.wide}

```compare
| Packed C struct | JSON (cJSON, jsmn) | CBOR (zcbor, QCBOR) | Protobuf (nanopb)
Schema | A shared header file | None: self-describing | Optional: CDDL | **A .proto file, required**
Size | Smallest, fixed width | **Largest**: text and quotes | **Compact**, above all with integer keys | **Smallest** with structure
Binary data | Fixed arrays only | Base64: a third bigger | **Native byte strings** | **Native bytes**
Adding a field | **Breaks** | Easy: unknown keys ignored | **Easy** | **Easy**: never reuse a field number
Where used | Inside one product | Web APIs and the cloud | **CoAP, LwM2M, Matter, COSE, FIDO2** | **gRPC**, Google Cloud, mobile apps
```

## 7. Checklist {style=card colour=purple}

```checklist
[x] Never send raw struct memory between compilers, architectures or firmware versions
[x] Protobuf: `sint32` and `sint64` for anything that can be negative
[x] Protobuf: bound strings and bytes in `.options`, so nanopb needs no malloc
[x] CBOR: integer keys or arrays on narrowband links such as NB-IoT and LoRaWAN
[x] Put a message type or schema ID in the envelope, and ignore unknown fields
```

## 8. Glossary

```glossary cols=1
CBOR | Concise Binary Object Representation, RFC 8949
CDDL | Concise Data Definition Language, RFC 8610
COSE | CBOR Object Signing and Encryption, RFC 9052
SenML | Sensor Measurement Lists, RFC 8428
Varint | 7 bits a byte, with a continuation bit
ZigZag | Maps −1, 1, −2 to 1, 2, 3, so small negatives stay short
```

## In short {.summary}

Replace JSON and raw structs with CBOR, for CoAP, LwM2M and self-describing payloads, or Protobuf, when both ends share a schema.

### Never send raw structs

One compiler update or new field moves every offset, and breaks every device in the field.

### Binary belongs in binary

A 64-byte signature in JSON needs Base64. CBOR and Protobuf send the bytes.

### sint32 for negatives

ZigZag makes −1 one byte; plain int32 makes it ten.
