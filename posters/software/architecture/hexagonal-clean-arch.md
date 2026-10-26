---
title: "Hexagonal, Clean and Layered Architecture"
subtitle: Keeping domain and control logic free of drivers, databases and transports
byline: Software architecture
orientation: landscape
columns: 3
paper: a1
width: 1750
document_number: PO-028
colours:
  accent: "#1e3a8a"
  secondary: "#1e40af"
footer:
  left: Hexagonal and Clean Architecture
  centre: Software Architecture Reference
  qr: https://alistair.cockburn.us/hexagonal-architecture/
  qr-label: Alistair Cockburn on ports and adapters
---

## Key figures {.stats style=tiles}

| Value | Label |
|---|---|
| 1 rule | Source dependencies point inward, towards the domain |
| 0 | Vendor SDK, database or web imports in the domain |
| 2 sides | Driving adapters call in; driven adapters are called out to |
| 1 adapter | Is all that changes when a chip or database does |

## Introduction {.abstract}

In a traditional layered code base, control logic calls vendor SPI registers, SQL or an MQTT library directly. When a chip goes out of stock or a protocol changes, the application is rewritten. **Hexagonal architecture** (ports and adapters) and **clean architecture** apply the **dependency inversion principle**. The domain sits at the centre and defines **ports**, and hardware and network **adapters** plug into them from outside.

## 1. The rings

```target
Domain | Entities and rules: maths, state, invariants | green
Use cases | What the system does; defines the ports | teal
Adapters | Controllers, gateways, codecs | blue
Frameworks and drivers | HAL, RTOS, SQL, web | amber
```

Every ring may depend only on the rings inside it.

## 2. Ports and adapters

```flow
[Driving adapter: timer IRQ, CLI, CoAP, test|navy] -calls inbound port-> [Domain and use cases|green] -outbound port-> [Driven adapter: STM32 I2C, flash, fake|blue]
The driven adapter implements a port that the domain defines, so the driver depends on the domain, not the other way round.
```

```cards cols=1 style=top
Inbound ports | How the world asks for work, such as `record_sample()`. Called by driving adapters: an interrupt, a CLI, an MQTT subscriber, a unit test | navy
Outbound ports | What the core needs, in its own words: `PressureSensorPort`, `TelemetryStorePort`, `ClockPort`. Implemented by driven adapters: a driver, a flash log, a fake | blue
```

## 3. A functional core

Write control laws, parsers and rules as pure, deterministic functions, and push every side effect to the shell of adapters. Pure code needs no mocks to test.

## 4. The same rule, coupled and ported {.wide}

No object orientation needed: in C a port is a struct of function pointers, or a header linked to different files.

```code-compare
@bad Coupled: the rule includes the driver
#include "stm32f4xx_hal.h"                         <1>
action_t valve_step(float limit_kpa) {
    float kpa = bme280_read_kpa(&hi2c1);           <2>
    return kpa > limit_kpa ? OPEN_VALVE : HOLD;
}
@good Ported: the rule knows only its port
typedef struct {
    err_t (*read_kpa)(void *ctx, float *kpa);
} pressure_port_t;

action_t valve_step(const pressure_port_t *p, void *ctx, float limit_kpa) {
    float kpa;
    if (p->read_kpa(ctx, &kpa) != ERR_OK) return TRIP_SAFE_OPEN;   <3>
    return kpa > limit_kpa ? OPEN_VALVE : HOLD;
}
-- 1 | The safety rule cannot compile on a PC, or on another chip
-- 2 | And a bus error is invisible
-- 3 | A test passes a fake port; production passes the BME280 adapter. The rule does not change
```

## 5. Three styles compared {.wide}

```compare
| Layered (app, logic, HAL) | Hexagonal (ports and adapters) | Clean, or onion
Dependencies | Downward: the domain depends on the HAL | **Inward**: adapters depend on the domain's ports | **Strictly inward**, ring by ring
New chip or database | Changes ripple up if types leak | **One new adapter** | **One new adapter** in the outer ring
Testing off target | Hard, without link-time tricks | **Natural**: a fake adapter | **Natural**: the core has no dependencies
Over-engineering | Little | Some, if trivial code is wrapped | Real, if every struct gets four mappers
Suits | Small, short-lived code | **Long-lived firmware, gateways, services** | **Large and safety-critical systems**
```

## 6. Enforcement checklist {cols=2 style=card colour=blue}

```checklist
[x] Domain code in its own directory whose build cannot link vendor SDKs
[x] Ports named in domain words, `read_temperature`, never in hardware words
[x] Wire formats (Protobuf, JSON, Modbus frames) kept in adapters and converted at the edge
[x] All adapters wired to ports in one place, `main.c`: the composition root
[x] A CI check that fails if the domain includes an adapter header
```

## 7. Glossary

```glossary cols=1
BSP | Board support package
Composition root | The one place that wires adapters to ports
DIP | Dependency inversion principle
DTO | Data transfer object: a wire format, kept at the edge
HAL | Hardware abstraction layer
Port | An interface the core defines
```

## In short {.summary}

Keep the domain pure. Define narrow ports in its own words, put hardware and network details in adapters, and wire them together only in `main()`.

### Name ports after intent

A `BatteryGaugePort` survives a move from an I2C fuel gauge to an ADC divider.

### Enforce it in the build

If the domain cannot see the SDK's include path, no deadline can couple them.

### Fakes are adapters too

A test is just another driving adapter, with fake driven ones.
