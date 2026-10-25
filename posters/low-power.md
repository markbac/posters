---
title: "Low-Power Embedded Design: Sleep Modes and Battery Maths"
subtitle: Engineering hardware and firmware to run for ten years on a single primary cell
byline: Ultra-Low-Power Hardware & Firmware Engineering Explainer
orientation: landscape
paper: a1
width: 1750
document_number: PO-012
version: "1.0"
colours:
  accent: "#16a34a"
  secondary: "#15803d"
footer:
  left: Low-Power Embedded Design Explainer
  centre: Hardware & Firmware Power Reference
  right: Battery Budgeting & Sleep Architecture Guide
  qr: https://en.wikipedia.org/wiki/Low-power_electronics
  qr-label: Low-Power Design
---

## Key figures {.stats style=tiles}

| Value | Label | Change | Verdict |
|---|---|---|---|
| < 3 µA | Target deep-sleep current for a 10-year coin or lithium cell | 99.9% of time | good |
| 8,760 h | Hours in one year (`87,600 hours` in a 10-year product lifetime) | duty-cycle maths | good |
| 15 to 30% | Capacity lost to self-discharge, temperature and pulse derating | safety margin | bad |
| 100 µA | Current leaked by one forgotten `33 kΩ` pull-up resistor at `3.3 V` | kills battery | bad |

## Introduction {.abstract}

Building a sensor node that runs for five to ten years on a single battery is a discipline of **microampere accounting**. Because the device sleeps for **99.9%** of its life, a tiny `50 µA` sleep leak drains more charge over a year than thousands of radio transmissions. Such leaks often come from a floating **General-Purpose Input/Output (GPIO)** pin, a noisy voltage regulator or an unclosed peripheral clock. Long battery life comes from choosing the right cell chemistry, minimising sleep quiescent current (`Iq`) and waking for as few milliseconds as possible.

## 1. The battery life equation: calculating average current

Engineers express battery capacity in **milliampere-hours (`mAh`)**. To estimate lifetime, compute the time-weighted average current (`I_avg`) across one complete wake-measure-send-sleep cycle of duration `T_cycle`:

```figure
@segments
title: One 15-minute (900 s) reporting cycle — Sleep current dominates time; Radio current dominates energy!
7 | 1. Deep Sleep (898.5 s at 2.5 µA) | 2,246 µAs charge | green
2 | 2. Wake & Sample Sensor (0.3 s at 1.2 mA) | 360 µAs charge | blue
3 | 3. Radio Transmit & ACK (1.2 s at 45 mA) | 54,000 µAs charge | amber
+++
@lanes
Bad firmware (Polling) | *CPU spinning in delay_ms() at 4 mA | *Sensor conversion | *Blocking UART wait | Drains 1,000 mAh cell in 10 days!
Event-driven low power | *RTC wakes MCU | *Start ADC + DMA (CPU sleeps) | *Burst Tx | *Shut down peripherals & enter 2 µA STOP mode
```

| State in a 900 s cycle | Duration (`t`) | Current (`I`) | Charge per cycle (`I × t`) | Contribution to average current |
|---|---|---|---|---|
| Deep Sleep (`STOP2`) | `898.5 s` | `2.5 µA` | `2,246 µAs` | `2.50 µA` |
| Sensor Read (`I2C`) | `0.3 s` | `1.2 mA` | `360 µAs` | `0.40 µA` |
| Radio Burst (`Tx/Rx`) | `1.2 s` | `45.0 mA` | `54,000 µAs` | `60.00 µA` |
| **Cycle Total / Average** | **`900.0 s`** | — | **`56,606 µAs`** | **`I_avg = 62.9 µA`** (`~551 mAh / year`) |

```chart type=bar title="Where 1 year of battery charge goes in the 15-minute sensor above (mAh/year)" unit=" mAh" max=950
Radio Tx (1.2 s) | 525
Deep Sleep (2.5 uA) | 22
Sensor Read (0.3 s) | 4
100 uA PCB Leak! | 876
```

> [!WARNING]
> Notice the bottom bar: an accidental **`100 µA` sleep leak** consumes **`876 mAh` every year**—more than the radio, sensor and sleep current combined!

## 2. Microcontroller sleep modes: retention vs wake time

Modern microcontrollers offer a ladder of sleep states that trade clock shutdown depth against wakeup latency:

```compare
| Sleep (CPU Halted) | Deep Sleep (`STOP` / `LPM3`) | Standby / Shutdown (`LPM4.5`)
High-speed clocks (`PLL`, `HSI`) | Running (peripherals stay active) | **Switched off** (only `32.768 kHz` RTC runs) | **Switched off** (optional RTC)
SRAM & register retention | Full SRAM & CPU registers kept | Full SRAM & registers kept | Lost (except tiny backup registers)
Typical current | `300 µA` to `2 mA` | **`1.2 µA` to `4 µA`** (workhorse mode) | **`0.05 µA` to `0.4 µA`**
Wakeup latency | `< 2 µs` (any interrupt) | **`5 µs` to `50 µs`** (resumes right after `WFI`) | `0.5 ms` to `2 ms` (full reboot from `Reset_Handler`)
```

## 3. Choosing a primary battery chemistry

Not all `3 V` batteries can deliver radio transmit pulses or survive outdoor winters:

```cards cols=3 style=top
CR2032 / CR2477 (`Li-MnO2`, 3.0 V) | Compact coin cells (220 to 1,000 mAh) with high internal resistance (10–30 Ω); continuous current must stay under ~15 mA or voltage sags below brown-out | amber
AA / C `Li-SOCl2` (3.6 V, Bobbin / Spiral) | Lithium Thionyl Chloride cells (2,400 to 19,000 mAh) with < 1% annual self-discharge and -55 to +85 °C range; pair bobbin cells with a hybrid layer capacitor (`HLC`) for cellular bursts | green
2x AA Alkaline / `Li-FeS2` (3.0 V) | Inexpensive, safe cells (1,500 to 3,000 mAh); `Li-FeS2` handles high pulse currents well and avoids alkaline leakage | blue
```

