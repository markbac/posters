---
title: "Cosmology and the Expanding Universe"
subtitle: From inflation and the first light to dark matter, dark energy and the Hubble tension
byline: Popular astrophysics explainer
orientation: landscape
columns: 3
paper: a1
width: 1750
document_number: PO-040
colours:
  accent: "#0284c7"
  secondary: "#0369a1"
footer:
  left: Cosmology and the Big Bang
  centre: Popular Astrophysics Reference
  qr: https://en.wikipedia.org/wiki/Lambda-CDM_model
  qr-label: The ΛCDM model
---

## Key figures {.stats style=tiles}

| Value | Label |
|---|---|
| 13.8 billion years | Age of the universe, from the Planck satellite |
| 2.725 K | Temperature of the cosmic microwave background today |
| 95 % | Of the universe that is dark energy and dark matter |
| 93 billion light-years | Across the observable universe |

## Introduction {.abstract}

The Big Bang was not an explosion into empty space: it was the expansion of **space itself**, from a hot dense state 13.8 billion years ago. As space stretched, the plasma cooled. Protons formed, then the first nuclei, then atoms, and the light of that moment is still arriving as the **cosmic microwave background**. The **Lambda-Cold Dark Matter (ΛCDM)** model describes all of it with six numbers.

## 1. The history of the universe, on a log scale {.wide}

Each mark is ten times later than the one before it. Inflation grew space 10²⁶ times in a split second, and its quantum ripples became the seeds of galaxies. Protons formed at a microsecond, the first nuclei (75 % hydrogen, 25 % helium) by three minutes, and atoms at 380,000 years, which released the CMB. The first stars lit at about 200 million years, and dark energy took over at about 9.8 billion.

```logscale unit=" s" width=2400
1e-36 | Inflation | purple
1e-6 | Protons form | blue
180 | First nuclei | blue
1.2e13 | Atoms form: the CMB | amber
6e15 | First stars | amber
3e17 | Dark energy dominates | red
4.35e17 | Today | green
```

## 2. What the universe is made of

Every star, planet and person adds up to less than 5 % of it. Of the ordinary matter, most is thin gas between the galaxies: stars are one tenth of it.

```vega-lite
{
  "data": {"values": [{"part": "Dark energy, 68 %", "n": 68}, {"part": "Dark matter, 27 %", "n": 27}, {"part": "Ordinary matter, 5 %", "n": 5}]},
  "transform": [
    {"window": [{"op": "sum", "field": "n", "as": "end"}]},
    {"calculate": "datum.end - datum.n", "as": "start"},
    {"calculate": "sequence(datum.start, datum.end)", "as": "cell"},
    {"flatten": ["cell"]},
    {"calculate": "datum.cell % 10", "as": "col"},
    {"calculate": "floor(datum.cell / 10)", "as": "row"}
  ],
  "mark": {"type": "square", "size": 300},
  "width": 240, "height": 240,
  "encoding": {
    "x": {"field": "col", "type": "ordinal", "axis": null},
    "y": {"field": "row", "type": "ordinal", "axis": null, "sort": "descending"},
    "color": {"field": "part", "type": "nominal", "title": null, "legend": {"orient": "bottom", "direction": "vertical", "labelLimit": 400, "labelFontSize": 14}, "sort": ["Dark energy, 68 %", "Dark matter, 27 %", "Ordinary matter, 5 %"]}
  }
}
```

[[CAPTION:Figure]] The universe as 100 squares, from the Planck satellite and Type Ia supernovae.

## 3. Expansion and redshift

Galaxies recede with a speed in proportion to their distance, like raisins in rising dough: the dough is **space**, and every raisin moves away from every other.

```equation
title: The Hubble-Lemaître law, and redshift
v = H_0 \, d \qquad 1 + z = \frac{a_{\text{now}}}{a_{\text{then}}}
H_0 | The Hubble constant, the expansion rate today | km/s/Mpc
z | Redshift: how far the light's wavelength has stretched |
a | The scale factor: the size of space, relative to today |
```

