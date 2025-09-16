---
type: documentation
category: nostr
created: 2025-09-13
tags: [nostr, protocol, decentralized, p2p]
status: active
---

# nostr protocol fundamentals

## what is nostr?
**Notes and Other Stuff Transmitted by Relays** - a decentralized protocol for censorship-resistant communication

### core architecture
- **clients**: user interfaces (like web/mobile apps)
- **relays**: websocket servers that store and distribute data
- **cryptographic identity**: public/private key pairs replace usernames/passwords

### how it works
1. generate keypair (public = identity, private = signature)
2. write content, sign with private key
3. send to multiple relays
4. followers receive from relays they monitor
5. cryptographic verification ensures authenticity

## key advantages over traditional platforms

### censorship resistance
- no single point of failure
- content lives on multiple relays
- can't be globally censored

### user sovereignty
- you own your identity (keypair)
- control your data and connections
- not dependent on any company

### interoperability
- protocol not platform
- multiple clients can access same content
- switch apps without losing followers

## 2025 momentum
- 18+ million registered users
- jack dorsey donated $10m+ to development
- mainstream adoption predicted for 2025
- beyond social: wikis, marketplaces, file sharing

## technical standards
**NIPs** (nostr implementation possibilities) define:
- what MUST be implemented
- what SHOULD be implemented
- what MAY be implemented

## decentralized internet vision alignment
- flips "dumb client/smart server" to "smart client/dumb server"
- users control identity and data
- censorship-resistant by design
- interoperable ecosystem vs siloed platforms