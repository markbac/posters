---
title: "The Interstellar Medium, Nebulae and Star Formation"
subtitle: The phases of galactic gas, the 21 cm line, Jeans collapse, nebulae and cosmic dust
byline: Popular astrophysics explainer
orientation: landscape
columns: 3
paper: a1
width: 1750
document_number: PO-045
colours:
  accent: "#7c3aed"
  secondary: "#5b21b6"
footer:
  left: The Interstellar Medium
  centre: Popular Astrophysics Reference
  qr: https://en.wikipedia.org/wiki/Interstellar_medium
  qr-label: The interstellar medium
---

## Key figures {.stats style=tiles}

| Value | Label |
|---|---|
| 1 atom/cm³ | Average density between the stars; air has 10¹⁹ |
| 10 K | Inside the dark clouds where stars form |
| 21.1 cm | The radio line of neutral hydrogen, at 1420.4 MHz |
| 1 % | Of interstellar matter that is dust, which absorbs about a third of starlight |

## Introduction {.abstract}

Space between the stars is not empty. About 10 to 15 % of the visible mass of the Milky Way's disk is the **interstellar medium (ISM)**: 99 % gas, mostly hydrogen and helium, and 1 % dust. Supernovae blast it into million-degree bubbles; elsewhere it cools into **10 K molecular clouds**. Gravity crushes the densest cores into new stars, and dying stars return enriched gas.

## 1. Five phases in balance {.wide}

How can 10 K clouds sit beside million-degree gas? Their **pressures** are similar, P = n k T: where the gas is a hundred thousand times colder, it is a hundred thousand times denser.

```plot type=scatter xlog=yes ylog=yes labels=yes width=520 height=320 xtitle="Density (particles per cm³)" ytitle="Temperature (K)"
Molecular clouds | 1000 | 15 | 8 | Cold
Cold neutral | 30 | 80 | 6 | Cold
Warm neutral | 0.3 | 8000 | 6 | Warm
H II regions | 100 | 10000 | 4 | Warm
Hot ionised | 0.003 | 1000000 | 7 | Hot
```

```compare
| Molecular clouds | Cold neutral | Warm neutral and ionised | H II regions | Hot ionised
Temperature | **10 to 20 K** | 50 to 100 K | 6,000 to 10,000 K | About 10,000 K | **1 to 10 million K**
Density, per cm³ | **100 to a million** | 20 to 50 | 0.2 to 0.5 | 10 to 10,000 | **0.001 to 0.01**
Share of volume | **Under 1 %**, yet 40 % of the gas mass | 1 to 4 % | **50 to 60 %** | Under 1 % | **30 to 50 %**
Hydrogen as | **H₂**, with CO | **Atoms (H I)** | Atoms and protons | **Protons (H II)** | Bare plasma
Seen by | **CO** and dust, at millimetres (ALMA) | **The 21 cm line** | 21 cm and faint Hα | Pink **Hα** and green [O III] | **Soft X-rays** (Chandra, eROSITA)
```

## 2. Collapse: the Jeans mass

Heat, turbulence and magnetic fields hold a cloud up against its own gravity. In 1902 **James Jeans** found the mass above which gravity wins:

```equation
title: The Jeans mass
M_J = \left( \frac{5 k T}{G \mu m_H} \right)^{3/2} \left( \frac{3}{4 \pi \rho} \right)^{1/2}
T | Temperature | K
\rho | Density | kg/m³
\mu m_H | Mass of the average particle |
```

A warm cloud at 100 K and 10 atoms/cm³ needs thousands of Suns to collapse. A cold core at 10 K and 100,000/cm³ needs **about one**. Dust shields a cloud's inside from starlight, and CO molecules radiate the heat away at millimetre wavelengths, cooling it to 10 K.

```steps
Molecular cloud | 10 K, 100,000 Suns of H₂, CO and dust | purple
Dense core | Fragments below the Jeans mass collapse | navy
Protostar | A spinning disk forms; jets shoot from the poles | blue
T Tauri star | Dust in the disk sticks into pebbles and planetesimals: ALMA sees the rings | teal
Main-sequence star | The core reaches 10 million K and fusion starts; the wind clears the leftover gas | amber
```

## 3. Five kinds of nebula

```cards cols=1 style=top
Emission nebulae (H II regions) | The Orion and Lagoon nebulae. Young O and B stars strip hydrogen of its electrons; as they recombine, the gas glows **Hα red** | red
Reflection nebulae | Round the Pleiades. Stars too cool to ionise gas; dust scatters their blue light more than red | blue
Dark nebulae | The Horsehead and the Coalsack. Dense dusty clouds, black against what lies behind, but much clearer in the infrared | purple
Planetary nebulae and supernova remnants | The Ring and Helix: shells puffed off by dying Sun-like stars. The Crab and Veil: blast waves of exploded giants | teal
```

The lines a nebula glows in name what it is made of:

```spectrum mode=emission
486.1 | Hβ
500.7 | [O III]
656.3 | Hα
658.4 | [N II]
671.6 | [S II]
```

## 4. Hydrogen and dust {style=card colour=purple}

```cards cols=1 style=label
The 21 cm line | The electron and proton of a hydrogen atom flip from aligned to opposed spins once in about 10 million years, giving a radio photon that passes through dust. Ewen and Purcell detected it in 1951; Oort's group then mapped the spiral arms
H₂ is invisible | A symmetric molecule radiates almost nothing at 10 K, so cold clouds are traced by carbon monoxide at 2.6 mm: one CO for every 10,000 H₂
Reddening | Grains 0.01 to 0.2 µm across, like smoke, dim blue light more than red, so distant stars look redder
Ice and organics | In dark clouds, grains grow coats of water, CO, ammonia and methanol. Ultraviolet light builds complex organic molecules on them, before planets form
```

```chart type=bar title="Dimming by dust, by wavelength (green = 100)" unit=" %" max=300
Ultraviolet, 0.2 µm | 280
Blue, 0.44 µm | 132
Green, 0.55 µm | 100
Near-infrared, 2.2 µm | 11
Mid-infrared, 10 µm | 3
```

## 5. Glossary {.wide}

```glossary cols=4
CNM, WNM | Cold and warm neutral medium
GMC | Giant molecular cloud
H I, H II, H₂ | Atomic, ionised and molecular hydrogen
Hα | The red Balmer line of hydrogen, 656.3 nm
HH object | A Herbig-Haro object: a protostar's jet hitting gas
ISM | Interstellar medium
[O III] | Doubly ionised oxygen; its 500.7 nm line is green
PAH | Polycyclic aromatic hydrocarbons, a glowing soot
```

## In short {.summary}

The interstellar medium is the galaxy's recycling engine. Supernovae heat and enrich it, dust and CO cool it to 10 K, gravity collapses it into stars, and young stars light it up as nebulae.

### Seeing through black clouds

Dust grains block visible light but let the longer infrared waves that JWST sees slip past.

### Smoke makes planets

Dust is 1 % of the interstellar medium, but all the rock of planets like Earth.

### Green nebulae, no green stars

Stars shine in broad rainbows; thin nebulae glow in sharp lines, such as oxygen's green 500.7 nm.
