---
type: integration-guide
category: nostr
created: 2025-09-13
tags: [hugo, nostr, static-site, integration]
status: active
---

# hugo + nostr integration options

## current integration landscape

### nsite - direct nostr hosting
**github**: `lez/nsite`
- host static sites directly on nostr
- uses blossom servers for content storage
- mapping from path to content hash stored on relays
- non-kyc deployment with bitcoin payments
- built-in redundancy across gateways

**workflow**:
1. generate hugo site
2. deploy to nsite platform
3. site accessible via nostr gateways
4. censorship-resistant hosting

### blogo - hybrid approach
**github**: `pluja/blogo`
- lightweight blog engine
- backs up posts to nostr automatically
- dual publishing: traditional + nostr

### static blog discussions
**nip-23**: long-form content specification
- build tools could pull nip-23 posts at build time
- static generation from nostr content
- no client-side js needed

## integration strategies for your hugo blog

### option 1: nsite deployment
**pros**:
- full decentralization
- censorship resistance
- multiple gateway access

**cons**:
- experimental/early stage
- potential seo limitations
- still developing

### option 2: dual publishing
**current setup**: hugo → github → cloudflare pages
**extended**: also publish to nostr relays
- keep existing workflow
- add nostr syndication step
- broader reach + backup

### option 3: hugo + nostr shortcodes
**custom integration**:
- develop hugo shortcodes for nostr publishing
- embed nostr content in hugo posts
- hybrid static/dynamic approach

## technical considerations

### content format
- markdown → hugo processing
- potentially map to nip-23 format
- maintain front matter compatibility

### build process
- existing: hugo build → deploy
- extended: + publish to nostr relays
- could integrate with github actions

### identity management
- generate/manage nostr keypair
- integrate with hugo deployment
- secure key storage for ci/cd

## next steps for implementation
1. experiment with nsite for static hosting
2. explore custom hugo-to-nostr publishing tools
3. consider hybrid approach for maximum reach