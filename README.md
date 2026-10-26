# Posters

Single-page A1 explainer posters on astronomy, embedded systems, IoT, software engineering and science, written in Markdown and built with [py-doc](https://github.com/markbac/py-doc).

## Get the PDFs

Every merge to `main` publishes a [release](../../releases/latest) with one PDF per poster, `posters-pdf.zip` with all of them, and `posters-html.zip` with the self-contained HTML pages. Each PDF prints its release version under its footer.

## Build them yourself

You need py-doc, and Docker for its tool container, which draws the diagrams and prints the PDFs.

```bash
python -m pip install "py-doc @ git+https://github.com/markbac/py-doc"
py-doc tools build                 # once: the tool image
py-doc poster --pdf                # every poster and its PDF, into build/
py-doc poster lwm2m --watch        # one poster, rebuilt and reloaded on every save
```

## Add a poster

1. Write it under `posters/<category>/<topic>/<name>.md`, with front matter like the others: `title`, `subtitle`, `orientation`, `paper`, `document_number` and `footer`.
1. Add an entry for it under `posters:` in `py-doc.yml`. CI fails if a poster is missing from it.
1. Open a pull request. CI builds every poster and checks that each PDF is one page; the PDFs are attached to the run.

The guides in py-doc, *Writing a poster* and *Posters*, list every block. These posters use them where a picture says it better than words: `orbits`, `spectrum`, `logscale`, `hex-dissect`, `memory`, `pinout`, `code-compare`, `equation`, `timeline`, `bowtie` and more.

## Releases

`.github/workflows/posters.yml` runs on every pull request and every push to `main`:

| Step | Pull request | Push to main |
|---|---|---|
| Check every poster is listed in `py-doc.yml` | Yes | Yes |
| Build the tool image, every poster and its PDF | Yes | Yes |
| Check each PDF is one page | Yes | Yes |
| Upload the PDFs and HTML as a run artifact | Yes | Yes |
| Tag the next version (`v1.0.0`, then `v1.1.0`, ...) and publish a GitHub release | No | Yes |

## The posters

### Aerospace

| Poster | Topic | Number | Layout |
|---|---|---|---|
| [Orbital Mechanics and Spacecraft Navigation](posters/aerospace/spaceflight/orbital-mechanics.md) | spaceflight | PO-033 | A1 landscape |

### AI

| Poster | Topic | Number | Layout |
|---|---|---|---|
| [How Large Language Models and Transformers Work](posters/ai/language-models/llm-transformers.md) | language models | PO-037 | A1 landscape |

### Astronomy

| Poster | Topic | Number | Layout |
|---|---|---|---|
| [Cosmology and the Expanding Universe](posters/astronomy/cosmology/cosmology-big-bang.md) | cosmology | PO-040 | A1 landscape |
| [Galaxies, Dark Matter Halos and the Cosmic Web](posters/astronomy/cosmology/galaxies-cosmic-web.md) | cosmology | PO-046 | A1 landscape |
| [Hubble, Cepheid Variables and the Expanding Universe](posters/astronomy/cosmology/hubble-cosmic-expansion.md) | cosmology | PO-043 | A1 landscape |
| [Cosmic Rays, Neutrinos and Multi-Messenger Astronomy](posters/astronomy/observation/cosmic-rays-neutrinos.md) | observation | PO-051 | A1 landscape |
| [Multi-Wavelength Astronomy and Space Telescopes](posters/astronomy/observation/multi-wavelength-telescopes.md) | observation | PO-048 | A1 landscape |
| [Asteroids, Comets, Meteorites and Planetary Defence](posters/astronomy/planetary-science/asteroids-comets-defence.md) | planetary science | PO-050 | A1 landscape |
| [Astrobiology, the Drake Equation and the Fermi Paradox](posters/astronomy/planetary-science/astrobiology-fermi-paradox.md) | planetary science | PO-052 | A1 portrait |
| [How Astronomers Find and Study Exoplanets](posters/astronomy/planetary-science/exoplanets-detection.md) | planetary science | PO-041 | A1 portrait |
| [The Solar System: Formation, Giant Planets and Ocean Moons](posters/astronomy/planetary-science/solar-system-icy-moons.md) | planetary science | PO-049 | A1 landscape |
| [Solar Physics, Space Weather and Earth's Magnetosphere](posters/astronomy/planetary-science/solar-system-space-weather.md) | planetary science | PO-042 | A1 landscape |
| [Black Holes, Spacetime Curvature and Gravitational Waves](posters/astronomy/stars/black-holes-relativity.md) | stars | PO-039 | A1 landscape |
| [Globular Clusters and Dating the Oldest Stars](posters/astronomy/stars/globular-clusters-stellar-ages.md) | stars | PO-044 | A1 landscape |
| [The Interstellar Medium, Nebulae and Star Formation](posters/astronomy/stars/interstellar-medium-nebulae.md) | stars | PO-045 | A1 landscape |
| [Neutron Stars, Pulsars, Magnetars and Fast Radio Bursts](posters/astronomy/stars/neutron-stars-pulsars.md) | stars | PO-047 | A1 landscape |
| [The Life and Death of Stars: Fusion to Supernovae](posters/astronomy/stars/stellar-evolution-fusion.md) | stars | PO-038 | A1 landscape |

### Embedded

| Poster | Topic | Number | Layout |
|---|---|---|---|
| [Embedded Rust vs C for Bare-Metal Firmware](posters/embedded/firmware/embedded-rust-vs-c.md) | firmware | PO-026 | A1 landscape |
| [Event-Driven Architecture and State Machines](posters/embedded/firmware/event-driven-hsm.md) | firmware | PO-029 | A1 portrait |
| [Defensive Embedded C and Safety Guidelines](posters/embedded/firmware/misra-defensive-c.md) | firmware | PO-025 | A1 portrait |
| [Superloop vs Real-Time Operating System](posters/embedded/firmware/superloop-vs-rtos.md) | firmware | PO-010 | A1 portrait |
| [Mixed-Signal Chains: ADC, PWM and DMA](posters/embedded/hardware/adc-pwm-dma.md) | hardware | PO-018 | A1 landscape |
| [Low-Power Embedded Design: Sleep Modes and Battery Maths](posters/embedded/hardware/low-power.md) | hardware | PO-012 | A1 landscape |
| [Microcontroller vs Microprocessor](posters/embedded/hardware/mcu-vs-mpu.md) | hardware | PO-003 | A1 landscape |
| [Microcontroller Memory Maps and Bootloaders](posters/embedded/hardware/memory-bootloader.md) | hardware | PO-011 | A1 portrait |
| [Closed-Loop Control and Sensor Filtering](posters/embedded/hardware/pid-filtering.md) | hardware | PO-017 | A1 landscape |
| [Embedded Serial Buses](posters/embedded/hardware/serial-buses.md) | hardware | PO-005 | A1 landscape |
| [Hardware Debugging and Real-Time Trace](posters/embedded/test-and-debug/debug-trace.md) | test and debug | PO-016 | A1 portrait |
| [Embedded Testing, Mocking and Hardware-in-the-Loop](posters/embedded/test-and-debug/embedded-testing-hil.md) | test and debug | PO-027 | A1 portrait |

### Energy

| Poster | Topic | Number | Layout |
|---|---|---|---|
| [How the Electrical Power Grid Works](posters/energy/power-grid/electrical-grid.md) | power grid | PO-032 | A1 landscape |

### IoT

| Poster | Topic | Number | Layout |
|---|---|---|---|
| [Bluetooth Low Energy: Advertising and Attributes](posters/iot/connectivity/ble-gatt.md) | connectivity | PO-019 | A1 portrait |
| [Positioning and Time Synchronisation](posters/iot/connectivity/gnss-time-sync.md) | connectivity | PO-024 | A1 landscape |
| [Low-Power Wide-Area Networks](posters/iot/connectivity/lpwan.md) | connectivity | PO-009 | A1 portrait |
| [Thread, Matter and IPv6 Mesh Networking](posters/iot/connectivity/matter-thread.md) | connectivity | PO-020 | A1 landscape |
| [NB-IoT: Narrowband Internet of Things](posters/iot/connectivity/nbiot.md) | connectivity | PO-001 | A1 landscape |
| [Binary Serialisation and Compact Data Formats](posters/iot/protocols/cbor-protobuf-json.md) | protocols | PO-022 | A1 portrait |
| [Binary Framing and Checksums](posters/iot/protocols/framing-crc.md) | protocols | PO-006 | A1 portrait |
| [LwM2M: Lightweight Machine-to-Machine](posters/iot/protocols/lwm2m.md) | protocols | PO-002 | A1 landscape |
| [Industrial Fieldbus Protocols: Modbus and CANopen](posters/iot/protocols/modbus-canopen.md) | protocols | PO-021 | A1 landscape |
| [IoT Application Protocols: MQTT, CoAP and HTTP](posters/iot/protocols/mqtt-coap-http.md) | protocols | PO-007 | A1 portrait |

### Science

| Poster | Topic | Number | Layout |
|---|---|---|---|
| [Molecular Biology as Digital Code: Genome to Gene Editing](posters/science/biology/dna-molecular-machines.md) | biology | PO-034 | A1 portrait |
| [How the Human Immune System Fights Infection](posters/science/biology/immune-system.md) | biology | PO-035 | A1 landscape |
| [The Physics and Chemistry of Espresso and Coffee Extraction](posters/science/chemistry/coffee-extraction-science.md) | chemistry | PO-036 | A1 landscape |

### Software

| Poster | Topic | Number | Layout |
|---|---|---|---|
| [The C4 Model for Software Architecture](posters/software/architecture/c4-model.md) | architecture | PO-013 | A1 landscape |
| [Domain-Driven Design: Contexts and Aggregates](posters/software/architecture/domain-driven-design.md) | architecture | PO-030 | A1 landscape |
| [Hexagonal, Clean and Layered Architecture](posters/software/architecture/hexagonal-clean-arch.md) | architecture | PO-028 | A1 landscape |
| [Resilience and Distributed Systems Patterns](posters/software/architecture/resilience-patterns.md) | architecture | PO-031 | A1 portrait |
| [Containers vs Virtual Machines](posters/software/practices/docker-containers.md) | practices | PO-014 | A1 portrait |
| [Git: Distributed Version Control](posters/software/practices/git.md) | practices | PO-004 | A1 landscape |
| [Public Key Infrastructure and Hardware Roots of Trust](posters/software/security/pki-x509-hsm.md) | security | PO-023 | A1 portrait |
| [Software Bill of Materials and Supply-Chain Security](posters/software/security/sbom-security.md) | security | PO-015 | A1 portrait |
| [Transport Layer Security for Constrained Devices](posters/software/security/tls-dtls.md) | security | PO-008 | A1 portrait |
