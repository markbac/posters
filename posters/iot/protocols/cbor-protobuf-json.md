---
title: "Binary Serialisation and Compact Data Formats"
subtitle: Packing structured telemetry and commands into minimal bytes without sacrificing schema evolution
byline: Embedded Data Formats & Protocol Serialisation Explainer
orientation: portrait
columns: 2
paper: a1
width: 1200
document_number: PO-022
version: "1.0"
colours:
  accent: "#4f46e5"
  secondary: "#4338ca"
footer:
  left: CBOR vs Protobuf vs JSON Explainer
  centre: Data Serialisation Reference
  right: RFC 8949 CBOR, Protocol Buffers & JSON Guide
  qr: https://cbor.io/
  qr-label: RFC 8949 CBOR Spec
---

## Key figures {.stats style=tiles}

| Value | Label | Change | Verdict |
|---|---|---|---|
| 54 bytes | Typical text JavaScript Object Notation (JSON) sensor payload | human-readable | bad |
| 19 bytes | Same payload in Concise Binary Object Representation (CBOR) | `-65%` wire size | good |
| 11 bytes | Same payload in schema-compiled Protocol Buffers (`Protobuf`) | `-80%` wire size | good |
| 0 fragility | Both CBOR and Protobuf tolerate adding new fields safely | vs raw C structs | good |

## Introduction {.abstract}

Why not cast a C `struct` to a `uint8_t*` pointer and send it over the radio? Raw C structs break as soon as compiler padding, endianness or firmware versions change. Meanwhile, text **JavaScript Object Notation (JSON)** wastes cellular battery life formatting numbers as **American Standard Code for Information Interchange (ASCII)** strings and repeating key names. **Concise Binary Object Representation (CBOR)** and **Protocol Buffers (`Protobuf`)** provide compact, endian-safe binary encoding with clean schema evolution.

## 1. Encoding the exact same sensor packet three ways {.wide}

Consider a sensor reading with three fields: `{"id": 42, "temp": 21.5, "ok": true}`. Compare how each format lays out those values on the wire:

```figure
@segments
title: 1. Text JSON — 36 bytes (ASCII strings, quotes, colons, commas and decimal text conversion)
10 | {"id":42,"temp":21.5,"ok":true} (31 to 36 ASCII bytes — requires string parser & strtof()) | 36 B | amber
+++
@segments
title: 2. Self-Describing CBOR (Map with integer keys: {1: 42, 2: 21.5, 3: true}) — 11 bytes!
1 | A3 (Map of 3) | hdr | navy
2 | 01 18 2A (1: 42) | int | blue
3 | 02 F9 4D 60 (2: 21.5 half-float!) | IEEE 754 | purple
2 | 03 F5 (3: true) | bool | green
+++
@segments
title: 3. Schema-Driven Protocol Buffers (message Sensor { uint32 id=1; float temp=2; bool ok=3; }) — 9 bytes!
2 | 08 2A (Tag 1 Varint = 42) | 2 B | blue
5 | 15 00 00 AC 41 (Tag 2 Float32 = 21.5) | 5 B | purple
2 | 18 01 (Tag 3 Varint = true) | 2 B | green
```

```chart type=bar title="Wire payload size for a 6-field telemetry report (bytes)" unit=" B" max=140
JSON (Text Keys) | 128
CBOR (String Keys) | 74
CBOR (Integer Keys) | 29
Protobuf (nanopb) | 22
```

## 2. How CBOR works (`RFC 8949`)

Every **CBOR** data item starts with a single **Initial Byte** split into a 3-bit **Major Type (`0..7`)** and a 5-bit **Additional Information (`0..31`)** field:

| Major Type (Bits 7..5) | Meaning | Example Encoding |
|---|---|---|
| `0` (`0b000_xxxxx`) | Unsigned integer | `0x0A` = `10` (values `0..23` fit in the initial byte itself!) |
| `1` (`0b001_xxxxx`) | Negative integer | `0x20` = `-1` (`-1 - value`) |
| `2` (`0b010_xxxxx`) | Byte string (`uint8_t[]`) | Raw binary blobs, cryptographic hashes or keys (no Base64 bloat!) |
| `3` (`0b011_xxxxx`) | `UTF-8` text string | Length-prefixed string (no null-terminator scanning needed) |
| `4` (`0b100_xxxxx`) | Array of items | `0x83` = array of 3 elements |
| `5` (`0b101_xxxxx`) | Map of key-value pairs | `0xA3` = map of 3 pairs (keys can be integers to save bytes!) |
| `7` (`0b111_xxxxx`) | Floats, booleans, null | `0xF4` = `false`, `0xF5` = `true`, `0xF9` = 16-bit half-float |

