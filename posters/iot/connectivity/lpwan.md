---
title: "Low-Power Wide-Area Networks"
subtitle: Cellular and unlicensed long-range radio for battery devices compared
byline: IoT connectivity
orientation: portrait
columns: 3
paper: a1
width: 1350
document_number: PO-009
footer:
  left: LPWAN
  centre: IoT Engineering Reference
  qr: https://lora-alliance.org/
  qr-label: LoRa Alliance
---

## Key figures {.stats style=tiles}

| Value | Label |
|---|---|
| 10 km and more | Rural range of LoRaWAN |
| 164 dB | Link budget of NB-IoT: the deepest indoor reach |
| 1 Mbps | Peak rate of LTE-M, with handover and voice |
| 1 % | Duty-cycle limit in Europe's 868 MHz band |

## Introduction {.abstract}

**Low-power wide-area (LPWA)** radios fill the gap between short-range wireless and cellular broadband. **LoRaWAN** uses chirp spread spectrum in unlicensed bands, so anyone can put up a gateway, with no SIM fees. **NB-IoT** and **LTE-M** use licensed 3GPP cellular spectrum and the operators' towers, with managed quality of service.

## 1. Three radios

```cards cols=1 style=top
LoRaWAN, unlicensed | Chirp spread spectrum at 868 MHz (Europe) or 915 MHz (Americas). A node broadcasts; any gateway in range forwards to the network server | green
NB-IoT, licensed 180 kHz | A narrow carrier inside LTE: the deepest indoor reach and longest sleep, for sensors that stay put | navy
LTE-M, licensed 1.4 MHz | Wider: full handover, lower latency, room for firmware updates, and VoLTE | blue
```

## 2. Link budget

Maximum coupling loss: how much loss between node and tower the link survives. Each 6 dB doubles the range in free space.

```gradient-scale from=140 to=166 unit=" dB" colours=red,amber,green step=4
142 | LTE, and LoRa SF7
156 | LTE-M
157 | LoRa SF12
164 | NB-IoT
```

NB-IoT gets there by repetition: a downlink can be sent up to 2,048 times.

## 3. LoRa spreading factors

The **spreading factor** trades rate for sensitivity; **adaptive data rate (ADR)** picks it per node.

| Spreading factor | Bit rate at 125 kHz | Air time, 50 B | Largest payload (EU868) |
|---|---|---|---|
| SF7, near a gateway | 5,470 bps | About 100 ms | 222 B |
| SF9 | 1,760 bps | About 330 ms | 115 B |
| SF12, at the edge | 250 bps | About 2.3 s | 51 B |

> [!WARNING]
> At 868 MHz a node may transmit **1 %** of the time: 36 s an hour. At SF12 that is about 15 messages.

## 4. Trade-offs, side by side {.wide}

```plot type=parallel width=1100 height=260 title="Typical values"
| Range km | Battery years | Bit rate kbps | Peak current mA
LoRaWAN | 12 | 9 | 5 | 40
NB-IoT | 15 | 10 | 60 | 220
LTE-M | 11 | 7 | 1000 | 350
```

```compare
| LoRaWAN (Class A, B, C) | NB-IoT (Cat-NB2) | LTE-M (Cat-M1)
Spectrum | Unlicensed 868 or 915 MHz: free | Licensed, 700 to 2100 MHz: SIM | Licensed, 700 to 2100 MHz: SIM
Who runs it | You, a community, or an operator | Mobile operators | Mobile operators
Bandwidth | 125 to 500 kHz | 180 kHz | 1.4 MHz
Data rate | 0.3 to 27 kbps | 26 to 159 kbps | 300 kbps to 1 Mbps
Packet size | 11 to 222 B | 20 to 1,500 B | IP streams, large updates
Duty cycle | **1 % in EU868** | Scheduled by the network | Scheduled by the network
Moving | Works: every gateway hears it | Stationary: reselection only | **Full handover**, at motorway speed
Peak transmit current | **35 to 110 mA** | 70 to 220 mA | 150 to 350 mA
```

## 5. How a sleeping node is reached {.wide}

```lanes
LoRaWAN Class A | *Send | *Rx1, 1 s | *Rx2, 2 s | Asleep until the next send
LoRaWAN Class B | *Beacon | *Ping slot | *Ping slot | Downlink at set times
LoRaWAN Class C | *Listening | *Send | *Listening | Mains powered: no delay
Cellular PSM | *Send | *Idle, T3324 | Asleep in PSM | *Wake at T3412
```

## 6. Joining

```terminal title="LoRaWAN, OTAA (AT commands vary by module)"
> AT+JOIN=1:0:10:8
+EVT:JOINED
> AT+SEND=2:A41580
+EVT:TX_DONE SF7 14dBm
-- Over-the-air activation: fresh session keys on every join
```

```terminal title="NB-IoT, attaching"
> AT+COPS?
+COPS: 0,2,"23415",9
> AT+CEREG?
+CEREG: 0,1
-- Operator 234-15, access technology 9: NB-IoT; registered on the home network
```

## 7. Which one

```structogram
if Private site, no SIM fees, under 100 B an hour?
  LoRaWAN
else
  if Moving, voice, or large updates?
    LTE-M
  else
    NB-IoT: deep indoor, stationary
```

## 8. Deployment checklist {style=card colour=green}

```checklist
[x] OTAA with unique root keys; never ABP with hard-coded keys
[x] ADR on for stationary LoRaWAN nodes, so near ones drop to SF7
[x] The battery suits the peak: coin cells need a capacitor for 220 mA cellular bursts
[x] Binary payloads (CBOR or packed bits) that fit SF12's 51 bytes
[x] Firmware updates tested: LoRaWAN multicast fragments, or CoAP blocks on cellular
```

## 9. Glossary {.wide}

```glossary cols=4
ADR | Adaptive data rate
CE level | Coverage enhancement: how many repetitions
CSS | Chirp spread spectrum
eDRX, PSM | Extended discontinuous reception; power saving mode
ISM | Unlicensed industrial, scientific and medical bands
MCL | Maximum coupling loss
OTAA, ABP | Over-the-air activation; activation by personalisation
SF | Spreading factor, SF7 to SF12
```

## In short {.summary}

LoRaWAN for private gateways and no SIM costs; NB-IoT for national coverage deep indoors; LTE-M for things that move and large updates.

### Own the network

One rooftop gateway covers a farm or factory, with no subscription per sensor.

### Reach the basement

Licensed spectrum, 23 dBm and repetition reach where unlicensed radios cannot.

### Follow the asset

LTE-M hands over between towers across countries.
