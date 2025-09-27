---
type: log
category: admin
created: 2025-09-27
modified: 2025-09-27
tags: [neuromancer, ai, audio, codec, music, recommendations, research]
status: active
---

# SNAC Audio Codec Exploration

## Overview
Explored the SNAC (Multi-Scale Neural Audio Codec) repo: https://github.com/hubertsiuzdak/snac. It's a neural audio compression tool that encodes audio (speech, music, sound effects) into hierarchical discrete tokens at low bitrates (0.98–2.6 kbps). Captures multi-resolution features: coarse tokens (~10 Hz for long contexts like song structure) and fine details for perceptual reconstruction. Pretrained models available on Hugging Face for mono audio at 24/32/44 kHz.

## Potential for Personalization
To train on favorite songs: Fine-tune a pretrained model (e.g., snac_32khz) on a custom dataset of your playlist using PyTorch. Encode songs into tokens as features, then build recommendations via token similarity search or train a language model (e.g., adapt MusicGen) on them to generate/suggest tracks matching preferences.

## Genre Categorization
Categorize encoded tokens by music genres (e.g., rock, electronic, hip-hop) to enable genre-specific embeddings. This allows targeted fine-tuning: group songs by genre in training data, producing genre-aware token representations for more precise recommendations within or across styles.

## Methodology Gap
Key challenge: Collecting a diverse set of unheard songs for testing recommendations. Current playlists risk confirmation bias; need unbiased evaluation dataset (e.g., from Spotify APIs or public benchmarks) to measure true discovery quality against held-out tracks, ensuring recs expand tastes effectively.

*Excited to prototype this for neuromancer's knowledge synthesis – turning audio prefs into actionable insights! 🚀*
