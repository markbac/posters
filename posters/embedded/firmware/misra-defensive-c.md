---
title: "Defensive Embedded C and Safety Guidelines"
subtitle: Removing undefined behaviour, memory corruption and concurrency traps from safety-critical firmware
byline: Embedded firmware engineering
orientation: portrait
columns: 2
paper: a1
width: 1200
document_number: PO-025
colours:
  accent: "#b91c1c"
  secondary: "#991b1b"
footer:
  left: Defensive Embedded C
  centre: Embedded Engineering Reference
  qr: https://misra.org.uk/
  qr-label: MISRA
---

## Key figures {.stats style=tiles}

| Value | Label |
|---|---|
| 0 | Heap allocations after start-up |
| Every loop | Has a provable upper bound, by the Power of 10 |
| Undefined | What C does on signed overflow or a null dereference |
| 3 gates | Strict warnings, static analysis and sanitizers, on every commit |

## Introduction {.abstract}

C gives firmware direct access to hardware at no cost, but it holds dozens of **undefined behaviour (UB)** traps. Trigger one, such as a signed overflow or a strict-aliasing violation, and the optimiser may silently delete your safety checks. **MISRA C**, from the motor industry, and NASA JPL's **Power of 10** restrict C to a safe subset, checked on every commit.

## 1. Six classic traps {.wide}

```cards cols=3 style=top
No volatile | Without `volatile`, the compiler keeps a status register or interrupt flag in a CPU register, and the loop never sees it change | red
Integer promotion | `uint8_t` and `uint16_t` become signed `int` before arithmetic. `1 << 31` on a 32-bit `int` is UB: write `1UL << 31U` | amber
Heap | `malloc()` and `free()` fragment a small SRAM until, weeks into the field, an allocation returns NULL | red
Unbounded waits | `while (!(SPI1->SR & RXNE));` hangs for ever when a sensor wire breaks | amber
Type punning | `*(uint32_t *)&f` breaks strict aliasing and miscompiles at -O2. Use `memcpy(&u, &f, sizeof u)` | blue
Torn reads | Reading a 64-bit timestamp shared with an interrupt, without a critical section, can return half old and half new bytes | navy
```

## 2. A wait, made safe {.wide}

```code-compare
@bad Hangs, and has undefined behaviour
uint32_t status_flags;               <1>
void wait_ready(int bit) {
  while (!(REG_STATUS & (1 << bit))) { }   <2>
}
@good Bounded, unsigned and checked
volatile uint32_t g_status_flags;
err_t wait_ready(uint8_t bit, uint32_t max_polls) {
  if (bit >= 32U) { return ERR_INVALID_ARG; }
  uint32_t mask = 1UL << bit;
  while (((REG_STATUS & mask) == 0U) && (max_polls > 0U)) {
    max_polls--;
  }
  return (max_polls > 0U) ? ERR_OK : ERR_TIMEOUT;   <3>
}
-- 1 | Shared with an interrupt, but not volatile
-- 2 | Never returns if the sensor is unplugged, and 1 << 31 overflows a signed int
-- 3 | A fixed upper bound, and every outcome returned to the caller
```

## 3. Six rules that give most of the benefit {.wide}

```compare
| The habit | The defensive rule (MISRA C, Power of 10)
Memory | `malloc()` and `free()` as needed | **No dynamic allocation after start-up**: static pools and ring buffers
Loops | `while (condition)` until done | **Every loop has a fixed upper bound** that a tool can prove
Functions | Recursion, `goto`, 500-line functions | **No recursion**, so stack depth is bounded, and functions under 60 lines
Types | `int`, `long`, silent sign conversion | `<stdint.h>` exact-width types, and unsigned literals such as `0x10U`
Errors | Return codes ignored | **Check every return value**; check pointers and ranges on entry
Macros | `#define MAX(a, b)` with side effects | `static inline` functions, `enum` and `const`
```

## 4. Three gates in CI

```flow
[Commit|navy] -> [Strict compiler: -Wall -Wextra -Werror -Wconversion|blue] -> [Static analysis: clang-tidy, Cppcheck, MISRA checker|purple] -> [Host tests with ASan and UBSan|green]
```

Hardware-free modules compiled on a PC with sanitizers fail at the first bad access:

```terminal title="Host unit tests"
$ cc -g -fsanitize=address,undefined ring.c test_ring.c -o test_ring
$ ./test_ring
ring.c:42:17: runtime error: left shift of 1 by 31 places cannot be represented in type 'int'
-- UBSan names the file, line and the exact undefined operation
```

## 5. Check it when it compiles

```c
#include <assert.h>

/* C11: zero cost at run time */
static_assert(sizeof(packet_header_t) == 12U, "Padding broke the header");
static_assert((RING_SIZE & (RING_SIZE - 1U)) == 0U, "Ring size must be a power of 2");
```

`-fstack-usage` writes a `.su` file for each source file, so CI can fail any function whose frame is too big.

## 6. Code review checklist {style=card colour=red}

```checklist
[x] Build with `-Wall -Wextra -Werror -Wconversion -Wsign-conversion -Wshadow -Wstrict-prototypes`
[x] No `malloc`, `free`, `strcpy`, `sprintf` or `atoi`: use `snprintf` and `strtol`
[x] No recursion, and the worst-case stack depth checked
[x] Every wait on hardware has a timeout and returns an error
[x] Data shared with interrupts uses `<stdatomic.h>` or a short critical section
```

## 7. Glossary

```glossary cols=1
ASan, UBSan | AddressSanitizer and UndefinedBehaviorSanitizer
ASIL, SIL | Safety levels of ISO 26262 and IEC 61508
JPL | NASA's Jet Propulsion Laboratory, home of the Power of 10
MISRA | Motor Industry Software Reliability Association
SAST | Static application security testing
UB | Undefined behaviour: anything may happen
```

## In short {.summary}

No heap after start-up and no recursion; a timeout on every wait; exact-width types with warnings as errors; and static analysis and sanitizers on every commit.

### If it can hang, it will

A wire will shake loose in the field. A bounded loop turns a lock-up into a logged error.

### Warnings are errors

`-Wconversion` and `-Wshadow` catch sign and shadowing bugs as you build.

### Sanitize on the host

Run hardware-free code on a PC with ASan and UBSan, and off-by-one errors show in milliseconds.
