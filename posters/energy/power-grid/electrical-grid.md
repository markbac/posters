---
title: "How the Electrical Power Grid Works"
subtitle: Balancing generation and demand, high-voltage transmission, the duck curve and 50 Hz stability
byline: Energy systems explainer
orientation: landscape
columns: 3
paper: a1
width: 1750
document_number: PO-032
colours:
  accent: "#d97706"
  secondary: "#b45309"
footer:
  left: The Electrical Grid
  centre: Energy Systems Reference
  qr: https://en.wikipedia.org/wiki/Electrical_grid
  qr-label: The electrical grid
---

## Key figures {.stats style=tiles}

| Value | Label |
|---|---|
| 50.00 Hz | The grid's frequency in Europe; 60 Hz in the Americas |
| 400 kV | A typical transmission line |
| 0 s | Of storage in a wire: supply must match demand every instant |
| 5 to 8 % | Of power lost as heat on the way |

## Introduction {.abstract}

The grid is the largest machine ever built. Its wires store no energy, so power stations hundreds of kilometres away must make exactly what millions of kettles, heat pumps and motors draw, at every moment. Every spinning turbine on a synchronous grid turns in step at **50 cycles a second**. Transformers, frequency and storage are how it stays in balance.

## 1. From turbine to socket {.wide}

```flow
[Generator, 11 to 25 kV|navy] -step up-> [Transmission, 275 or 400 kV|red] -step down-> [Substations, 132, 33, 11 kV|amber] -street transformer-> [Homes, 400 V three-phase, 230 V|green]
```

```equation
title: Why transmit at high voltage
P = V I \qquad P_{\text{loss}} = I^2 R
P | Power delivered | W
I | Current in the line | A
R | Resistance of the line | Ω
```

Raise the voltage 20 times, from 20 kV to 400 kV, and the current for the same power falls 20 times. So the heat lost in the wires falls **400 times**.

## 2. The frequency envelope (Great Britain) {.wide}

```threshold title="What happens as the frequency moves" target="50.00 Hz" width=2400
span: Below 48.8 Hz | Emergency | Demand switched off in blocks | red | 2
pin: 48.8 Hz Low-frequency demand disconnection | red
span: 48.8 to 49.5 Hz | Outside statutory limits | Reserves and fast response | amber | 2
pin: 49.5 Hz Statutory limit | amber
span: 49.5 to 49.8 Hz | Containment | Batteries respond in under a second | amber | 2
pin: 49.8 Hz | green
span: 49.8 to 50.2 Hz | Normal | The operational band | green | 4
pin: 50.2 Hz | green
span: 50.2 to 50.5 Hz | High | Generation reduced | amber | 2
pin: 50.5 Hz Statutory limit | amber
```

## 3. Frequency: the grid's pulse {cols=4}

Every turbine and every load is coupled. When demand exceeds generation, the missing energy comes out of the **spinning inertia** of every rotor on the grid, and they all slow: the frequency falls. When generation exceeds demand, it rises.

```balance unit=" GW"
left: Generation | 41.8 | green
right: Demand | 41.5 | red
right: Losses | 0.6 | grey
```

## 4. The duck curve

Solar peaks at midday, when demand is moderate, and fades at sunset just as people get home to cook, heat and charge cars. Demand minus solar, the **net load**, has the shape of a duck.

```chart type=line title="A spring day" unit=" GW" min=0 max=45 step=5 height=180 colours=blue,amber,green values=last
series: Demand, Solar, Net load
04:00 | 24 | 0 | 24
08:00 | 32 | 3 | 29
13:00 | 33 | 18 | 15
16:00 | 35 | 8 | 27
19:00 | 42 | 0 | 42
23:00 | 27 | 0 | 27
```

> [!WARNING]
> From 13:00 to 19:00 the net load climbs **27 GW**: about 25 nuclear reactors' worth, in six hours.

## 5. Three-phase AC

Three voltages 120° apart give motors a smooth, constant torque, and, when balanced, need no return current.

```plot type=function from=0 to=0.04 samples=300 width=380 height=170 xtitle="Time (s)" ytitle="Volts"
curve: L1 | 325 * sin(2 * PI * 50 * x)
curve: L2 | 325 * sin(2 * PI * 50 * x - 2 * PI / 3)
curve: L3 | 325 * sin(2 * PI * 50 * x + 2 * PI / 3)
```

## 6. AC and HVDC {style=card colour=amber}

```cards cols=1 style=label
Why undersea links are DC | Beyond about 60 km under water, an AC cable's insulation acts as a huge capacitor, charged and discharged 50 times a second, and its capacity is used up by that current. HVDC avoids it, and joins grids that are not in step, such as Britain and the continent
Active and reactive power | Motors and transformers slosh magnetic energy back and forth: **reactive power**. It heats wires without doing work, and lowers the **power factor**
```

## 7. Sources and storage {.wide}

```compare
| Nuclear and hydro | Wind and solar | Gas (CCGT, OCGT) | Batteries and pumped hydro
Direct CO₂ | **None** | **None** | 350 to 500 g/kWh | None: they store other power
Dispatch | Steady (hydro ramps fast) | **Weather-dependent** | **On demand** | **Instant**: under 100 ms for batteries
Inertia | **High**: heavy rotors | **None**: inverters | **High** | **Synthetic**, from grid-forming inverters
Start-up | Hours to days for nuclear; seconds for hydro | With the sun and wind | 10 to 45 minutes | Milliseconds to 20 seconds
```

## 8. Black start {.wide}

Most power stations need power from the grid to run their own pumps and magnets. If a whole country goes dark:

```steps cols=4
Split into islands | Breakers divide the dead network into small regions
Start a black-start unit | A hydro dam opens its gates, or a diesel cranks a gas turbine, to make the first 50 Hz | green
Energise a spine | One line at a time, to the next large station, matching voltage, frequency and phase | amber
Reconnect load in blocks | Hospitals and towns, 10 to 50 MW at a time, so the surge never stalls a turbine | blue
```

## 9. Glossary {.wide}

```glossary cols=4
BESS | Battery energy storage system
CCGT | Combined-cycle gas turbine
GW, MW, kV | Gigawatt, megawatt, kilovolt
HVDC | High-voltage direct current
kWh | Energy: a 2 kW kettle for 30 minutes uses 1 kWh
kVAR | Reactive power
PMU | Phasor measurement unit: GPS-timed grid sensor
PV | Solar photovoltaics
```

## In short {.summary}

The grid balances supply and demand across a continent, every instant. Transformers keep losses small, the frequency shows the balance, and storage carries midday sun into the evening.

### High voltage saves heat

Twenty times the voltage means a four-hundredth of the heat lost in the wires.

### Frequency is the pulse

Grid batteries watch the frequency to a thousandth of a hertz and respond in milliseconds.

### Storage flattens the duck

Batteries and pumped hydro turn midday sunshine into firm evening power.
