---
title: "Solar Physics, Space Weather and Earth's Magnetosphere"
subtitle: The solar dynamo, flares and coronal mass ejections, aurora physics, and protecting the grid
byline: Planetary science explainer
orientation: landscape
columns: 4
paper: a1
width: 1750
document_number: PO-042
colours:
  accent: "#ea580c"
  secondary: "#9a3412"
footer:
  left: Space Weather
  centre: Planetary Science Reference
  qr: https://www.swpc.noaa.gov/
  qr-label: NOAA Space Weather Prediction Center
---

## Key figures {.stats style=tiles}

| Value | Label |
|---|---|
| 11 years | The sunspot cycle; the magnetic field flips every cycle |
| 400 to 800 km/s | Speed of the solar wind past Earth |
| 8.3 minutes | For a flare's X-rays to reach Earth; a CME takes 15 to 72 hours |
| 1859 | The Carrington Event, the benchmark superstorm |

## Introduction {.abstract}

The Sun is a ball of magnetised **plasma** whose equator turns in 25 days and its poles in 35. This **differential rotation** winds its magnetic field up like rubber bands until loops burst through the surface, as **sunspots**, **flares** and **coronal mass ejections (CMEs)** of billions of tonnes. Earth's magnetic field, from its liquid iron core, shields our air, satellites and power grids.

## 1. Flares, CMEs and particle storms {.wide}

A **flare** is the muzzle flash, light at 300,000 km/s. A **CME** is the cannonball: magnetised plasma that arrives days later.

```compare
| Solar flare | Coronal mass ejection (CME) | Solar energetic particles (SEP)
What leaves the Sun | A flash of **X-rays and extreme ultraviolet** | **1 to 10 billion tonnes** of plasma, with its own magnetic field | **Protons and ions** at 10 to 80 % of light speed
Time to Earth | **8 minutes 20 seconds** | **15 to 72 hours**, at 500 to 3,000 km/s | **20 minutes to hours**
Scale | **A, B, C, M, X**, each ten times the last | Speed, width (a **halo CME** comes at us) and the tilt of its field, **Bz** | NOAA **S1 to S5**
What it does | Ionises the day-side upper air: **HF radio blackouts** (R1 to R5) | If its field points **south**, a **geomagnetic storm** (G1 to G5) and aurorae | Flips bits in satellite memory, wears solar panels, endangers astronauts
```

## 2. Inside the Sun

```cutaway type=sphere unit=" R☉"
Core | 0.25 | 15 million K, fusion | red
Radiative zone | 0.7 | Light random-walks for about 100,000 years | amber
Convective zone | 1 | Boiling cells; the dynamo at its base | brown
```

The surface, the **photosphere**, is 5,778 K. Yet the thin **corona** above it is 1 to 3 million K. Magnetic waves and countless tiny **nanoflares** carry the heat up, and drive the solar wind.

## 3. Flare classes

```logscale unit=" W/m²"
1e-8 | A | green
1e-6 | C | blue
1e-5 | M | amber
1e-4 | X | red
2.8e-3 | X28+, 4 Nov 2003 | purple
```

X-ray power at Earth, 0.1 to 0.8 nm. Each letter is ten times the one before.

## 4. Why the field direction, Bz, decides

Earth's field stands off the solar wind about 60,000 km out, at the **magnetopause**.

```flow
[CME or fast wind|amber] -field points north (+Bz)-> [Glances off|green]
[CME or fast wind|amber] -field points south (−Bz)-> [Fields reconnect|red] -energy stored in the tail-> [Tail snaps back|purple] -electrons down the field lines-> [Aurora|green]
```

Two identical CMEs can hit Earth: one does nothing, the other lights the sky to the tropics. The difference is **Bz**.

## 5. The colours of an aurora

Electrons from the magnetotail hit the upper air, and excited atoms give out light at exact wavelengths:

```spectrum mode=emission
427.8 | N₂⁺ violet
557.7 | O green
630 | O red
```

```cutaway type=column unit=" km"
0 | 12 | Troposphere | Airliners fly here | grey
80 | 100 | Blue and pink fringe | Nitrogen, in strong storms | purple
100 | 200 | Green | Oxygen, 557.7 nm: the commonest | green
200 | 400 | Red crown | Oxygen, 630 nm: needs 110 s undisturbed | red
```

## 6. Protecting what we built {.wide}

```steps cols=4
Warning from L1 | DSCOVR and ACE, 1.5 million km sunward, measure a CME's speed and Bz 15 to 60 minutes before it arrives | green
Satellite drag | A storm heats and swells the thermosphere. In February 2022, 38 new Starlink satellites fell back after a minor storm | amber
Currents in the grid | A changing field drives slow, near-DC currents into long power lines. They saturate transformer cores: Quebec's grid failed in 90 seconds in 1989 | red
Hardening | Operators block neutral currents and hold reserves in G4 and G5 alerts. Spacecraft use error-correcting memory and safe modes | blue
```

> [!NOTE]
> In May 2024 the first G5 storm since 2003 brought aurorae to southern Europe and Mexico. Grids held, with warnings.

## 7. Glossary {.wide}

```glossary cols=4
Bz | The north-south part of the solar wind's magnetic field
CME | Coronal mass ejection
GIC | Geomagnetically induced current
IMF | Interplanetary magnetic field
Kp | A 0 to 9 index of geomagnetic activity; 7 or more brings aurorae to mid-latitudes
L1 | The Lagrange point 1.5 million km towards the Sun
SEP | Solar energetic particles
SEU | Single-event upset: a bit flipped by a particle
```

## In short {.summary}

The Sun's twisted magnetic field drives an 11-year cycle of flares and CMEs. Earth's magnetosphere turns their energy into aurorae, and spacecraft at L1 warn the grid of the storms that matter.

### Light in minutes, plasma in days

A flare blacks out HF radio in 8 minutes. The CME behind it takes one to three days.

### South is the key

A CME glances off unless its field points south and links with Earth's.

### Long wires are antennas

In a G5 storm, power lines across a continent become loops that the changing field drives current through.
