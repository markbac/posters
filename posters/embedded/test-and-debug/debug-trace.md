---
title: "Hardware Debugging and Real-Time Trace"
subtitle: Reading memory, registers, fault frames and live execution over two debug pins
byline: Embedded test and debug
orientation: portrait
columns: 2
paper: a1
width: 1200
document_number: PO-016
colours:
  accent: "#0f766e"
  secondary: "#115e59"
footer:
  left: Debug and Trace
  centre: Embedded Engineering Reference
  qr: https://developer.arm.com/documentation/ddi0403/latest/
  qr-label: Armv7-M Architecture Reference
---

## Key figures {.stats style=tiles}

| Value | Label |
|---|---|
| 2 pins | For Serial Wire Debug: SWDIO and SWCLK |
| Under 1 µs | To log a line with RTT, into target RAM |
| 8 words | Pushed to the stack by a Cortex-M fault |
| 4 to 8 | Hardware breakpoints in a Cortex-M |

## Introduction {.abstract}

`printf` over a slow serial port changes interrupt timing and hides races. Microcontrollers have **debug silicon** reached over 2-pin **Serial Wire Debug (SWD)** or 4-pin **JTAG**. Without halting the CPU, a probe can read and write RAM, and stream logs in under a microsecond with **RTT**. It can sample the program counter over **SWO**, and decode the frame a crash leaves behind.

## 1. The debug connection {.wide}

```flow
[GDB, with the ELF's symbols|navy] -USB-> [Probe: J-Link, ST-Link, CMSIS-DAP|teal] -SWDIO, SWCLK-> [Debug access port|blue] -bus matrix-> [Core, RAM and flash, live|green]
```

```cards cols=3 style=top
JTAG | IEEE 1149.1, on TDI, TDO, TCK and TMS: boundary scan, and several chips in a chain | navy
SWD | Arm's two-wire protocol, SWDIO and SWCLK, with ground and a target voltage sense | teal
SWO | One more pin for trace: ITM messages, interrupt entry and exit, and PC samples, at megabits a second | blue
```

## 2. The standard header

The 10-pin, 1.27 mm Cortex debug connector. Put one on every prototype.

```pinout package=header rows=2
1 | VTref | pwr
2 | SWDIO | swd
3 | GND | gnd
4 | SWCLK | swd
5 | GND | gnd
6 | SWO | swd
7 | KEY | nc
8 | NC | nc
9 | GNDdetect | gnd
10 | nRESET | reset
```

## 3. Logging without disturbing timing

```compare
| UART printf | SWO and ITM | SEGGER RTT
Extra pins | 1 or 2 | 1: SWO | **None**: uses the SWD pins
Time to log 32 bytes | **2,780 µs** at 115,200 baud | About 16 µs | **Under 1 µs**: a copy into RAM
Safe in a fast interrupt | **No** | Yes, if non-blocking | **Yes**
Works with no probe | Yes | No | No
```

```logscale unit=" s" title="Time to log 32 bytes"
1e-6 | RTT | green
1.6e-5 | SWO | blue
2.78e-3 | UART, 115,200 baud | red
```

## 4. What a crash leaves behind

A bad pointer, a divide by zero or a jump into garbage makes the hardware push eight registers onto the stack, then enter `HardFault_Handler`:

```tape
cells: R0 R1 R2 R3 R12 LR PC xPSR
1-4 | Arguments | blue
5-5 | Scratch | teal
6-6 | Caller | amber
7-7 | The faulting instruction | red
8-8 | Status | navy
```

```terminal title="GDB, at the HardFault"
(gdb) p/x SCB->CFSR
$1 = 0x8200
(gdb) p/x SCB->BFAR
$2 = 0x4
(gdb) info symbol 0x080041a2
read_sensor + 18 in section .text
$ arm-none-eabi-addr2line -f -e app.elf 0x080041a2
read_sensor
sensor.c:84
-- CFSR 0x8200: a precise bus fault at the address in BFAR, 0x4: a NULL struct pointer, field +4
```

> [!TIP]
> Copy the frame, CFSR and BFAR into a `.noinit` RAM struct before the watchdog reset. On the next boot, send the crash line to the cloud.

## 5. Breakpoints and watchpoints

Flash cannot be patched quickly, so the core has comparators:

```cards cols=2 style=label
FPB | Flash patch and breakpoint: 4 to 8 comparators that halt when an instruction address matches
DWT watchpoints | 1 to 4 comparators that halt the moment code reads or writes a chosen address: buffer overruns caught red-handed
DWT CYCCNT | A 32-bit counter of every CPU clock, for measuring a function in cycles
ETM | Embedded trace macrocell: every branch, over a 4-bit trace port, for full instruction replay
```

## 6. Checklist {style=card colour=teal}

```checklist
[x] SWDIO, SWCLK, SWO, nRESET, VTref and GND on a 10-pin Cortex header on prototypes
[x] A HardFault handler that keeps PC, LR, CFSR and BFAR in `.noinit` RAM across the reset
[x] The ELF and map file of every release archived, to turn field crash addresses into lines
[x] CYCCNT used in bring-up to measure the worst case of each interrupt
[x] Read-out protection on in production, so no one can dump keys over SWD
```

## 7. Glossary {.wide}

```glossary cols=4
CFSR, BFAR | Configurable fault status, and bus fault address, registers
DAP | Debug access port
FPB, DWT | Flash patch and breakpoint; data watchpoint and trace
ITM | Instrumentation trace macrocell
PC, LR, SP | Program counter, link register, stack pointer
RTT | SEGGER Real-Time Transfer
SWD, SWO | Serial Wire Debug, Serial Wire Output
xPSR | Program status register
```

## In short {.summary}

Log with RTT or SWO, which never disturb timing. Catch corruption with DWT watchpoints, and keep every HardFault frame in retained RAM.

### Stop printing over serial

A UART line stalls an interrupt for milliseconds. RTT copies it in under a microsecond.

### Let watchpoints catch it

When a variable changes mysteriously, a write watchpoint stops on the exact instruction.

### Record every field crash

The stacked PC, LR and CFSR turn a mysterious reset into a one-line fix.
