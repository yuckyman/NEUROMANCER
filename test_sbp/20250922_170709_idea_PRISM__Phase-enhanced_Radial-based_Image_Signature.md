---
title: 'PRISM: Phase-enhanced Radial-based Image Signature Mapping framework for fingerprinting
  AI-generated images'
link: https://arxiv.org/abs/2509.15270
summary: 'The article discusses a new framework called PRISM (Phase-enhanced Radial-based Image Signature Mapping) that addresses the challenge of attributing AI-generated images to their creators. PRISM uses a radial reduction of the discrete Fourier transform to capture model-specific signatures and then clusters these signatures using linear discriminant analysis in diverse settings, even if the model's internal details are inaccessible. The authors also provide a detailed description of the framework, including its architecture, components, and implementation details.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 7384971d0b285445866d0cee0890f1371de8497b5d39a024222ac46c47ef9c7c
feed_title: cs.AI updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.AI
date_processed: '2025-09-22T17:07:09.939802'
category: 24-computing
---

arXiv:2509.15270v1 Announce Type: cross Abstract: A critical need has emerged for generative AI: attribution methods. That is, solutions that can identify the model originating AI-generated content. This feature, generally relevant in multimodal applications, is especially sensitive in commercial settings where users subscribe to paid proprietary services and expect guarantees about the source of the content they receive. To address these issues, we introduce PRISM, a scalable Phase-enhanced Radial-based Image Signature Mapping framework for fingerprinting AI-generated images. PRISM is based on a radial reduction of the discrete Fourier transform that leverages amplitude and phase information to capture model-specific signatures. The output of the above process is subsequently clustered via linear discriminant analysis to achieve reliable model attribution in diverse settings, even if the model's internal details are inaccessible. To support our work, we construct PRISM-36K, a novel da...