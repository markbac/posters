---
title: "IoT Application Protocols: MQTT, CoAP and HTTP"
subtitle: Publish-subscribe brokers against request-response web transfers
byline: IoT protocols
orientation: portrait
columns: 3
paper: a1
width: 1250
document_number: PO-007
footer:
  left: MQTT, CoAP and HTTP
  centre: IoT Protocols Reference
  qr: https://mqtt.org/
  qr-label: mqtt.org
---

## Key figures {.stats style=tiles}

| Value | Label |
|---|---|
| 2 bytes | The smallest MQTT fixed header |
| 4 bytes | The CoAP header, over UDP |
| 2 packets | For a confirmed CoAP report: request and acknowledgement |
| 3 levels | Of MQTT delivery guarantee: QoS 0, 1 and 2 |

## Introduction {.abstract}

The application protocol decides how many packets cross the radio, and how a server finds a device. **HTTP** is universal, but its text headers and TCP and TLS handshakes drain batteries on cellular links. **MQTT** connects devices through a **broker** over one long-lived TCP connection. **CoAP** brings compact REST to UDP, in a 4-byte header.

## 1. Three models

```cards cols=1 style=top
MQTT: publish and subscribe | Devices publish to topics such as site/floor1/temp on a broker; any number of subscribers get a copy, without knowing each other | green
CoAP: REST over UDP | Binary request and response, with Observe for subscriptions and confirmable messages for retries: made for sleeping nodes and LwM2M | navy
HTTP: the web | Text headers over TCP and TLS: easy cloud integration, for mains-powered gateways and Wi-Fi appliances | blue
```

## 2. Waking up to send

A node that wakes once an hour pays mostly for setting up the connection:

```lanes
CoAP, UDP | *Send CON | *Receive ACK | Sleep at once
MQTT, TCP | *TCP handshake | *TLS handshake | *CONNECT, PUBLISH
HTTP, TCP | *TCP handshake | *TLS handshake | *Request, 200 OK
```

```chart type=bar title="Bytes on air for one 20-byte report after sleep (typical)" unit=" B" max=1800
CoAP, DTLS with connection ID | 96
MQTT, TLS resumed | 380
MQTT, full TLS | 1420
HTTPS, full TLS | 1680
```

## 3. An MQTT PUBLISH

```hex-dissect cols=8 title="QoS 1 PUBLISH of 21.4 to t/1"
bytes: 32 0b 00 03 74 2f 31 10 42 32 31 2e 34
0 | Fixed header | 0x32: PUBLISH, QoS 1 | navy
1 | Remaining length | 11 bytes | grey
2-3 | Topic length | 3 | blue
4-6 | Topic | t/1 | blue
7-8 | Packet ID | 0x1042, for the PUBACK | amber
9-12 | Payload | 21.4 | green
```

## 4. Topics that scale

```syntax-anatomy
v1/acme/dev-042/telemetry
v1 | Version of the topic scheme | grey
acme | Tenant | navy
dev-042 | Device: broker permissions key on it | blue
telemetry | Message kind | green
```

## 5. Delivery guarantees

```cards cols=1 style=label
MQTT QoS 0 | At most once: no acknowledgement
MQTT QoS 1 | At least once: the broker replies PUBACK; retried until it does
MQTT QoS 2 | Exactly once: a four-step handshake; the most air time
CoAP CON, NON | Confirmable messages need an ACK over UDP; non-confirmable ones do not
```

> [!TIP]
> Give MQTT a **last will**: a retained `offline` message the broker publishes for you if the device vanishes.

## 6. Three protocols compared {.wide}

```compare
| HTTP/1.1, HTTP/2 | MQTT 3.1.1, 5.0 | CoAP (RFC 7252)
Model | Client and server, REST | Publish and subscribe, via a broker | Client and server, REST, with Observe
Transport | TCP | TCP, or WebSockets | UDP; also TCP, SMS, non-IP
Security | TLS | TLS, port 8883 | DTLS, port 5684
Header | Text (HPACK in HTTP/2) | 2 bytes and a UTF-8 topic | 4 bytes and compact options
Server push | Polling, SSE or WebSockets | **Built in** | **Built in**: Observe
Device management | Your own JSON endpoints | Your own topics, or Sparkplug B | **Standard**: LwM2M
Power | Mains or Wi-Fi | Always on, or short sleeps | **Years on a cell**: NB-IoT, LoRaWAN
```

## 7. Which one

```structogram
if Sleeps in PSM, on NB-IoT or UDP?
  CoAP, with LwM2M
else
  if Frequent two-way events, many to many?
    MQTT over TLS
  else
    HTTPS, to existing web APIs
```

## 8. Production checklist {style=card colour=green}

```checklist
[x] No plain ports on public networks: not 1883, 5683 or 80
[x] DTLS connection IDs or TLS resumption, so waking nodes skip full handshakes
[x] Topics prefixed with tenant and device, with broker permissions on them
[x] CBOR payloads, not JSON, on narrowband links
[x] Exponential back-off with jitter on reconnect, to prevent storms
```

## 9. Glossary

```glossary cols=1
CON, NON | Confirmable and non-confirmable CoAP messages
DTLS | TLS over datagrams
LWT | MQTT last will and testament
QoS | MQTT quality of service
REST | Representational state transfer
SSE | Server-sent events
```

## In short {.summary}

CoAP over UDP for battery devices that wake to send one packet; MQTT over TCP for event streams between many parties; HTTPS where power and bandwidth are plentiful.

### Two packets and back to sleep

No handshake and a 4-byte header: a confirmed CoAP report is two packets.

### A broker fans out

One MQTT connection lets a broker route messages between thousands of devices and services.

### Handshakes cost more than data

CBOR and session resumption cut air time by most of it.

## References {.references}

1. OASIS, *MQTT Version 5.0*, 2019.
2. IETF RFC 7252, *The Constrained Application Protocol (CoAP)*, 2014.
