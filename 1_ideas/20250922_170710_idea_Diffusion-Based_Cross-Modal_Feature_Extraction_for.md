---
title: Diffusion-Based Cross-Modal Feature Extraction for Multi-Label Classification
link: https://arxiv.org/abs/2509.15553
summary: 'The article discusses a new framework called Diff-Feat, which extracts intermediate features from pre-trained diffusion-Torres models for images and text. It focuses on multi-label classification tasks where the most discriminative intermediate feature occurs at the middle step of the diffusion process in Transformer-based models. The authors observe that this phenomenon is more pronounced for image tasks compared to language tasks. They also present a heuristic local-search algorithm called "i" that can find the locally optimal solution, which they call "Layer 12." This finding has implications for improving classification performance across various datasets and applications.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 6aae4362cddb5b08149c416fb7a864f5671c93165f1560010f28badc032df8a5
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:10.050385'
category: 24-computing
---

arXiv:2509.15553v1 Announce Type: new Abstract: Multi-label classification has broad applications and depends on powerful representations capable of capturing multi-label interactions. We introduce \textit{Diff-Feat}, a simple but powerful framework that extracts intermediate features from pre-trained diffusion-Transformer models for images and text, and fuses them for downstream tasks. We observe that for vision tasks, the most discriminative intermediate feature along the diffusion process occurs at the middle step and is located in the middle block in Transformer. In contrast, for language tasks, the best feature occurs at the noise-free step and is located in the deepest block. In particular, we observe a striking phenomenon across varying datasets: a mysterious "Layer $12$" consistently yields the best performance on various downstream classification tasks for images (under DiT-XL/2-256$\times$256). We devise a heuristic local-search algorithm that pinpoints the locally optimal "i...