---
title: Causal Fingerprints of AI Generative Models
link: https://arxiv.org/abs/2509.15406
summary: 'The article discusses the use of AI generative models to create images, which can leave traces in their generated images that are referred to as model fingerprints. The authors argue that a complete model fingerprint should reflect the causality between image provenance and model traces, which is largely unexplored.

To address this issue, the authors propose a causality-decoupling framework that disentangles it from image-specific content and style in a semantic-invariant latent space derived from pre-trained diffusion reconstruction residual. They also enhance fingerprint granularity with diverse feature representations.

The authors validate their approach by assessing attribution performance across representative GANs and diffusion models and by comparing the performance of different feature representations.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 720afdc642de70cdb30a9a854f5c9e6f88fec93c1812d0fbbf740c312e21dd66
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:11.045193'
category: 24-computing
---

arXiv:2509.15406v1 Announce Type: new Abstract: AI generative models leave implicit traces in their generated images, which are commonly referred to as model fingerprints and are exploited for source attribution. Prior methods rely on model-specific cues or synthesis artifacts, yielding limited fingerprints that may generalize poorly across different generative models. We argue that a complete model fingerprint should reflect the causality between image provenance and model traces, a direction largely unexplored. To this end, we conceptualize the \emph{causal fingerprint} of generative models, and propose a causality-decoupling framework that disentangles it from image-specific content and style in a semantic-invariant latent space derived from pre-trained diffusion reconstruction residual. We further enhance fingerprint granularity with diverse feature representations. We validate causality by assessing attribution performance across representative GANs and diffusion models and by ach...