> [!TIP]
> In **CBOR** (and **SenML / LwM2M**), use **integer map keys** (`1`, `2`, `3`) or a **Concise Data Definition Language (`CDDL`)** schema (`zcbor`) instead of repeating string keys (`"temperature"`). Integer keys shrink CBOR to nearly the same size as Protobuf while keeping the wire format self-describing.

## 3. How Protocol Buffers (`Protobuf` / `nanopb`) work

**Protobuf** removes all field names and structural brackets from the wire. Both sender and receiver compile a shared `.proto` schema file (`nanopb` generates static C structs with zero `malloc`). On the wire, every field is a **`[Tag][Value]`** pair where `Tag = (field_number << 3) | wire_type`:

```lcd cols=1
// telemetry.proto (compiled with nanopb for C MCUs)
syntax = "proto3";
message Telemetry {
  uint32 uptime_s   = 1; // Varint (1 to 5 bytes)
  sint32 temp_mc    = 2; // ZigZag signed varint!
  bytes  signature  = 3; // Raw byte array [(max_size) = 64]
}
-- Warning: Use sint32 (ZigZag) for negative numbers!
-- Standard int32 encodes -1 as a 10-byte 64-bit two's complement varint!
```

## 4. Head-to-head comparison {.wide}

```compare
| Raw Packed C `struct` | Text `JSON` (`cJSON` / `jsmn`) | `CBOR` (`zcbor` / `QCBOR`) | Protocol Buffers (`nanopb`)
Schema file required | Shared `.h` header | None (self-describing) | Optional (`CDDL` or schemaless) | **Mandatory `.proto` file**
Wire size efficiency | Smallest (0 tags), fixed width | **Largest** (ASCII + quotes) | **Compact** (especially integer keys) | **Smallest structured** (Varints + tags)
Raw binary byte arrays | Fixed array only | Must Base64-encode (`+33%` size!) | **Native Major Type 2** (`0%` overhead) | **Native `bytes` type** (`0%` overhead)
Schema evolution | **Breaks** if fields are inserted | Easy (ignore unknown keys) | **Easy** (skip unknown keys/tags) | **Easy** (never reuse deleted field IDs)
Standard IoT ecosystems | Custom internal links only | Web REST APIs & cloud | **CoAP, LwM2M, Matter, COSE, FIDO2** | **gRPC**, Google Cloud & Android/iOS apps
```

## 5. Serialisation engineering checklist {style=card colour=purple}

```checklist
[x] Never transmit raw C `struct` memory across different compilers, architectures (`ARM` vs `x86`) or firmware versions
[x] In `Protobuf`, always use `sint32` / `sint64` (ZigZag encoding) when a field can take negative values
[x] In `Protobuf`, bound string and byte-array lengths in `.options` (`max_size: 64`) so `nanopb` allocates static C arrays without `malloc`
[x] In `CBOR`, prefer integer map keys or array-of-values (`CDDL`) over narrowband links like **NB-IoT** and **LoRaWAN**
[x] Include a semantic schema or message type ID in the envelope and silently ignore unknown future fields for forward compatibility
```

## 6. Acronym guide: every term defined {.wide}

```cards cols=4 style=label
CBOR | Concise Binary Object Representation (IETF RFC 8949): compact, self-describing binary data format
JSON | JavaScript Object Notation (RFC 8259): ubiquitous human-readable text format for key-value objects
Protobuf | Protocol Buffers: Google's language-neutral, schema-compiled binary serialisation format
CDDL | Concise Data Definition Language (RFC 8610): schema language used to validate CBOR structures and generate C code
COSE | CBOR Object Signing and Encryption (RFC 9052): compact binary equivalent of JSON Web Tokens (JWT)
SenML | Sensor Measurement Lists (RFC 8428): standard IoT telemetry array structure encoded in CBOR or JSON
TLV & Varint | Tag-Length-Value binary structure and Variable-Length Integer (uses 7 bits per byte + 1 continuation bit)
ASCII & UTF-8 | American Standard Code for Information Interchange and 8-bit Unicode Transformation Format text encodings
```

## In short {.summary}

Replace text **JSON** and fragile raw C structs with **CBOR** (for CoAP, LwM2M or self-describing payloads) or **Protobuf (`nanopb`)** (when both ends share a `.proto` file).

### Never send raw C structs

One compiler update or new struct field shifts every byte offset and bricks compatibility with deployed devices.

### Binary blobs belong in binary formats

Sending a 64-byte cryptographic signature or firmware chunk in JSON requires Base64 encoding; CBOR and Protobuf send raw bytes directly.

### Use `sint32` for negative numbers

In Protobuf, `sint32` ZigZag-maps `-1` to `1` (`1 byte`), whereas `int32` sign-extends `-1` to `10 bytes`!
