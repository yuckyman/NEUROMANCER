---
title: 'Lynx: Towards High-Fidelity Personalized Video Generation'
link: https://arxiv.org/abs/2509.15496
summary: 'Lynx is an open-source model for video synthesis that uses a Diffusion Transformer (DiT) foundation to generate personalized videos from single input images. The model introduces two lightweight adapters called ID-adapter and Ref-adapter to ensure identity fidelity while maintaining temporal coherence and visual realism. These modules enable robust identity preservation, but they also introduce fine-grained details across all transformer layers through cross-attention. Lynx has demonstrated superior face resemblance, competitive prompt following, and strong video quality on a curated benchmark of 40 subjects and 20 unbiased prompts.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 0e8b6eab32d1de421f0ddc31eae9b0a900f9f0f685a74eaea3f40b6996dc0383
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:11.691095'
category: 24-computing
---

arXiv:2509.15496v1 Announce Type: new Abstract: We present Lynx, a high-fidelity model for personalized video synthesis from a single input image. Built on an open-source Diffusion Transformer (DiT) foundation model, Lynx introduces two lightweight adapters to ensure identity fidelity. The ID-adapter employs a Perceiver Resampler to convert ArcFace-derived facial embeddings into compact identity tokens for conditioning, while the Ref-adapter integrates dense VAE features from a frozen reference pathway, injecting fine-grained details across all transformer layers through cross-attention. These modules collectively enable robust identity preservation while maintaining temporal coherence and visual realism. Through evaluation on a curated benchmark of 40 subjects and 20 unbiased prompts, which yielded 800 test cases, Lynx has demonstrated superior face resemblance, competitive prompt following, and strong video quality, thereby advancing the state of personalized video generation.