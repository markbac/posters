---
title: "Embedded Serial Buses"
subtitle: Choosing the right interface on the board and out in the field
byline: Embedded hardware engineering
orientation: landscape
columns: 3
paper: a1
width: 1750
document_number: PO-005
footer:
  left: Serial Buses
  centre: Embedded Engineering Reference
  qr: https://en.wikipedia.org/wiki/Serial_communication
  qr-label: Serial communication
---

## Key figures {.stats style=tiles}

| Value | Label |
|---|---|
| 2 wires | For UART and for I2C |
| 50 Mbps and more | SPI, the fastest bus on a board |
| 112 | Usable addresses on a 7-bit I2C bus |
| 1,200 m | Reach of RS-485 over twisted pair |

## Introduction {.abstract}

Microcontrollers talk to sensors, displays, memory and distant actuators over serial buses that trade pins for speed and reach. **UART** joins two devices with no clock wire. **I2C** shares two wires among dozens of chips on a board. **SPI** uses four wires for speed. **RS-485** and **CAN** send a voltage difference down a twisted pair, which survives factory noise over hundreds of metres.

## 1. Three buses on the board {.wide}

```cards cols=3 style=top
UART | Point to point, full duplex, on TX and RX. No clock: both ends agree the baud rate in advance | amber
I2C | Half duplex on SDA and SCL, with pull-up resistors. Each chip has a 7- or 10-bit address | blue
SPI | Full duplex and fast, on SCLK, MOSI, MISO, and one chip select for each chip | navy
```


## 2. A UART byte

With no clock, each byte carries its own start and stop bits: 10 bits for 8 of data.

```instrument type=logic title="0x55 at 8N1: idle, start, 8 bits LSB first, stop"
TX | 11010101010111
```

## 3. An I2C read

A temperature sensor at 0x48: write the register number, then read two bytes.

```hex-dissect title="Logic analyser, decoded" ascii=no
bytes: 90 00 91 15 80
0 | Address 0x48, write | 0x48 << 1 | navy
1 | Register | 0x00: temperature | blue
2 | Address 0x48, read | Repeated start | navy
3-4 | Temperature | 21.5 °C | green
```

A 7-bit address shifted left becomes 0x90 to write and 0x91 to read: the commonest bring-up mistake.

## 4. SPI modes

| Mode | CPOL | CPHA | Clock idles | Data sampled on |
|---|---|---|---|---|
| 0 | 0 | 0 | Low | Rising edge: the commonest |
| 1 | 0 | 1 | Low | Falling edge |
| 2 | 1 | 0 | High | Falling edge |
| 3 | 1 | 1 | High | Rising edge |

## 5. Off the board: differential pairs

Single-ended 3.3 V traces pick up interference beyond half a metre. **RS-485** and **CAN** send the difference between two twisted wires, so noise that hits both cancels.

```cards cols=1 style=top
RS-485 | 32 to 256 transceivers over 1,200 m; usually carries Modbus RTU | blue
CAN | Any node may send; bitwise arbitration lets the highest priority win without damage; hardware CRC and fault confinement | green
```

```hex-dissect title="A J1939 identifier, 0x18FF50E5" ascii=no
bytes: 18 FF 50 E5
0 | Priority 6 | 0x18 | red
1-2 | PGN | 0xFF50: proprietary | blue
3 | Source address | 0xE5 | green
```

> [!WARNING]
> Fit a **120 Ω** terminator at each end of an RS-485 or CAN trunk, and nowhere else. Without them, reflections corrupt bits at speed.

## 6. Speeds

```logscale unit=" bps"
1.152e5 | UART at 115,200 | amber
4e5 | I2C fast mode | blue
1e6 | CAN | green
1e7 | RS-485, fast | teal
5e7 | SPI to flash | navy
```

## 7. Five buses compared {.wide}

```compare
| UART | I2C | SPI | RS-485 | CAN
Wires | 2: TX, RX | 2: SDA, SCL | 4 or more | 2 or 4, twisted | 2: CAN_H, CAN_L
Duplex | Full | Half | Full | Half (2-wire) | Half, arbitrated
Devices | 2 | **112** addresses | One per chip select | 32 to 256 | 64 to 120 and more
Speed | 9.6 kbps to 3 Mbps | 100 kbps, 400 kbps, 1 Mbps | 1 to 80 Mbps | 9.6 kbps to 10 Mbps | 125 kbps to 1 Mbps; CAN FD to 5 Mbps and more
Reach | Under 1 m | Under 0.5 m | Under 0.3 m | **1,200 m** | 500 m at 125 kbps
Framing | Bytes only | Address and ACK | None: raw bits | None: carries UART bytes | **ID, CRC and ACK**
```

## 8. Which bus

```structogram
if Does the cable leave the board?
  if Many nodes polled by one master?
    RS-485 with Modbus
  else
    CAN
else
  if Over 1 Mbps?
    SPI
  else
    if Many slow sensors?
      I2C
    else
      UART
```

## 9. Bring-up checklist {style=card colour=navy}

```checklist
[x] UART TX and RX crossed, and baud rates within 2 %
[x] I2C pull-ups on SDA and SCL: 2.2 to 4.7 kΩ at 3.3 V and 400 kHz
[x] I2C 7-bit address not confused with the shifted 8-bit one
[x] SPI CPOL and CPHA match the datasheet's timing diagram
[x] A common ground between boards and the logic analyser
[ ] 120 Ω terminators at the two ends of RS-485 and CAN only
```

## 10. Glossary

```glossary cols=1
ACK, NACK | Acknowledge and not acknowledge, on the ninth I2C clock
CAN FD | CAN with flexible data rate: up to 64-byte payloads
CPOL, CPHA | SPI clock polarity and phase
DLC | Data length code of a CAN frame
MOSI, MISO | SPI controller out and controller in
PGN | Parameter group number, in J1939
RTU | Modbus's binary framing
TTL | Logic levels: single-ended 3.3 or 5 V
```

## In short {.summary}

I2C for slow sensors on the board, SPI for fast chips on the board, UART for one module, and RS-485 or CAN whenever the wire leaves the board.

### Two wires on a board

I2C runs a dozen sensors on two pins, if the pull-ups suit the bus capacitance.

### Four wires for speed

SPI streams megabytes a second to flash and displays, with no addressing.

### Twisted pair for distance

RS-485 and CAN ignore factory noise over hundreds of metres by measuring a difference.
