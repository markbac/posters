---
title: "Globular Clusters and Dating the Oldest Stars"
subtitle: Turnoff clocks, stellar populations, blue stragglers and the galaxy's oldest fossils
byline: Popular astrophysics explainer
orientation: landscape
columns: 3
paper: a1
width: 1750
document_number: PO-044
colours:
  accent: "#b45309"
  secondary: "#78350f"
footer:
  left: Globular Clusters
  centre: Popular Astrophysics Reference
  qr: https://en.wikipedia.org/wiki/Globular_cluster
  qr-label: Globular clusters on Wikipedia
---

## Key figures {.stats style=tiles}

| Value | Label |
|---|---|
| 12 to 13.5 billion years | Age of the Milky Way's globular clusters |
| 10 million stars | In Omega Centauri, the largest, in a ball 150 light-years across |
| Up to a million × | Denser in stars, at a cluster's core, than the Sun's neighbourhood |
| 0.8 Suns | The heaviest stars still burning hydrogen in an old globular |

## Introduction {.abstract}

About **150 globular clusters** orbit in the Milky Way's halo, each a ball of 100,000 to 10 million ancient stars 50 to 150 light-years across. All the stars of a cluster formed at about the **same time**, from the same gas, 12 to 13.5 billion years ago. That makes globulars nature's best **clocks**, and sets a lower limit on the age of the universe.

## 1. The turnoff: a cluster's hourglass {.wide}

A lone star tells little of its age: it spends 90 % of its life on the main sequence, little changed. But in a cluster, stars of **every mass** were born together, and heavy stars use up their fuel first. Plot every star's colour against its brightness, and the point where stars **turn off** the main sequence gives the age.

```plot type=scatter xlog=yes ylog=yes xinvert=yes width=640 height=300 xtitle="Surface temperature (K)" ytitle="Brightness (Suns)"
Star 4 | 3500 | 0.03 | 2 | Main sequence
Star 5 | 4200 | 0.1 | 2 | Main sequence
Star 6 | 5000 | 0.35 | 2 | Main sequence
Star 7 | 5800 | 0.9 | 2 | Main sequence
Turnoff | 6200 | 1.6 | 6 | Turnoff
Star 8 | 5700 | 2.6 | 2 | Subgiants and giants
Star 9 | 5100 | 6 | 2 | Subgiants and giants
Star 10 | 4700 | 30 | 2 | Subgiants and giants
Star 11 | 4400 | 150 | 2 | Subgiants and giants
Star 12 | 4100 | 1000 | 2 | Subgiants and giants
Star 13 | 6500 | 45 | 2 | Horizontal branch
Star 14 | 8000 | 40 | 2 | Horizontal branch
Star 15 | 11000 | 30 | 2 | Horizontal branch
Star 16 | 7200 | 4 | 3 | Blue stragglers
Star 17 | 7800 | 7 | 3 | Blue stragglers
Star 18 | 12000 | 0.003 | 2 | White dwarfs
Star 19 | 8000 | 0.0008 | 2 | White dwarfs
```

[[CAPTION:Figure]] The colour-magnitude diagram of an old globular, sketched. The turnoff sits at stars of about 0.8 solar masses.


## 2. Lifetimes, by mass

```logscale unit=" years"
3e7 | 10 Suns: a blue giant | blue
1.8e9 | 2 Suns: Sirius A | teal
1e10 | The Sun | amber
1.7e10 | 0.8 Suns: an old turnoff | red
3.6e10 | 0.6 Suns: an orange dwarf | brown
```

A star lasts about 10¹⁰ years × (M/M☉)⁻²·⁵. The universe is 13.8 billion years old, so every star below about 0.8 Suns ever made is still shining.

## 3. Three populations of stars

Astronomers call every element heavier than helium a **metal**, and measure it as [Fe/H]: 0 is the Sun, −2 is a hundredth of its iron.

```segments
title: Population number goes up as age goes down
2 | Population III: no metals at all; 100 to 300 Suns; none seen yet | The first, 13.6 billion years ago | purple
4 | Population II: [Fe/H] of −1 to −7, in globulars and the halo | 12 to 13.5 billion years | amber
4 | Population I: [Fe/H] near 0, in the disk; the Sun | Up to 10 billion years | green
```

Pure hydrogen and helium cannot cool well enough to break into small stars, so the first stars were giants that lived only a few million years. Their supernovae made the metals of Population II.

## 4. Globular and open clusters {.wide}

```compare
| Globular clusters | Open clusters | Nuclear clusters
Where | In the **halo**, far above and below the disk | In the **spiral arms** of the disk | At the very centre of a galaxy
Stars | **100,000 to 10 million** | **100 to 5,000**, loosely held; they disperse in under 500 million years | **10 to 100 million**, round a black hole
Age | **11.5 to 13.5 billion years** | **1 million to 2 billion years** | Several generations
Metals | **Poor**: 0.1 to 5 % of the Sun's iron | **Rich**: 50 to 200 % of the Sun's | Mixed, from mergers
Examples | **Omega Centauri**, **M13**, **47 Tucanae** | **The Pleiades**, the Hyades, the Jewel Box | Omega Centauri may be one: the core of a dwarf galaxy the Milky Way swallowed
```

## 5. Three independent clocks

```cards cols=1 style=top
White dwarf cooling | A white dwarf has no fuel left and cools like a poker from the fire. The faintest in M4, found by Hubble, have been cooling about **12 billion years** | blue
Radioactive decay | As geologists date rocks, astronomers compare thorium-232 (half-life 14 billion years) and uranium-238 (4.5 billion) with stable europium in very metal-poor stars: **12.5 to 14 billion years**, give or take 2 or more | amber
The Methuselah star | HD 140283, 200 light-years away, once seemed 14.5 billion years old: older than the universe. Better distances from Gaia and better models bring it to **12 to 13.5 billion** | green
```

## 6. Strange things in crowded cores {style=card colour=amber}

```cards cols=1 style=label
Blue stragglers | Stars above the turnoff that look too young: two old stars merged, or one stripped its partner's hydrogen
Millisecond pulsars | Old neutron stars capture new partners and are spun up to hundreds of turns a second. 47 Tucanae has over 40
No dark matter | Unlike dwarf galaxies, globulars hold no dark matter halo
```

## 7. Glossary {.wide}

```glossary cols=4
CMD | Colour-magnitude diagram, the observer's H-R diagram
[Fe/H] | Iron to hydrogen, on a log scale relative to the Sun
HB | Horizontal branch: old stars burning helium in their cores
MSTO | Main-sequence turnoff
ω Cen | Omega Centauri, the largest Milky Way globular
Pop I, II, III | Stellar populations: young and rich in metals, old and poor, the first
RGB | Red giant branch
RR Lyrae | Pulsing horizontal-branch stars, a standard candle
```

## In short {.summary}

Globular clusters are 13-billion-year-old fossils in our galaxy's halo. The turnoff, white dwarf cooling and radioactive decay all agree: the oldest stars formed a few hundred million years after the Big Bang.

### No dark nights

At the centre of Omega Centauri or 47 Tucanae, stars are light-weeks apart: thousands would outshine Venus.

### Metal-poor means old

Heavy elements are only made in stars, so a star with almost no iron formed before many generations of supernovae.

### Stars agree with the universe

Before dark energy, the universe seemed younger than its oldest stars. Dark energy made it 13.8 billion years old, and the conflict went away.
