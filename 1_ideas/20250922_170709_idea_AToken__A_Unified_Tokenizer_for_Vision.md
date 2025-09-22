---
title: 'AToken: A Unified Tokenizer for Vision'
link: https://arxiv.org/abs/2509.14476
summary: 'The article discusses the introduction of a new unified visual tokenizer called AToken that combines reconstruction and semantic understanding across various image, video, and 3D assets. The tokenizer uses 4D rotary position embeddings to process inputs at different resolutions and durations. To ensure stable training, an adversarial-free objective combining perceptual and Gram matrix losses is introduced. AToken supports both continuous and discrete latent tokens and achieves a high reconstruction quality with rFID of 0.21.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: e9fdc8e82d6cd98a586ebc53cbc5db4c8876089e8a47a830156edc8d14ffd2bf
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:09.834186'
category: 24-computing
---

arXiv:2509.14476v1 Announce Type: new Abstract: We present AToken, the first unified visual tokenizer that achieves both high-fidelity reconstruction and semantic understanding across images, videos, and 3D assets. Unlike existing tokenizers that specialize in either reconstruction or understanding for single modalities, AToken encodes these diverse visual inputs into a shared 4D latent space, unifying both tasks and modalities in a single framework. Specifically, we introduce a pure transformer architecture with 4D rotary position embeddings to process visual inputs of arbitrary resolutions and temporal durations. To ensure stable training, we introduce an adversarial-free training objective that combines perceptual and Gram matrix losses, achieving state-of-the-art reconstruction quality. By employing a progressive training curriculum, AToken gradually expands from single images, videos, and 3D, and supports both continuous and discrete latent tokens. AToken achieves 0.21 rFID with 8...