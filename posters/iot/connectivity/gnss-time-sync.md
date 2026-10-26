---
title: "Positioning and Time Synchronisation"
subtitle: From satellite pseudoranges and centimetre corrections to nanosecond network clocks
byline: IoT connectivity
orientation: landscape
columns: 3
paper: a1
width: 1750
document_number: PO-024
colours:
  accent: "#0369a1"
  secondary: "#075985"
footer:
  left: GNSS and Time Sync
  centre: IoT Engineering Reference
  qr: https://en.wikipedia.org/wiki/Satellite_navigation
  qr-label: Satellite navigation
---

## Key figures {.stats style=tiles}

| Value | Label |
|---|---|
| 4 satellites | To solve position and the receiver's clock error |
| 1 to 2 cm | With RTK carrier-phase corrections; 2.5 m without |
| About 30 s | To a first fix from cold, decoding data at 50 bps |
| Under 100 ns | Clock accuracy from a PPS pin or PTP |

## Introduction {.abstract}

Every **GNSS** receiver is a precision clock. Radio travels **30 cm per nanosecond**, so timing signals from orbiting atomic clocks gives both a position and **UTC**. **Assisted GNSS** cuts the battery cost of a fix, **RTK** brings centimetres, and **PTP** brings nanosecond clocks to industrial networks.

## 1. Why four satellites

```equation
title: One pseudorange per satellite
\rho_i = \sqrt{(x - x_i)^2 + (y - y_i)^2 + (z - z_i)^2} + c \, \Delta t
\rho_i | Measured range to satellite i | m
x, y, z | The receiver's position: three unknowns | m
\Delta t | The receiver's clock error: the fourth | s
```

A receiver clock 1 µs off is a **300 m** error, so a fourth satellite is needed to solve for it.

```cards cols=1 style=top
Two bands, L1 and L5 | L1 (1575.42 MHz) is slowed by the ionosphere and bounces off glass. Adding L5 (1176.45 MHz) cancels the delay and rejects reflections | blue
One pulse per second | Once locked, the module raises a pin at the start of each UTC second, to within 10 to 30 ns | green
```

## 2. The receiver chain

```flow
[4 or more satellites, 20,200 km up|navy] -−130 dBm, below the noise-> [Antenna, LNA, SAW filter|blue] -> [Baseband: correlates codes|teal] -NMEA or UBX, and PPS-> [MCU|green]
[Cloud A-GNSS server|amber] -1 to 3 KB over LTE-M or NB-IoT-> [Baseband: correlates codes|teal]
```

## 3. Cold, warm, assisted and hot starts

| Start | What the receiver already has | Time to first fix | Charge at 25 mA | Energy at 3.3 V |
|---|---|---|---|---|
| Cold | Nothing: search, then decode 50 bps orbit data | 30 to 45 s | About 875 mAs | About 2.9 J |
| Warm | Almanac, rough time and position | 15 to 25 s | About 500 mAs | About 1.6 J |
| **Assisted** | Orbits sent over the network | **2 to 4 s** | **About 75 mAs** | **About 0.25 J** |
| **Hot** | Orbits under 2 hours old, and the time | **About 1 s** | **About 25 mAs** | **About 0.08 J** |

> [!WARNING]
> Keep the module's backup supply, **V_BCKP**, powered while it sleeps. Lose it, and every wake-up is a 35-second cold start.

## 4. From metres to centimetres

Ordinary GNSS measures the code, whose chips are about 300 m long, to 1.5 to 3 m. **RTK** locks onto the **19 cm** carrier itself. Corrections come from a fixed base station, over NTRIP:

```logscale unit=" m"
2.5 | Single band | red
0.9 | L1 and L5 | amber
0.6 | SBAS: WAAS, EGNOS | amber
0.25 | RTK float | blue
0.02 | RTK fixed | green
```

```syntax-anatomy width=1200
$GNGGA,091422.00,5130.45128,N,00007.67341,W,4,18,0.6,48.2,M
GNGGA | Sentence: multi-GNSS fix | navy
091422.00 | UTC 09:14:22 | blue
5130.45128,N | Latitude 51° 30.45′ N | green
00007.67341,W | Longitude 0° 7.67′ W | green
4 | Fix quality 4: RTK fixed | red
18 | Satellites used | amber
0.6 | HDOP | amber
48.2,M | Altitude, metres | grey
```

## 5. Keeping clocks together {.wide}

```compare
| NTP and SNTP | IEEE 1588 PTP | GNSS PPS and time messages
Accuracy | **1 to 20 ms**, over the internet | **10 to 200 ns**, on a local network | **10 to 50 ns**, anywhere with sky
Timestamped in | Software: OS and queue jitter | **Hardware**, in the Ethernet MAC or PHY | A hardware timer capture pin
Needs | Any UDP connection, port 123 | PTP-aware switches | A view of the sky
Used for | Certificate expiry, cloud logs | Motion control, audio and video, 5G cells | Seismic sensors, grid phasors, telecom
```


## 6. Clock accuracy

```logscale unit=" s"
2e-2 | NTP over the internet | red
1e-3 | NTP on a LAN | amber
2e-7 | PTP | blue
3e-8 | GNSS PPS | green
```

## 7. Board and timing checklist {style=card colour=blue}

```checklist
[x] V_BCKP always powered, and A-GNSS data sent on cold boots, for fixes in under 3 s
[x] The 50 Ω antenna trace kept away from regulators, SPI clocks and cellular antennas, with a SAW filter
[x] The ground plane the patch antenna's datasheet asks for, such as 50 × 50 mm
[x] PPS captured by a timer input, then labelled with the UTC second from the next message
[x] Timestamps stored as 64-bit epoch values: 32-bit seconds overflow in 2038
```

## 8. Glossary

```glossary cols=1
A-GNSS | Assisted GNSS
HDOP | Horizontal dilution of precision: satellite geometry
NMEA | The ASCII sentence format of GNSS receivers
NTRIP | Networked transport of RTCM corrections over IP
PPS | Pulse per second
PTP | Precision Time Protocol, IEEE 1588
RTK | Real-time kinematic
TTFF | Time to first fix
```

## In short {.summary}

Keep V_BCKP powered and send A-GNSS data, so trackers fix in 2 s, not 35. Use RTK for centimetres, and PPS or PTP when NTP's jitter is too large.

### Never cold-start on a coin cell

Decoding orbits at 50 bps costs ten times the energy of fetching 2 KB over the network.

### PPS and messages together

The serial message says which second it is; the PPS pin says exactly when it starts.

### 64-bit time

A signed 32-bit Unix time overflows on 19 January 2038.
