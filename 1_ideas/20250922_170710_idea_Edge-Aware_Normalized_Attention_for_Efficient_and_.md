---
title: Edge-Aware Normalized Attention for Efficient and Detail-Preserving Single
  Image Super-Resolution
link: https://arxiv.org/abs/2509.14550
summary: 'The article discusses an edge-guided attention mechanism for single-image super-resolution (SISR). This method derives an adaptive modulation map from jointly encoded edge features and intermediate feature activations, then applies it to normalize and reweight responses, selectively amplifying structurally salient regions while suppressing spurious textures. The mechanism is designed to balance fidelity, perceptual realism, and training stability by combining pixel-wise, perceptual, and adversarial terms.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 470478d89ba495714370632dfcc52a9644a79c2e6f58cd87b292b0f6fcc7daba
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:10.227318'
category: 24-computing
---

arXiv:2509.14550v1 Announce Type: new Abstract: Single-image super-resolution (SISR) remains highly ill-posed because recovering structurally faithful high-frequency content from a single low-resolution observation is ambiguous. Existing edge-aware methods often attach edge priors or attention branches onto increasingly complex backbones, yet ad hoc fusion frequently introduces redundancy, unstable optimization, or limited structural gains. We address this gap with an edge-guided attention mechanism that derives an adaptive modulation map from jointly encoded edge features and intermediate feature activations, then applies it to normalize and reweight responses, selectively amplifying structurally salient regions while suppressing spurious textures. In parallel, we integrate this mechanism into a lightweight residual design trained under a composite objective combining pixel-wise, perceptual, and adversarial terms to balance fidelity, perceptual realism, and training stability. Extensi...