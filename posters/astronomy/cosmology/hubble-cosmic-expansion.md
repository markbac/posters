---
title: "Hubble, Cepheid Variables and the Expanding Universe"
subtitle: How Henrietta Leavitt and Edwin Hubble measured the cosmos, and why the expansion rate is still in dispute
byline: Popular astrophysics explainer
orientation: landscape
columns: 3
paper: a1
width: 1750
document_number: PO-043
colours:
  accent: "#1d4ed8"
  secondary: "#1e3a8a"
footer:
  left: Hubble and the Expanding Universe
  centre: Popular Astrophysics Reference
  qr: https://en.wikipedia.org/wiki/Hubble%27s_law
  qr-label: The Hubble-Lemaître law
---

## Key figures {.stats style=tiles}

| Value | Label |
|---|---|
| 1924 | Hubble shows Andromeda is a galaxy far outside our own |
| 70 km/s/Mpc | About how fast space grows, per megaparsec of distance |
| 67.4 or 73.0 | The two measured expansion rates that disagree: the Hubble tension |
| 14 billion light-years | The Hubble sphere, where space recedes at the speed of light |

## Introduction {.abstract}

Until the 1920s, many astronomers thought the Milky Way was the whole universe, and the spiral "nebulae" clouds inside it. With **Henrietta Leavitt's** law for Cepheid stars and the 100-inch telescope at Mount Wilson, **Edwin Hubble** showed that Andromeda is a galaxy of its own. Five years later, with **Vesto Slipher's** redshifts and **Georges Lemaître's** theory, he showed that galaxies recede in proportion to their distance: **space is expanding**.

## 1. How the universe got bigger {.wide}

```timeline
1912 | Leavitt's law | Cepheids in the Small Magellanic Cloud: the longer the period, the brighter | teal
1917 | Slipher's redshifts | Almost every spiral nebula is receding | blue
1920 | The Great Debate | Shapley and Curtis argue: are the spirals galaxies? | grey
1923 | Hubble's "VAR!" | A Cepheid in Andromeda puts it at 900,000 ly (2.5 million, today) | navy
1927 | Lemaître | Expanding space, from general relativity, and a first expansion rate | purple
1929 | Hubble's law | Speed against distance: a straight line | navy
1998 | Acceleration | Distant supernovae are too faint: dark energy | red
2022 | JWST | Confirms Hubble's Cepheids: the tension is real | amber
```

## 2. Standard candles: Leavitt's law

A star that looks faint may be small and near, or bright and far. Cepheids pulse with a period of 1 to 100 days, and **the period gives their true brightness**. Compare that with how bright they look, and the distance follows.

```equation
title: Leavitt's law
M_V \approx -2.43 \left( \log_{10} P - 1 \right) - 4.05
M_V | Absolute magnitude: the true brightness |
P | Period of the pulse | days
---
title: Distance from brightness
d = 10^{(m - M + 5)/5}
d | Distance | parsecs
m | Apparent magnitude: how bright it looks |
M | Absolute magnitude |
```

## 3. Space stretches, galaxies stay put

```cards cols=1 style=top
Faster than light, legally | Nothing may move **through** space faster than light. But nothing limits how fast space **itself** stretches. Beyond the Hubble sphere, about 14 billion light-years away, galaxies recede faster than light | blue
Why Andromeda comes closer | In groups of galaxies, and in stars and atoms, gravity and electric forces win easily. Andromeda approaches at 110 km/s, and is blueshifted | teal
```

## 4. The Hubble-Lemaître law

```equation
v = H_0 \, d
v | Speed of recession | km/s
H_0 | The Hubble constant | km/s/Mpc
d | Distance | Mpc
```

```chart type=line title="Recession speed against distance" unit=" km/s" min=0 max=30000 step=10000 height=200 colours=blue,red values=last axis="km/s"
series: Planck (67.4), SH0ES (73.0)
0 Mpc | 0 | 0
100 Mpc | 6740 | 7300
200 Mpc | 13480 | 14600
300 Mpc | 20220 | 21900
400 Mpc | 26960 | 29200
```

Hubble's own value was about 500 km/s/Mpc, seven times too high: he did not know there are two kinds of Cepheid. Walter Baade found them in 1952, and the universe doubled in size.

## 5. Hubble and Webb, a team {style=card colour=blue}

```sizes shape=hexagon unit=" m"
Webb (JWST) | 6.5 | Gold mirror, 18 segments, at L2 | amber
Hubble (HST) | 2.4 | One mirror, in orbit at 540 km | blue
```

```checklist
[x] **Hubble** sees ultraviolet, visible and near-infrared, 0.1 to 1.7 µm, and has done since 1990
[x] **Webb** is cooled to 40 K behind its sunshield to see infrared, 0.6 to 28 µm
[x] **Redshift moves light into the infrared**: the visible light of galaxies at z > 10 arrives at 2 to 5 µm, where only Webb sees it
```

## 6. The Hubble tension {.wide}

Today $H_0$ is measured to about 1 %, yet the two best methods differ by more than **five standard deviations**:

```compare
| From the early universe | From the distance ladder | Tie-breakers
Value | **67.4 ± 0.5 km/s/Mpc** | **73.0 ± 1.0 km/s/Mpc** | 70 to 73, so far
How | The sound-wave scale frozen into the CMB, carried forward to today with ΛCDM | Parallax, then Cepheids, then Type Ia supernovae in galaxies near and far | Methods that skip the Cepheids altogether
Instruments | Planck, ACT and SPT | Hubble, Webb and Gaia (the SH0ES team) | The tip of the red giant branch, gravitational-wave "standard sirens", lensed quasars
Age it implies | **13.8 billion years** | About 12.7 billion years, unless ΛCDM changes | Not settled
```

```gradient-scale from=64 to=76 unit=" km/s/Mpc" colours=blue,green,amber,red step=2 width=2400
67.4 | Planck
69.8 | Red giant branch tip
73.0 | SH0ES
```

## 7. Glossary {.wide}

```glossary cols=4
BAO | Baryon acoustic oscillations, a standard ruler
Cepheid | A pulsing supergiant star, a standard candle
CMB | Cosmic microwave background
H₀ | The Hubble constant
Mpc | Megaparsec: 3.26 million light-years
SH0ES | The team measuring H₀ with Cepheids and supernovae
Standard siren | A merger whose gravitational waves give its distance
TRGB | Tip of the red giant branch, another standard candle
```

## In short {.summary}

Henrietta Leavitt gave astronomy a yardstick, and Hubble and Lemaître used it to show that the universe is expanding. A five-sigma gap between two measurements of that expansion may point to new physics.

### Space stretches between galaxies

Redshift is not galaxies flying apart: it is space growing while the light is on its way.

### Brooklyn is not expanding

Expansion wins only across the near-empty space between clusters. Inside them, gravity holds.

### The gap is real

Webb's sharp infrared images show that crowding did not distort Hubble's Cepheids.
