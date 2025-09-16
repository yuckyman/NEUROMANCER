---
type: reference
category: nostr
created: 2025-09-13
tags: [nostr, clients, tools, aggregation]
status: active
---

# nostr clients & aggregation tools

## content creation clients

### long-form writing
- **habla.news**: articles and blogs on nostr
- **yakihonne**: beautifully designed long-form platform
- **highlighter**: read, highlight, share with nostr integration

### multimedia
- **wavlake**: music streaming with artist zaps
- **fountain**: podcasting 2.0 with nostr integration

### general purpose
- **primal**: feature-rich web/ios/android client
- **damus**: popular ios-native experience
- **amethyst**: privacy-focused android client

## aggregation & discovery tools

### search & discovery
- **nostr.band**: search engine for profiles, posts, relays
- comprehensive nostr content discovery
- advanced filtering and search capabilities

### relay management
- **bostr**: relay aggregator proxy (nodejs)
- **bostr2**: relay aggregator proxy (go)
- manage connections to multiple relays
- optimize content distribution

## content syndication model

### the outbox model
unique to nostr's architecture:

1. **announce outbox relays**: publish which relays you use
2. **followers discover**: clients look up your relay announcements
3. **direct monitoring**: followers connect to your outbox relays
4. **continuous updates**: real-time content syndication

### vs traditional syndication
- **traditional**: centralized distribution through platforms
- **nostr**: decentralized relay-based distribution
- **smart clients**: decide which relays to monitor
- **user control**: choose your content distribution strategy

## aggregation for blog content

### content types suitable for aggregation
- nip-23: long-form articles (perfect for blog posts)
- short notes: updates, announcements
- media attachments: images, videos
- external links: link sharing and curation

### aggregation strategies
- **multi-relay publishing**: distribute to various relays
- **topic-based relays**: specialized content distribution
- **community relays**: audience-specific syndication
- **backup relays**: ensure content persistence

## tools for your use case

### for blog aggregation
1. **nostr.band** for discovering relevant content
2. **primal** for content management and curation
3. **habla.news** for long-form blog-style content
4. **custom relay setup** for your specific aggregation needs

### development resources
- **awesome-nostr**: comprehensive project collection
- **nip documentation**: protocol specifications
- **nostrapps.com**: browse the full ecosystem