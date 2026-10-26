---
title: "Embedded Testing, Mocking and Hardware-in-the-Loop"
subtitle: A test pyramid from sub-second host tests to automated hardware rigs
byline: Embedded test and debug
orientation: portrait
columns: 2
paper: a1
width: 1200
document_number: PO-027
colours:
  accent: "#15803d"
  secondary: "#166534"
footer:
  left: Embedded Testing and HIL
  centre: Embedded Engineering Reference
  qr: https://www.throwtheswitch.org/
  qr-label: ThrowTheSwitch
---

## Key figures {.stats style=tiles}

| Value | Label |
|---|---|
| Under 2 s | To run 500 unit tests on a laptop |
| About 80 % | Of firmware logic that can be tested off target, behind a HAL |
| 0 boards | Needed to run the real binary in Renode or QEMU |
| Every release | Checked on real silicon by a hardware-in-the-loop rig |

## Introduction {.abstract}

Testing a one-line change to a parser should not mean cross-compiling, flashing a board and pressing buttons. Fast embedded teams build a **test pyramid**. A thin **hardware abstraction layer (HAL)** keeps business logic away from vendor registers, so most of it compiles and runs on a laptop in milliseconds. The real binary then runs in a **simulator**, and on a **hardware-in-the-loop (HIL)** rig.

## 1. The pyramid

```pyramid
Hardware in the loop | 5 to 10 % | Real boards: electrical, DMA, timing, sleep current | navy
Virtual target | 15 to 20 % | The real ELF in Renode or QEMU: vectors, RTOS, radio networks | blue
Host unit tests | 70 to 80 % | gcc or clang on a PC, with mocks, sanitizers and coverage, in seconds | green
```

## 2. The pipeline

```flow
[Push|navy] -under 10 s-> [Host tests, analysis, ASan|green] -under 30 s-> [Cross-compile, size budgets|teal] -about 1 min-> [Renode|blue] -about 3 min-> [HIL bench|navy]
```

The fast stages catch most logic and memory bugs before a board is ever flashed.

## 3. A seam for the hardware {.wide}

Code that writes `I2C1->DR` cannot compile on a PC. Put a small interface between them: production links `i2c_stm32.c`, tests link a generated mock.

```c
/* temp_sensor.c: portable, no vendor headers */
#include "i2c_bus.h"

err_t tmp102_read_celsius(uint8_t addr, float *out_c) {
    uint8_t raw[2] = {0};
    if (i2c_read_reg(addr, 0x00U, raw, 2U) != I2C_OK) {
        return ERR_BUS_FAULT;
    }
    int16_t counts = (int16_t)(((uint16_t)raw[0] << 4U) | (raw[1] >> 4U));
    *out_c = (float)counts * 0.0625f;
    return ERR_OK;
}
```

```c
/* test_temp_sensor.c: Unity and CMock, on a laptop, in 0.1 ms */
void test_tmp102_reads_25C(void) {
    uint8_t fake[2] = {0x19, 0x00};                 /* +25.0 °C */
    i2c_read_reg_ExpectAndReturn(0x48, 0x00, NULL, 2, I2C_OK);
    i2c_read_reg_IgnoreArg_buf();
    i2c_read_reg_ReturnArrayThruPtr_buf(fake, 2);
    float t = 0.0f;
    TEST_ASSERT_EQUAL(ERR_OK, tmp102_read_celsius(0x48, &t));
    TEST_ASSERT_FLOAT_WITHIN(0.01f, 25.0f, t);
}
```

A second test returns `I2C_NACK` and checks the error path: no sensor, no wiring, every commit.

## 4. Three environments {.wide}

```compare
| Host unit tests (Unity, CMock, GoogleTest) | Simulation (Renode, QEMU) | Hardware in the loop (pytest)
Compiler | The PC's gcc or clang | The target's arm-none-eabi-gcc | The target's arm-none-eabi-gcc
Speed | **Over 1,000 tests a second** | Real time, or deterministic virtual time | Real time, plus 10 to 30 s to flash
Logic and parser bugs | **Best: sanitizers and fuzzing** | Yes | Yes, slowly
Linker and vector bugs | No | **Yes**: the real startup and RTOS | **Yes**
Electrical, DMA and timing bugs | No | Partly: peripherals are models | **Yes**: real silicon, real microamps
```

## 5. A HIL bench

A Raspberry Pi or mini-PC runner, wired to the **device under test (DUT)**:

```steps
Power and current | A programmable supply or a power profiler cycles power, tests brown-out, and checks sleep stays under 3.5 µA
Debug probe | Flashes the new ELF with OpenOCD, pyOCD or probe-rs, and streams RTT logs back | blue
Stimulus | USB-CAN, USB-RS-485, a logic analyser or a helper MCU injects signals and frames | green
pytest | Fixtures flash, stimulate and assert, and publish a JUnit report to CI | navy
```

```terminal title="Nightly HIL run"
$ pytest hil/ -k "sleep or can"
hil/test_power.py::test_sleep_current PASSED   [2.41 µA < 3.50 µA]
hil/test_can.py::test_heartbeat_100ms PASSED
hil/test_can.py::test_bus_off_recovery PASSED
======== 3 passed in 41.2s ========
```

## 6. Testability checklist {style=card colour=green}

```checklist
[x] No vendor SDK headers in domain, protocol, filter or state-machine code
[x] Host tests run with `-fsanitize=address,undefined`, and over 80 % branch coverage of core logic
[x] Every frame decoder and parser fuzzed on the host with libFuzzer or AFL++
[x] A diagnostic shell over UART or RTT, so tests can trigger self-tests
[x] A nightly HIL power test that fails if sleep current goes up
```

## 7. Glossary

```glossary cols=1
DUT | Device under test
HAL | Hardware abstraction layer
HIL, SIL | Hardware in the loop, software in the loop
Mock | A generated stand-in that records calls and returns set values
Renode | An open-source simulator of whole embedded systems
Unity, CMock | A C test framework, and its mock generator
```

## In short {.summary}

Draw a strict HAL seam, so most firmware runs in sub-second host tests. Run the real binary in Renode in CI, and keep the HIL bench for electrical and power sign-off.

### Don't debug parsers on the board

A CRC or CBOR bug takes milliseconds to find on a PC with ASan.

### Mock the failures

Pulling an I2C wire at the right byte is hard by hand; one CMock line tests the recovery on every commit.

### Automate the sleep test

One forgotten pull-up ruins battery life. A nightly HIL test catches it.
