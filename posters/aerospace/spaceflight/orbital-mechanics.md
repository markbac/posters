---
title: "Orbital Mechanics and Spacecraft Navigation"
subtitle: Why orbit is sideways speed, why rockets stage, and how probes cross the solar system on almost no fuel
byline: Physics and aerospace engineering explainer
orientation: landscape
columns: 4
paper: a1
width: 1600
document_number: PO-033
colours:
  accent: "#1e3a8a"
  secondary: "#172554"
footer:
  left: Orbital Mechanics
  centre: Aerospace Reference
  qr: https://en.wikipedia.org/wiki/Orbital_mechanics
  qr-label: Orbital mechanics on Wikipedia
---

## Key figures {.stats style=tiles}

| Value | Label |
|---|---|
| 7.8 km/s | Sideways speed to stay in low Earth orbit |
| 9.4 km/s | Δv from the launch pad to low Earth orbit, losses included |
| 35,786 km | Altitude of geostationary orbit, one lap a sidereal day |
| 1.5 million km | From Earth to Sun-Earth L2, home of JWST |

## Introduction {.abstract}

Astronauts on the **International Space Station** float, yet gravity at 400 km is still about 89 % of what it is on the ground. They float because the station is **falling all the time**, while moving sideways so fast that the ground curves away beneath it as quickly as it falls. Newton's cannonball, Tsiolkovsky's rocket equation, Hohmann transfers and Lagrange points explain every counter-intuitive rule of spaceflight.

## 1. Newton's cannonball: orbit is sideways speed, not height

Fire a cannonball sideways from a mountain above the air. Slowly, it falls to the ground. At 7.8 km/s it falls around the curve of the Earth for ever.

```equation
title: Vis-viva: speed at any point of an orbit
v^2 = GM \left( \frac{2}{r} - \frac{1}{a} \right)
v | Orbital speed | m/s
GM | Earth's gravitational parameter, 3.986 × 10¹⁴ | m³/s²
r | Distance from Earth's centre now | m
a | Semi-major axis of the orbit | m
```

```cards cols=1 style=top
Lower is faster | Gravity weakens as 1/r², so a satellite at 400 km laps Earth in 90 minutes at 7.7 km/s, and a geostationary one takes a day at 3.07 km/s | navy
Brake to catch up | Trailing the ISS by 10 km? Speeding up lifts you to a higher, slower orbit and you fall further behind. Brake to drop into a lower, faster lane, overtake, then climb back | blue
```

## 2. The rocket equation: why rockets stage

A rocket pushes on nothing but its own exhaust, and must carry the fuel it will burn later. So the fuel needed grows **exponentially** with the change of velocity, **Δv**.

```equation
title: Tsiolkovsky rocket equation
\Delta v = I_{sp} \, g_0 \ln \frac{m_0}{m_f}
\Delta v | Change of velocity | m/s
I_{sp} | Specific impulse: 310 s kerosene, 450 s hydrogen, 3,000 s ion | s
g_0 | Standard gravity, 9.81 | m/s²
m_0, m_f | Mass full, and mass empty | kg
```

```segments
title: Where the mass of a 500-tonne launcher goes
72 | First-stage propellant | 72 % | amber
18 | Second-stage propellant | 18 % | blue
7 | Tanks, engines, fairing | 7 % | navy
3 | Payload | 2 to 4 % | green
```

Dropping the empty first stage resets $m_f$ halfway up, so the second stage pushes a much lighter rocket.

## 3. Changing orbit: the Hohmann transfer

The cheapest way between two circular orbits is half an ellipse that touches both, with one burn at each end, and the engines off in between.

```orbits star=Earth unit=" km" scale=sqrt
orbit: LEO | 6771 | blue
orbit: GEO | 42164 | amber
transfer: 6771 | 42164 | Geostationary transfer orbit
```

A **gravity assist** steals momentum from a planet: fly behind Jupiter and leave faster, for no fuel. Voyager 2 used four.

## 4. The five Lagrange points

Where two bodies orbit each other, such as the Sun and Earth, there are five points where a small craft keeps station with them.


```cards cols=1 style=label
L1 | Sunward, unstable: a constant view of the Sun for SOHO and DSCOVR
L2 | Beyond Earth, unstable: Sun, Earth and Moon all behind one sunshield, for JWST and Gaia
L3 | Behind the Sun: unstable and unused
L4, L5 | 60° ahead and behind: stable, where Trojan asteroids gather
```

## 5. Four Earth orbits compared {.wide}

```compare
| Low Earth (LEO) | Medium Earth (MEO) | Geostationary (GEO) | Sun-synchronous (SSO)
Altitude | **160 to 2,000 km**, ISS at 400 km | **2,000 to 35,786 km**, GPS at 20,200 km | **35,786 km** over the equator | **600 to 800 km**, tilted 98°
Speed and period | 7.8 km/s, **90 minutes** | 3.9 km/s, **12 hours** | 3.07 km/s, **23 h 56 m** | 7.5 km/s, **100 minutes**
From the ground | Crosses the sky in 5 to 10 minutes | Drifts slowly | **Hangs still** | Passes at the same local solar time
Radio round trip | **4 to 25 ms** | 125 to 140 ms | **480 to 600 ms** | About 10 ms overhead
Used for | ISS, Starlink, Hubble | GPS, Galileo, GLONASS, BeiDou | Weather, broadcast TV | Earth imaging, climate
```

## 6. The Δv budget to geostationary orbit {cols=3}

```chart type=waterfall title="Δv from the launch pad (km/s)" unit=" km/s" height=220
Orbital speed | +7.8 | blue | Low Earth orbit
Gravity loss | +1.2 | amber | Climbing straight up
Drag and steering | +0.4 | amber | Through the air
To LEO | =9.4 | navy |
Perigee burn | +2.4 | blue | Onto the transfer ellipse
Apogee burn | +1.5 | blue | Circularise and remove tilt
To GEO | =13.3 | green |
```

> [!TIP]
> From low Earth orbit, the Moon needs only about 4 km/s more. Hence Heinlein's line that orbit is halfway to anywhere.

## 7. Rules of thumb {style=card colour=blue}

```checklist
[x] **Launch east, near the equator**: Earth's spin gives up to 465 m/s for free
[x] **Raise or lower an orbit at perigee**, where the craft is fastest and each kilogram of fuel gives the most energy (the Oberth effect)
[x] **Change the tilt of an orbit at apogee**, where the craft is slowest
[x] **Brake in the air**: aerobraking and heat shields shed 7 to 11 km/s with no fuel
```

## 8. Glossary

```glossary cols=1
Apogee, perigee | Highest and lowest points of an orbit round Earth
Δv | Change of velocity, the currency of a mission's fuel budget
GEO | Geostationary orbit, 35,786 km over the equator
GTO | Geostationary transfer orbit, the ellipse from LEO to GEO
Isp | Specific impulse: how efficiently an engine uses propellant
JWST | James Webb Space Telescope, at Sun-Earth L2
LEO, MEO | Low and medium Earth orbit
Prograde, retrograde | Thrust along the direction of motion, or against it
SSO | Sun-synchronous orbit, always over the same local time
```


## In short {.summary}

Staying in space is about sideways speed, not height. Staging beats the exponential rocket equation, Hohmann transfers move between orbits on two short burns, and Lagrange points give telescopes a place to park.

### Gravity is strong in orbit

Astronauts are weightless because they fall all the time, round the curve of the Earth.

### Brake to go faster

A burn against the motion drops a craft into a lower, faster orbit: the key to every docking.

### Mass costs mass

Every kilogram sent beyond Earth needs ten or more on the launch pad.