```chart type=line title="Discharge voltage curve over battery life (Volts)" unit=" V" min=1.8 max=3.8 step=0.5 height=200 colours=green,blue,amber values=last
series: Li-SOCl2 (3.6V flat), Li-MnO2 Coin (3.0V), 2x Alkaline (sloped)
0% Used | 3.62 | 3.05 | 3.10
25% Used | 3.60 | 2.92 | 2.75
50% Used | 3.58 | 2.86 | 2.50
75% Used | 3.55 | 2.78 | 2.25
95% Used | 3.20 | 2.40 | 1.90
```

> [!TIP]
> Because **Lithium Thionyl Chloride (`Li-SOCl2`)** stays flat at `3.60 V` for 90% of its life, simple voltage dividers cannot estimate remaining capacity. Instead, count cumulative radio and active milliseconds in firmware (**coulomb counting**).

## 4. Six hardware & firmware traps that ruin sleep current

When your prototype measures `180 µA` in sleep instead of `3 µA`, check these six culprits in order:

```steps
Floating GPIO inputs | An unconnected CMOS input pin floats near Vdd/2, turning on both P and N transistors and leaking 50 to 500 µA; configure unused pins as Analogue mode
Driven pull-up or I2C lines | A pin driven low against an external 10 kΩ pull-up leaks 330 µA continuously; de-initialise SPI/UART pins before sleeping
Greedy voltage regulators | A standard 1117 Linear Regulator (LDO) burns 5,000 µA of quiescent current (Iq) doing nothing; pick a nanopower LDO or buck regulator with Iq < 500 nA | green
Battery voltage divider | Two 10 kΩ resistors across a 3.6 V cell drain 180 µA forever; switch the divider with a high-side P-MOSFET or use 2 MΩ resistors with a filter capacitor | amber
External Flash left awake | An SPI NOR Flash chip idles at 15 to 50 µA unless firmware sends the Deep Power-Down opcode (0xB9) before sleeping | blue
Debug probe attached | Leaving SWD / JTAG connected keeps the MCU debug clock domain powered (~400 µA); always measure sleep current with the debugger physically unplugged! | navy
```

## 5. Measuring microamps to milliamps {style=card colour=green}

A handheld multimeter cannot measure low-power nodes: its `µA` range has a high **burden voltage** (`> 100 mV` across a `100 Ω` shunt) that causes the microcontroller to brown out the instant the radio transmits `50 mA`:

```lcd cols=2
[Source Meter / Power Profiler]
Sleep floor:   2.41 uA
Tx peak:      48.20 mA (1.18 s)
Avg (15 min): 64.10 uA -> 8.9 yrs
-- Auto-ranging source meter (nA to 1 A)

// Firmware GPIO profiling marker:
GPIO_SET(DBG_PIN);   // Scope trigger high
radio_transmit_pkt();
GPIO_CLR(DBG_PIN);   // Measure pulse width!
-- Correlate code phases with current spikes
```

## 6. Low-power sign-off checklist

```checklist
[x] All unused MCU pins configured as Analogue input (Schmitt trigger disabled) before entering STOP mode
[x] DC-DC or Low-Dropout (LDO) regulator quiescent current (`Iq`) is under `1 µA` at no load
[x] Peripheral power domains (sensors, RS-485 transceiver, voltage dividers) switched via load switches or GPIO
[x] Sleep current verified at `-20 °C`, `+25 °C` and `+60 °C` with debugger disconnected and 30% battery margin applied
```

## 7. Acronym guide: every term defined {.wide}

```cards cols=4 style=label
Iq | Quiescent Current: no-load standby current drawn continuously by a voltage regulator or sensor chip
LDO & Buck | Low-Dropout linear regulator and step-down switched-mode Buck converter
RTC & WFI | Real-Time Clock (`32.768 kHz` sleep timer) and Wait For Interrupt (`WFI` CPU sleep instruction)
CMOS & GPIO | Complementary Metal-Oxide-Semiconductor logic gates and General-Purpose Input/Output pins
MOSFET | Metal-Oxide-Semiconductor Field-Effect Transistor: electronic switch used to cut power to hungry sensors
Li-SOCl2 & HLC | Lithium Thionyl Chloride (`3.6 V` primary cell) and Hybrid Layer Capacitor (absorbs high pulse currents)
BOR / BOD | Brown-Out Reset / Brown-Out Detector: hardware circuit that resets the MCU safely if battery voltage sags
SWD / JTAG | Serial Wire Debug and Joint Test Action Group: microcontroller debug interfaces that must be unplugged for sleep tests
PLL & HSI | Phase-Locked Loop and High-Speed Internal oscillator: fast clocks switched off during deep sleep
DMA & ADC | Direct Memory Access and Analogue-to-Digital Converter: sample sensors while the CPU core sleeps
```

## In short {.summary}

Sleep current governs ten-year battery life. Pick a sub-microamp regulator, shut down every unused pin and peripheral, and batch radio bursts so the node sleeps 99.9% of the time.

### Eliminate sleep leaks first

Cutting sleep current from `52 µA` to `2 µA` saves `438 mAh` every year—more than doubling the life of a coin cell.

### Never spin-wait in firmware

Replace every `delay_ms()` loop with a hardware timer interrupt and `WFI` so the CPU sleeps while waiting for sensors.

### Match cell to pulse current

Pair high-impedance lithium cells with a supercapacitor or hybrid layer capacitor so winter radio bursts never trigger a brown-out reset.
