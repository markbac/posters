---
title: "Multi-Wavelength Astronomy and Space Telescopes"
subtitle: Why astronomers observe across the whole spectrum, and how telescopes beat diffraction and the atmosphere
byline: Popular astrophysics explainer
orientation: landscape
columns: 3
paper: a1
width: 1750
document_number: PO-048
colours:
  accent: "#2563eb"
  secondary: "#1e40af"
footer:
  left: Multi-Wavelength Astronomy
  centre: Popular Astrophysics Reference
  qr: https://en.wikipedia.org/wiki/Multiwavelength_astronomy
  qr-label: Multi-wavelength astronomy
---

## Key figures {.stats style=tiles}

| Value | Label |
|---|---|
| Under an octave | Of the spectrum the eye sees: 400 to 700 nm |
| 2 windows | Optical and radio: the bands that reach the ground |
| 6.5 m | JWST's gold mirror, at 40 K, 1.5 million km away |
| 25 µas | Sharpness of the Event Horizon Telescope, an Earth-sized dish |

## Introduction {.abstract}

To see the universe in visible light alone is to hear a symphony through one octave. Cold dust glows in the **far infrared** and **millimetre** bands, and hydrogen gas at **21 cm** in the radio. Young stars shine in the **ultraviolet**, and the gas round black holes in **X-rays and gamma rays**. The atmosphere blocks most of these, so astronomy needs both giant ground telescopes and **space telescopes**.

## 1. The atmosphere: what reaches the ground {.wide}

Oxygen, ozone, water vapour and carbon dioxide absorb most of the spectrum, which protects life and blinds telescopes:

```segments
title: The spectrum from gamma rays to radio (not to scale)
2 | Gamma rays and X-rays: absorbed 30 to 100 km up | Space only: Fermi, Chandra | red
1 | Ultraviolet: absorbed by ozone | Space: Hubble | purple
2 | Visible and near-infrared: the optical window | Ground: ELT, Rubin, Keck | green
2 | Mid and far infrared: absorbed by water vapour | Space: JWST | amber
3 | Radio, 1 mm to 20 m: the radio window | Ground: ALMA, VLA, SKA | blue
```

## 2. Each band, its temperature {.wide}

The hotter a source, the shorter the wavelength it shines brightest at: **Wien's law**, λ_peak = 2,898 µm·K / T.

```compare
| Radio and millimetre | Infrared | Visible and ultraviolet | X-rays and gamma rays
Sources at | **3 to 100 K**, and electrons spiralling in magnetic fields | **20 to 3,000 K**: dust, brown dwarfs, redshifted first galaxies | **3,000 to 100,000 K**: stars, nebulae | **Millions of K and more**, jets, nuclear decay
What shines | The **CMB**, 21 cm hydrogen, CO in molecular clouds, **pulsars**, quasar jets | **Stars forming inside dust**, planet-forming disks, **exoplanet atmospheres** | **Stars**, nebulae, galaxies, white dwarfs | **Black-hole disks**, cluster gas, **supernova shocks**, gamma-ray bursts
Its strength | Passes through dust and cloud, day or night, and allows **interferometry** across continents | **Sees through dust**, which scatters long wavelengths far less | The sharpest images for each metre of mirror | The most violent gravity and magnetic fields in the universe
Flagships | **ALMA**, VLA, FAST, SKA, the **Event Horizon Telescope** | **JWST**, Spitzer, Herschel, Euclid | **Hubble**, Keck, VLT, **Rubin**, **ELT** | **Chandra**, XMM-Newton, IXPE, **Fermi**, CTAO
```

## 3. Diffraction: why size and wavelength set sharpness

```equation
title: The Rayleigh criterion
\theta = 1.22 \, \frac{\lambda}{D}
\theta | Smallest angle the telescope separates | radians
\lambda | Wavelength | m
D | Diameter of the mirror or dish | m
```

| Telescope | λ | D | θ |
|---|---|---|---|
| Hubble | 500 nm | 2.4 m | 0.05″ |
| JWST | 2 µm | 6.5 m | 0.08″ |
| A radio dish | 21 cm | 100 m | 530″ |
| EHT | 1.3 mm | 10,000 km | 0.000025″ |

**Interferometry** links dishes far apart, timed by atomic clocks, so the baseline between them acts as $D$.

## 4. Mirrors, to scale

```sizes shape=circle unit=" m"
ELT | 39.3 | Chile, from 2029 | navy
Keck | 10 | Hawaii, 36 segments | teal
JWST | 6.5 | Infrared, at L2 | amber
Hubble | 2.4 | In orbit since 1990 | grey
```

Twice the diameter gathers **four times the light** and halves the blur.

## 5. Adaptive optics: removing the twinkle

Turbulent air bends starlight a thousand times a second, and blurs a 10 m telescope to the sharpness of a 20 cm one. Adaptive optics measures the blur and bends a thin mirror to undo it.

```flow
[Laser guide star|amber] -589 nm light from sodium at 90 km-> [Wavefront sensor|blue] -1,000 times a second-> [Control computer|navy] -under 0.5 ms-> [Deformable mirror|green]
```

With it, the VLT and Keck followed the star S2 round the Milky Way's black hole, at up to 7,650 km/s.

## 6. Catching X-rays and gamma rays {style=card colour=blue}

```cards cols=1 style=label
Grazing mirrors | X-rays pass straight into a mirror met head-on. Chandra and XMM-Newton nest gold- and iridium-coated barrels that deflect them at about 1°, like a stone skipping on water
Pair telescopes | Gamma rays above 20 MeV cannot be focused. Fermi turns each into an electron and a positron, whose tracks point back to the source
Cherenkov arrays | A TeV gamma ray hits the upper air and makes a nanosecond flash of blue light, which CTAO's dishes catch
```

## 7. Glossary {.wide}

```glossary cols=4
Arcsecond (″) | 1/3,600 of a degree
ALMA | Atacama Large Millimeter/submillimeter Array, Chile
AO | Adaptive optics
EHT | Event Horizon Telescope, which imaged M87* and Sgr A*
ELT | Extremely Large Telescope, 39.3 m
µas | Micro-arcsecond, a millionth of an arcsecond
SKA | Square Kilometre Array, Australia and South Africa
VLBI | Very-long-baseline interferometry
```

## In short {.summary}

Each band of the spectrum shows a different temperature of the universe: radio and infrared the cold and dusty, visible the stars, X-rays and gamma rays the most violent.

### Why Webb's mirror is gold, and cold

Gold reflects over 98 % of infrared. A sunshield the size of a tennis court keeps the telescope at 40 K, so its own heat does not blind it.

### Bigger is better, twice

A larger mirror collects more light, for fainter objects, and blurs less, for finer detail.

### A dish the size of the Earth

Recording radio waves with atomic-clock times on several continents, the Event Horizon Telescope sees as sharply as one dish as wide as the planet.
