---
title: "How Astronomers Find and Study Exoplanets"
subtitle: Transits, stellar wobbles, habitable zones and reading alien air with JWST
byline: Planetary science explainer
orientation: portrait
columns: 2
paper: a1
width: 1200
document_number: PO-041
colours:
  accent: "#0d9488"
  secondary: "#0f766e"
footer:
  left: Finding Exoplanets
  centre: Planetary Science Reference
  qr: https://exoplanets.nasa.gov/
  qr-label: NASA exoplanet exploration
---

## Key figures {.stats style=tiles}

| Value | Label |
|---|---|
| Over 6,000 | Confirmed exoplanets, since the first in 1992 |
| 84 ppm | Dimming when an Earth crosses a Sun-like star |
| 9 cm/s | How fast Earth makes the Sun wobble |
| 4.24 ly | To the nearest exoplanet, Proxima Centauri b |

## Introduction {.abstract}

A star outshines its planets a billion times or more: a firefly beside a searchlight, seen from 1,000 km. So astronomers mostly watch the **star**. A planet passing in front dims it, a **transit**, and a planet's pull makes it wobble, which shifts its colour by the **Doppler effect**. Together they give a planet's size, mass and density.

## 1. Four ways to find a planet {.wide}

Size from a transit and mass from the wobble give **density**: rock, water world or gas.

```compare
| Transit (about 74 % of finds) | Radial velocity (19 %) | Microlensing (4 %) | Direct imaging (1 to 2 %)
How it works | The planet blocks a share of the star's light, (R_p / R_s)² | Star and planet circle their common centre, so the star's light shifts blue then red | A star and its planet bend and brighten the light of a star far behind | A mask blocks the starlight; adaptive optics show the planet's own glow
It measures | **Radius** and period | **Minimum mass** and eccentricity | Mass ratio, even for rogue planets | Brightness, temperature, orbit
Best for | Close planets whose orbits are edge-on to us | Heavy planets, and rocky ones round red dwarfs | Planets 1 to 10 AU out, towards the galactic bulge | Young giant planets far from their star
Telescopes | Kepler, TESS, PLATO | HARPS, ESPRESSO, Keck | OGLE, MOA, Roman | JWST, VLT SPHERE, Gemini
```

## 2. Reading a transit

```chart type=line title="A star's brightness through a transit" min=0.985 max=1.002 step=0.005 markers=no axis="Relative brightness" height=220
0 h | 1.000
1 h | 1.000
2 h | 1.000
2.5 h | 0.990
3 h | 0.990
3.5 h | 0.990
4 h | 0.990
4.5 h | 1.000
5 h | 1.000
6 h | 1.000
```

```equation
title: Depth of a transit
\Delta F = \left( \frac{R_p}{R_s} \right)^2
\Delta F | Fraction of light blocked |
R_p, R_s | Radii of the planet and the star | km
```

A Jupiter crossing the Sun blocks 1 %, which is seen from the ground. An Earth blocks 0.0084 %, which needs a space telescope. The time between transits gives the orbit, by Kepler's third law.

## 3. What the planets are like

```chart type=bar title="Confirmed exoplanets by type" unit=" %" max=40
Neptune-like | 35
Gas giants | 31
Super-Earths | 30
Rocky, Earth-sized | 4
```

Small rocky planets are the hardest to find, not the rarest.

```cards cols=2 style=top
Hot Jupiters | Giants eight times closer to their star than Mercury is to the Sun, at 1,500 K. 51 Pegasi b, the first round a Sun-like star, in 1995 | amber
Super-Earths, mini-Neptunes | The commonest planets are 1.2 to 3.5 times Earth's size, a size our Solar System lacks. Below about 1.6 they are rock; above 2, they keep thick gas | teal
Eyeball worlds | Round red dwarfs the habitable zone is so close that tides lock one face in daylight and the other in night | blue
Lava worlds | 55 Cancri e and Kepler-78b orbit in 18 and 8.5 hours, with oceans of magma on their day sides | red
```

## 4. Habitable zones: TRAPPIST-1

The habitable zone is where water could be liquid on a planet's surface. Round a cool red dwarf it lies very close in. TRAPPIST-1 has seven Earth-sized planets, three or four in its zone, all closer than Mercury is to the Sun.

```orbits star=TRAPPIST-1 unit=" AU" habitable=0.025-0.05
orbit: b | 0.0115 | grey
orbit: c | 0.0158 | grey
orbit: d | 0.0223 | teal
orbit: e | 0.0293 | green
orbit: f | 0.0385 | green
orbit: g | 0.0469 | green
orbit: h | 0.0619 | blue
```

> [!WARNING]
> Red dwarfs are 75 % of all stars, and their planets are easy to find. But their flares may strip the air from close planets.

## 5. Reading alien air with JWST {.wide}

During a transit, a little starlight passes through the planet's atmosphere. Each molecule absorbs its own infrared wavelengths, so the planet looks slightly larger at those: the transit becomes a chemical barcode.

```flow
[Starlight|amber] -through the planet's air-> [Absorbed at each molecule's wavelengths|teal] -JWST NIRSpec-> [In transit compared with out|blue] -> [H₂O, CO₂ at 4.3 µm, CH₄, SO₂|green]
```

In 2022 JWST found carbon dioxide, and sulphur dioxide made by starlight, in the air of the hot Saturn **WASP-39b**.

## 6. Signs of life {style=card colour=teal}

```checklist
[x] **Liquid water**: a planet in the habitable zone, with enough air pressure
[x] **Chemical disequilibrium**: oxygen or ozone together with methane, which destroy each other unless something keeps making both
[x] **More than one line of evidence**: volcanoes and sunlight can make oxygen or methane alone
[ ] **An Earth twin imaged**: the Habitable Worlds Observatory, a 6 to 8 m space telescope with a coronagraph, planned for the 2040s
```

## 7. Glossary {.wide}

```glossary cols=4
AU | Astronomical unit, 149.6 million km
HZ | Habitable zone
M⊕, R⊕ | Earth's mass and radius
ppm | Parts per million
RV | Radial velocity, the Doppler wobble method
TESS | Transiting Exoplanet Survey Satellite
TTV | Transit timing variation: tugs between sibling planets
HWO | Habitable Worlds Observatory
```

## In short {.summary}

Transits give a planet's size, wobbles its mass, and the starlight through its air its chemistry.

### Planets outnumber stars

On average every star in the Milky Way has at least one planet: hundreds of billions in all.

### Mass and radius give density

A shadow alone cannot tell rock from gas. Size and mass together can.

### No single gas proves life

Look for gases that should not be together, such as oxygen with methane.