Light is stretched with the space it crosses. The same lines of hydrogen and sodium, from a galaxy at z = 0.1:

```spectrum mode=absorption shift=0.1
656.3 | Hα
589 | Na D
486.1 | Hβ
434 | Hγ
```

The CMB left at 3,000 K, glowing near-infrared. Stretched by z ≈ 1,100, it now peaks at about 1 mm.

## 4. The Hubble tension

Two ways of measuring $H_0$ disagree, by more than their errors allow. The early universe (the CMB) gives a slower expansion than nearby stars and supernovae do. Either one method has a hidden error, or ΛCDM is missing new physics.

```gradient-scale from=64 to=76 unit=" km/s/Mpc" colours=blue,green,amber,red step=2
67.4 | Planck, from the CMB
69.8 | Tip of the red giant branch
73.0 | SH0ES, Cepheids and supernovae
```

## 5. The cosmic distance ladder

No tape reaches across space, so each rung calibrates the next:

```steps
Parallax | Gaia measures the yearly shift of nearby stars against distant ones: thousands of light-years | green
Cepheid variables | Henrietta Leavitt found that their period gives their true brightness: 100 million light-years | blue
Type Ia supernovae | Exploding white dwarfs near 1.4 solar masses all peak near the same brightness: billions of light-years | amber
Redshift | For the most distant galaxies, with ΛCDM: to z = 14 and beyond, seen by JWST | purple
```

## 6. The three ingredients {.wide}

```compare
| Ordinary matter (5 %) | Cold dark matter (27 %) | Dark energy (68 %)
What it is | Protons, neutrons and electrons: every element | Particles that neither emit nor absorb light | The energy of empty space itself, the cosmological constant Λ
How it acts | Every force: gravity, electromagnetism, the nuclear forces | **Gravity only**: it passes through rock and detectors | A smooth **negative pressure** that pushes space apart
The evidence | Stars, X-ray gas, the deuterium made in the first minutes | **Flat galaxy rotation curves**, gravitational lensing, the Bullet Cluster | **Distant Type Ia supernovae** are fainter than a coasting universe allows
What it does | Collapses into stars, planets and life | Built the cosmic web that gathered the galaxies | **Accelerates** the expansion, for the last 5 billion years
```

## 7. How we know the Big Bang happened {cols=2 style=card colour=blue}

```checklist
[x] **Expansion (1929)**: galaxies in every direction are redshifted in proportion to their distance
[x] **The CMB (1965)**: Penzias and Wilson found the 2.7 K afterglow that Alpher and Herman had predicted
[x] **The lightest elements**: the oldest gas is 75 % hydrogen and 25 % helium by mass, as three minutes of fusion predict, to about 1 % (lithium-7 is the known mismatch)
[x] **Baryon acoustic oscillations**: sound waves frozen in the CMB set a spacing of 490 million light-years between galaxies today
```

## 8. Glossary

```glossary cols=2
BAO | Baryon acoustic oscillations, a standard ruler
BBN | Big Bang nucleosynthesis, the first three minutes of fusion
CMB | Cosmic microwave background
H₀ | Hubble constant, the expansion rate today
Mpc | Megaparsec: 3.26 million light-years
ΛCDM | Lambda-Cold Dark Matter, the standard model of cosmology
JWST | James Webb Space Telescope
z | Redshift
```

## In short {.summary}

The universe began 13.8 billion years ago, hot and dense, and has been expanding and cooling ever since. Dark matter built its structure, atoms lit its stars, and dark energy now speeds its expansion.

### To look far is to look back

A galaxy 13 billion light-years away is seen as it was 800 million years after the Big Bang.

### Why 93 billion light-years

Space kept stretching while the oldest light travelled, so its sources are now 46 billion light-years away.

### Dark matter built our galaxy

Without its extra gravity, the thin, warm gas after the Big Bang could not have collapsed into galaxies.
