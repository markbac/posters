---
title: "Embedded Rust vs C for Bare-Metal Firmware"
subtitle: Memory safety at compile time, typestate drivers and zero-cost abstractions, with no garbage collector
byline: Embedded firmware engineering
orientation: landscape
columns: 3
paper: a1
width: 1750
document_number: PO-026
colours:
  accent: "#c2410c"
  secondary: "#9a3412"
footer:
  left: Embedded Rust vs C
  centre: Embedded Engineering Reference
  qr: https://docs.rust-embedded.org/book/
  qr-label: The Embedded Rust Book
---

## Key figures {.stats style=tiles}

| Value | Label |
|---|---|
| 0 bytes | Of runtime, garbage collector or OS needed by no_std Rust |
| About 70 % | Of severe security bugs in large C and C++ code bases that are memory-safety bugs |
| 1 or many | One mutable reference, or many shared ones: never both |
| 0 cycles | Cost of typestate checks: they all happen at compile time |

## Introduction {.abstract}

C has ruled microcontrollers for forty years because other languages needed a runtime or a garbage collector. **Rust** does not: with `no_std` it compiles through LLVM to bare-metal Cortex-M and RISC-V code, in about the RAM of C. Its **ownership** rules and **typestate** drivers turn null pointers, buffer overflows, data races and misconfigured pins into **compile errors**.

## 1. Three guarantees C leaves to discipline {.wide}

```cards cols=3 style=top
Ownership and borrowing | Every value has one owner. You may hold **one** mutable reference (`&mut T`) **or** any number of shared ones (`&T`), never both, so aliasing bugs and dangling pointers do not compile | amber
Typestate peripherals | Nothing in C stops `spi_write()` before the clock is on. In Rust, configuring a pin **consumes** the old pin and returns a new type: using the old one is a compile error | green
Safe concurrency | In C, any interrupt can write any global. In Rust, shared mutable state must be wrapped, such as in a `Mutex`, and opened with a critical-section token | blue
```

## 2. A pin, in C and in Rust {.wide}

```code-compare
@bad C: registers and hope
GPIOA->MODER |= (1U << 10);   /* PA5 output */
GPIOA->ODR   |= (1U << 5);    /* PA5 high   */
/* elsewhere, someone makes PA5 an input */
GPIOA->MODER &= ~(3U << 10);
GPIOA->ODR   |= (1U << 5);    <1>
@good Rust: the type is the state
let gpioa = dp.GPIOA.split();
let mut led = gpioa.pa5.into_push_pull_output();
led.set_high();
let btn = led.into_floating_input();   <2>
led.set_high();                        <3>
-- 1 | Compiles, runs, and the pin never moves: found only with a scope
-- 2 | Turning the pin into an input consumes led
-- 3 | Compile error: value led used after move
```

What the type of `led` says:

```syntax-anatomy width=2400
PA5<Output<PushPull>>
PA5 | Which pin | navy
Output | Its mode | green
PushPull | Its drive | amber
```

## 3. The crate layers

Each layer is generated from, or built on, the one below. Every HAL implements the `embedded-hal` traits, so one sensor driver works on STM32, nRF52, RP2040 and ESP32 unchanged.

```stack
Application | app | Your firmware, with forbid(unsafe_code) | green
Drivers | bme280 | Portable sensor and display crates | teal
embedded-hal | traits | SPI, I2C, delay and pin interfaces | blue
HAL | stm32f4xx-hal | Typestate drivers for one family | navy
PAC | svd2rust | Register structs, from the vendor's SVD file | grey
side: unsafe lives here | 4-5 | red
```

## 4. Concurrency without an RTOS

```cards cols=1 style=label
RTIC | Uses the interrupt controller (NVIC) as the scheduler, with priority-ceiling locks: one shared stack and no deadlocks, proved at compile time
Embassy | Compiles async tasks into state machines. Waits for DMA, timers and radio with no stack per task to size
defmt | Leaves format strings on the host: the MCU sends a string index and raw values over RTT
C and Rust together | Call C from Rust with bindgen, or link a Rust static library into a C project one module at a time
```

## 5. Adopting Rust {style=card colour=amber}

```checklist
[x] Start `no_std` and `no_main`, with `heapless` for fixed-size collections
[x] Optimise for size, with link-time optimisation, so abstractions inline away
[x] Use probe-rs, defmt and flip-link, which puts the stack at the bottom of RAM so an overflow faults at once
[x] Keep `unsafe` in the HAL and PAC; forbid it in application code
[x] Migrating C? Build one new parser or crypto module in Rust as a static library first
```

```toml
[profile.release]
opt-level = "z"
lto = true
codegen-units = 1
```

## 6. Head to head {.wide}

```compare
| Embedded C (C99, C11) | Embedded Rust (no_std, embedded-hal)
Bounds | `buf[i]` is unchecked and can overwrite the stack | Slices are checked, or iterators need no index at all
Null and errors | NULL pointers and ignored return codes | No null: `Option<T>` and `Result<T, E>`, which must be used
Interrupt safety | `volatile` and discipline | Enforced by the compiler: critical sections, **RTIC** or **Embassy**
Build and reuse | CMake, Make, vendor ZIP files | **Cargo**, crates.io and probe-rs
Hardware access | Anywhere: any cast is legal | Only inside `unsafe { }` blocks, typically a few percent of the code
Safety certification | Mature ISO 26262 toolchains | **Ferrocene**: a Rust compiler qualified for ISO 26262 and IEC 61508
```

## 7. Glossary {.wide}

```glossary cols=4
FFI | Foreign function interface: calling across languages
HAL | Hardware abstraction layer
LLVM | The compiler back end of rustc and clang
LTO | Link-time optimisation
NVIC | Nested Vectored Interrupt Controller, in every Cortex-M
PAC | Peripheral access crate: generated register structs
RTIC | Real-Time Interrupt-driven Concurrency
SVD | System View Description: a chip's registers, in XML
```

## In short {.summary}

Embedded Rust keeps C's speed and memory layout, and turns data races, null pointers, overruns and misconfigured pins into compile errors.

### Typestate costs nothing

Pin states in the type system catch configuration mistakes in the editor, with no runtime cost.

### Keep unsafe small

With the application free of unsafe code, memory bugs can only hide in the thin layer next to the hardware.

### Async without a heap

Embassy and RTIC give clear concurrent code on one stack, with no thread stacks to guess.
