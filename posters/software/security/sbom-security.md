---
title: "Software Bill of Materials and Supply-Chain Security"
subtitle: Knowing every dependency, its vulnerabilities, and whether they matter, across firmware and cloud
byline: Software security
orientation: portrait
columns: 2
paper: a1
width: 1100
document_number: PO-015
colours:
  accent: "#b45309"
  secondary: "#92400e"
footer:
  left: SBOM and Supply Chain
  centre: Security Reference
  qr: https://cyclonedx.org/
  qr-label: CycloneDX
---

## Key figures {.stats style=tiles}

| Value | Label |
|---|---|
| 80 % and more | Of a typical product's code that is third-party or open source |
| 2 standards | SPDX and CycloneDX |
| 24 hours | To give early warning of an actively exploited flaw, under the EU Cyber Resilience Act |
| 4 states | In a VEX statement, which cut false alarms |

## Introduction {.abstract}

Firmware and cloud services are built from hundreds of open-source libraries, packages and container layers. When a flaw appears deep in a dependency of a dependency, you cannot defend what you cannot list. A **software bill of materials (SBOM)** is a machine-readable inventory of every component, version, hash, licence and relationship in a build. With **VEX** statements and **SLSA** provenance, triage becomes a query.

## 1. The pipeline

Generate the SBOM in CI, as you build, then scan, triage and sign:

```flow
[Source and lock files|navy] -> [Reproducible build|blue] -Syft, cdxgen, Yocto-> [SBOM: CycloneDX or SPDX|teal] -Grype, Trivy, OSV-> [Findings|amber] -triage-> [VEX statements|green] -Cosign, SLSA-> [Signed attestation|navy]
An SBOM made at build time knows the exact static C libraries and commit hashes that a scan of the finished binary misses.
```

## 2. Naming a component exactly

Each component is named by a **package URL** and a hash, so two tools can never mean different things:

```syntax-anatomy
pkg:github/Mbed-TLS/mbedtls@3.6.0
pkg | Scheme | grey
github | Type: where it comes from | navy
Mbed-TLS | Namespace | blue
mbedtls | Name | green
3.6.0 | Version | amber
```

```json
{
  "bomFormat": "CycloneDX",
  "specVersion": "1.6",
  "components": [{
    "type": "library",
    "name": "mbedtls",
    "version": "3.6.0",
    "purl": "pkg:github/Mbed-TLS/mbedtls@3.6.0",
    "hashes": [{"alg": "SHA-256", "content": "9f86d081884c7d65..."}],
    "licenses": [{"license": {"id": "Apache-2.0"}}]
  }]
}
```

## 3. Two standards {.wide}

```compare
| SPDX | CycloneDX
Who | The Linux Foundation; **ISO/IEC 5962:2021** | **OWASP**; ECMA-424
Built for | **Licence compliance**, copyright and provenance | **Application security**: vulnerabilities and component risk
Covers | Files, packages, containers, operating systems, data | Software, hardware, cryptography and services
Formats | JSON, YAML, XML, tag-value | JSON, XML, Protobuf
Vulnerabilities | Links to advisories; security profiles in SPDX 3.0 | **CVEs and VEX built in**
```

## 4. VEX: is it exploitable here?

A scanner flags every CVE in every linked library, including code that never runs. **VEX** lets the maker state, per CVE, whether the product is affected:

```cards cols=1 style=top
Not affected | No action, with a reason a machine can read, such as vulnerable_code_not_in_execute_path | green
Affected | Reachable in this product: with mitigations until a fix ships | red
Fixed | This release has the patched version, or a backported fix | blue
Under investigation | The security team is checking whether it can be triggered | amber
```

## 5. SLSA: trusting the build

An SBOM is only as trustworthy as the build that made it. **SLSA** sets build levels:

```pyramid
Level 3 | Hardened | Isolated, short-lived builds that cannot reach the signing keys | green
Level 2 | Hosted, signed | A hosted CI service signs the provenance | amber
Level 1 | Provenance | A record of the source, commit and inputs | navy
```

## 6. Compliance checklist {style=card colour=amber}

Laws such as the EU **Cyber Resilience Act** now require SBOMs and vulnerability handling for connected products:

```checklist
[x] A fresh CycloneDX or SPDX document from every release build in CI
[x] Direct and transitive dependencies, including statically linked C libraries and RTOS modules
[x] Every component named by purl and SHA-256
[x] VEX statements published with each firmware release
[x] The binary and its SBOM signed with hardware-backed keys: Sigstore Cosign, or your PKI
```

## 7. Glossary

```glossary cols=1
CRA | The EU Cyber Resilience Act
CVE | Common Vulnerabilities and Exposures: a public flaw ID
purl | Package URL: a standard name for a component
SBOM | Software bill of materials
SLSA | Supply-chain Levels for Software Artifacts
SPDX | Software Package Data Exchange
VEX | Vulnerability Exploitability eXchange
```

## In short {.summary}

Generate an SBOM in every CI build, publish VEX statements to silence false alarms, and sign the binary and its SBOM with SLSA provenance.

### You cannot patch what you cannot list

When a library flaw breaks, an SBOM index lists every affected firmware version in seconds.

### Silence false alarms

VEX tells customers which CVEs sit in code that never runs.

### Sign the provenance

A signed attestation proves a trusted runner built the binary from reviewed source.
