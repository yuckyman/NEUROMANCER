---
title: Dataset Distillation for Super-Resolution without Class Labels and Pre-trained
  Models
link: https://arxiv.org/abs/2509.14777
summary: 'The article discusses the challenges in training deep neural networks and proposes a novel method called "data distillation" to improve their efficiency. The authors present a framework for single-image super-resolution (SISR) that relies on large datasets but faces limitations due to reliance on pre-trained models and class-specific information. To address these issues, they introduce a new data distillation approach that does not require class labels or pre-trained SISR networks. This method aims to improve the utilization of existing training datasets while maintaining generalizability and applicability.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 1239a70b869229f98cb44ebeadc474661f98a0648d80a97c6d1ba859d75c9389
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:11.268760'
category: 24-computing
---

arXiv:2509.14777v1 Announce Type: new Abstract: Training deep neural networks has become increasingly demanding, requiring large datasets and significant computational resources, especially as model complexity advances. Data distillation methods, which aim to improve data efficiency, have emerged as promising solutions to this challenge. In the field of single image super-resolution (SISR), the reliance on large training datasets highlights the importance of these techniques. Recently, a generative adversarial network (GAN) inversion-based data distillation framework for SR was proposed, showing potential for better data utilization. However, the current method depends heavily on pre-trained SR networks and class-specific information, limiting its generalizability and applicability. To address these issues, we introduce a new data distillation approach for image SR that does not need class labels or pre-trained SR models. In particular, we first extract high-gradient patches and catego...