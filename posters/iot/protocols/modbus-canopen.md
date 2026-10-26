---
title: "Industrial Fieldbus Protocols: Modbus and CANopen"
subtitle: Polled registers over RS-485 and Ethernet, against event-driven object dictionaries on CAN
byline: IoT protocols
orientation: landscape
columns: 3
paper: a1
width: 1750
document_number: PO-021
colours:
  accent: "#d97706"
  secondary: "#b45309"
footer:
  left: Modbus and CANopen
  centre: IoT Protocols Reference
  qr: https://modbus.org/specs.php
  qr-label: Modbus specifications
---

## Key figures {.stats style=tiles}

| Value | Label |
|---|---|
| 4 tables | In the Modbus data model: coils, inputs, input and holding registers |
| 247 | Device addresses on a Modbus serial line; 0 is broadcast |
| 8 bytes | In a classic CANopen PDO, with no protocol header |
| 29 bits | In a J1939 identifier: priority, PGN and source |

## Introduction {.abstract}

Factories, solar farms and heavy vehicles run on two families of protocol over twisted pair. **Modbus**, as RTU over **RS-485** or over **TCP**, polls four flat tables of bits and 16-bit registers. **CAN** protocols, **CANopen** and **SAE J1939**, organise data in a dictionary, and let any node broadcast an event without waiting to be asked.

## 1. The Modbus data model

Beware the off-by-one: register **40001** in a manual is wire address **0x0000**, read with function code 0x03.

| Table | Width | Access | Manual prefix | Function codes |
|---|---|---|---|---|
| Coils | 1 bit | Read and write | 0xxxx | 0x01 read; 0x05, 0x0F write |
| Discrete inputs | 1 bit | Read only | 1xxxx | 0x02 |
| Input registers | 16 bits | Read only | 3xxxx | 0x04 |
| Holding registers | 16 bits | Read and write | 4xxxx | 0x03 read; 0x06, 0x10 write |

Over TCP (port 502), the CRC is dropped and a 7-byte **MBAP** header goes in front: transaction ID, protocol 0, length and unit ID. The PDU inside is the same.

## 2. A request on the wire

Read two holding registers from address 0x006B, on device 1:

```hex-dissect cols=8 title="Request" ascii=no
bytes: 01 03 00 6b 00 02 b5 d7
0 | Device | 1 | navy
1 | Function | 0x03: read holding registers | amber
2-3 | Start address | 0x006B = 107: register 40108 | blue
4-5 | Count | 2 registers | blue
6-7 | CRC-16/MODBUS | 0xD7B5, low byte first | teal
```

## 3. The reply

```hex-dissect cols=8 title="Response" ascii=no
bytes: 01 03 04 02 2b 00 64 8a 68
0 | Device | 1 | navy
1 | Function | 0x03 | amber
2 | Byte count | 4 | grey
3-4 | Register 107 | 0x022B = 555: 55.5 °C | green
5-6 | Register 108 | 0x0064 = 100 rpm | green
7-8 | CRC | 0x688A, low byte first | teal
```

On an error the device sets the top bit of the function code (0x83) and returns an exception code.

> [!WARNING]
> Modbus defines 16-bit registers, not 32-bit floats. Vendors split them across two registers in four orders: ABCD, CDAB, BADC, DCBA. **Document yours.**

## 4. Polling, or events {.wide}

RS-485 has no arbitration, so a Modbus device speaks only when the PLC polls it. CAN arbitrates bit by bit, so any CANopen or J1939 node can send an urgent message at once:

```lanes
Modbus | *Poll drive 1 | *Reply | *Poll sensor 2 | *Reply | An alarm waits for its turn
CANopen | *Sync | *PDOs from every node | *EMCY the moment a fault occurs | *Heartbeats
```

```compare
| Modbus RTU | Modbus TCP | CANopen (CiA 301) | SAE J1939
Physical | RS-485, 9.6 to 115.2 kbps | Ethernet, port 502 | CAN, 125 kbps to 1 Mbps | CAN, 250 or 500 kbps
Model | Master and slaves, polled | Client and server | **PDOs** peer to peer, **SDOs** client and server | Cyclic and event broadcasts of **PGNs**
Alarm latency | Slow: waits to be polled | Fast if polled often | **Under a millisecond**: high-priority EMCY | **Milliseconds**: priority 0 to 7 in the ID
Data | Flat register numbers | Flat register numbers | Standard **index and subindex** | Standard **PGNs** and SPNs
```

## 5. The CANopen object dictionary

Every parameter has a 16-bit index and 8-bit subindex. The ranges are 0x1000 to 0x1FFF for communication, 0x2000 to 0x5FFF for the vendor, 0x6000 and up for device profiles such as CiA 402 drives.

The 11-bit **COB-ID** is a 4-bit function code and a 7-bit node ID. TPDO1 from node 1 is 0x181:

```tape
cells: 0 0 1 1 0 0 0 0 0 0 1
1-4 | Function 3: TPDO1 | green
5-11 | Node 1 | navy
```

## 6. CANopen objects

```cards cols=1 style=top
NMT, ID 0x000 | Network management: moves nodes between pre-operational, operational and stopped | navy
EMCY, 0x080 + node | Emergency: a high-priority fault frame, sent at once | red
PDOs, 0x180 to 0x57F | Process data: up to 64 bits of mapped variables, with no overhead | green
SDO, 0x580 and 0x600 + node | Service data: confirmed reads and writes of any entry, for set-up and updates | amber
```

## 7. Checklist {style=card colour=amber}

```checklist
[x] Give Modbus addresses both ways: wire offset 0x006B and PLC register 40108
[x] State the word order of every 32-bit value
[x] Return exception codes (0x01 function, 0x02 address, 0x03 value), never silence
[x] Ship an EDS file with every CANopen product
[x] Isolate RS-485 and CAN transceivers: a 2.5 kV isolator and an isolated supply
```

## 8. Glossary

```glossary cols=1
COB-ID | Communication object identifier: the CAN ID
EDS | Electronic data sheet of a CANopen device
MBAP | Modbus application protocol header, for TCP
PDO, SDO | Process and service data objects
PGN, SPN | J1939 parameter group and suspect parameter numbers
PLC | Programmable logic controller
RTU | Modbus's binary serial framing
```

## In short {.summary}

Use Modbus for PLCs and meters that expect polled registers. Use CANopen or J1939 when drives and sensors must coordinate within milliseconds.

### Mind the off-by-one

List both the hex wire address and the five-digit PLC register.

### Configure once, stream fast

Set a drive up with SDOs at start-up, then stream setpoints and feedback in PDOs.

### Isolate the field wiring

Factory ground loops destroy unprotected microcontrollers.
