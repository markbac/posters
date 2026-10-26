---
title: "Low-Power Embedded Design: Sleep Modes and Battery Maths"
subtitle: Hardware and firmware that run for ten years on one primary cell
byline: Embedded hardware engineering
orientation: landscape
columns: 3
paper: a1
width: 1750
document_number: PO-012
colours:
  accent: "#16a34a"
  secondary: "#15803d"
footer:
  left: Low-Power Design
  centre: Embedded Engineering Reference
  qr: https://en.wikipedia.org/wiki/Low-power_electronics
  qr-label: Low-power electronics
---

## Key figures {.stats style=tiles}

| Value | Label |
|---|---|
| Under 3 µA | Deep-sleep target for a ten-year battery |
| 99.9 % | Of its life a sensor node spends asleep |
| 15 to 30 % | Of a cell's capacity lost to self-discharge, cold and pulse loads |
| 100 µA | Wasted by one forgotten 33 kΩ pull-up at 3.3 V |

## Introduction {.abstract}

A sensor node that runs for five or ten years on one battery is an exercise in **microamp accounting**. It sleeps 99.9 % of the time. So a 50 µA leak from a floating pin, a hungry regulator or a clock left running uses more charge in a year than thousands of radio messages. Long life comes from the right cell, the lowest sleep current, and waking for as few milliseconds as possible.

## 1. The battery equation {.wide}

Average the current over one whole cycle: wake, measure, send, sleep. Here, one report every 15 minutes:

| State, in a 900 s cycle | Time | Current | Charge per cycle | Share of the average |
|---|---|---|---|---|
| Deep sleep | 898.5 s | 2.5 µA | 2,246 µAs | 2.5 µA |
| Read the sensor | 0.3 s | 1.2 mA | 360 µAs | 0.4 µA |
| Radio send and acknowledge | 1.2 s | 45 mA | 54,000 µAs | 60.0 µA |
| **Average** | **900 s** | | **56,606 µAs** | **62.9 µA: 551 mAh a year** |

## 2. A year of charge

```chart type=waterfall title="A year of charge, and one leak (mAh)" unit=" mAh" height=260
Sleep | +22 | green |
Sensor | +4 | blue |
Radio | +526 | amber | Time is sleep, energy is radio
Designed | =552 | navy |
A 100 µA leak | +876 | red | More than everything else
Shipped | =1428 | red |
```

## 3. Currents, from off to transmitting

```logscale unit=" A"
5e-8 | Shutdown | green
2.5e-6 | Deep sleep (STOP) | teal
1e-3 | CPU halted, clocks on | blue
4e-3 | Running | navy
4.5e-2 | Radio transmitting | red
```

Each step to the right costs ten to a thousand times more.

## 4. Choosing a cell

```cards cols=1 style=top
Coin cells, CR2032 and CR2477 | Li-MnO₂, 3.0 V, 220 to 1,000 mAh, with 10 to 30 Ω inside: keep pulses under about 15 mA, or the voltage sags into brown-out | amber
Li-SOCl₂, AA to D | 3.6 V, 2,400 to 19,000 mAh, under 1 % self-discharge a year, −55 to +85 °C. Bobbin cells need a hybrid layer capacitor for cellular bursts | green
Alkaline or Li-FeS₂, 2 × AA | 3.0 V, 1,500 to 3,000 mAh, cheap and safe; Li-FeS₂ handles pulses and does not leak | blue
```

```chart type=line title="Voltage over the cell's life" unit=" V" min=1.8 max=3.8 step=0.5 height=200 colours=green,blue,amber values=last
series: Li-SOCl₂, Coin, 2 × alkaline
0 % | 3.62 | 3.05 | 3.10
25 % | 3.60 | 2.92 | 2.75
50 % | 3.58 | 2.86 | 2.50
75 % | 3.55 | 2.78 | 2.25
95 % | 3.20 | 2.40 | 1.90
```

> [!TIP]
> Li-SOCl₂ stays at 3.6 V for 90 % of its life, so its voltage says nothing about what is left. Count the milliseconds of radio and activity in firmware instead.

## 5. Sleep modes {.wide}

```compare
| Sleep | Deep sleep (STOP, LPM3) | Shutdown (Standby, LPM4.5)
Fast clocks | Running; peripherals active | **Off**: only the 32.768 kHz RTC | **Off**; RTC optional
RAM and registers | Kept | Kept | **Lost**, except a few backup registers
Current | 300 µA to 2 mA | **1.2 to 4 µA**: the workhorse | **0.05 to 0.4 µA**
Wake-up | Under 2 µs | **5 to 50 µs**, carrying on after WFI | 0.5 to 2 ms: a full reboot
```

## 6. Six leaks, in the order to check them {.wide}

```steps cols=3
Floating inputs | An unconnected CMOS input floats near half the supply and leaks 50 to 500 µA: set unused pins to analogue | red
Pins fighting pull-ups | A pin driven low against a 10 kΩ pull-up leaks 330 µA: release SPI and UART pins before sleep | red
Regulators | A 1117 regulator draws 5 mA doing nothing: choose one under 500 nA | amber
Battery dividers | Two 10 kΩ resistors across 3.6 V drain 180 µA for ever: switch the divider, or use megohms and a capacitor | amber
Flash left awake | SPI NOR flash idles at 15 to 50 µA until it gets the deep power-down command, 0xB9 | blue
The debugger | A connected SWD probe keeps the debug domain powered: measure with it unplugged | navy
```

## 7. Measuring it {style=card colour=green}

A multimeter's µA range drops over 100 mV across its shunt, so the node browns out the moment the radio draws 50 mA. Use a source meter or power profiler that ranges from nanoamps to amps:

```highlight
2.41 µA | Sleep floor | Minimum 2.38, maximum 2.47 | green
```

Over 15 minutes it averaged **64.1 µA**: 8.9 years on a 5 Ah cell. Toggle a spare pin around each code phase, to line up current spikes with code on a scope.

## 8. Sign-off checklist

```checklist
[x] Every unused pin set to analogue before sleep
[x] Regulator quiescent current under 1 µA
[x] Sensors, transceivers and dividers switched off with load switches
[x] Sleep current measured at −20, +25 and +60 °C, debugger off, with 30 % margin
```

## 9. Glossary

```glossary cols=1
BOR | Brown-out reset
HLC | Hybrid layer capacitor, for pulse current
Iq | Quiescent current of a regulator or chip
LDO | Low-dropout linear regulator
RTC | Real-time clock, 32.768 kHz
SWD | Serial Wire Debug
WFI | Wait for interrupt: the CPU's sleep instruction
µAs | Microamp-seconds of charge
```

## In short {.summary}

Sleep current sets a ten-year battery life. Choose a nanoamp regulator, switch off every unused pin and peripheral, and send in short bursts so the node sleeps 99.9 % of the time.

### Fix the leaks first

Cutting sleep from 52 µA to 2 µA saves 438 mAh a year: twice the life of a coin cell.

### Never spin-wait

Replace `delay_ms()` loops with a timer interrupt and WFI.

### Match the cell to the pulse

Back a high-resistance lithium cell with a capacitor, so winter radio bursts never brown it out.
