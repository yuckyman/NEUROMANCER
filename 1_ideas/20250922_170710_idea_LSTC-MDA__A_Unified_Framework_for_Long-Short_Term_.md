---
title: 'LSTC-MDA: A Unified Framework for Long-Short Term Temporal Convolution and
  Mixed Data Augmentation in Skeleton-Based Action Recognition'
link: https://arxiv.org/abs/2509.14619
summary: 'The article discusses a new framework called LSTC-MDA, which combines temporal modeling with data diversity to improve action recognition. The authors propose an LSTC module that uses parallel short- and long-term branches to fuse these features adaptively. They also extend the Joint Mixing Data Augmentation (JMDA) method by adding an Additive Mixup at the input level. The results of their experiments show that LSTC-MDA achieves state-of-the-art performance on a dataset of 10,000 action videos.

The key contributions of this work include:
1. A unified framework for temporal modeling and data diversity
2. An LSTC module with parallel short- and long-term branches
3. An Additive Mixup at the input level to diversify training samples and reduce mixup operations

Overall, the authors' approach aims to address the challenges of action recognition by improving both temporal modeling and data diversity simultaneously.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: f3039396df37b00ce6db2e4a52276b84b61a2011a8481f40207ad55eef4e747e
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:10.894513'
category: 24-computing
---

arXiv:2509.14619v1 Announce Type: new Abstract: Skeleton-based action recognition faces two longstanding challenges: the scarcity of labeled training samples and difficulty modeling short- and long-range temporal dependencies. To address these issues, we propose a unified framework, LSTC-MDA, which simultaneously improves temporal modeling and data diversity. We introduce a novel Long-Short Term Temporal Convolution (LSTC) module with parallel short- and long-term branches, these two feature branches are then aligned and fused adaptively using learned similarity weights to preserve critical long-range cues lost by conventional stride-2 temporal convolutions. We also extend Joint Mixing Data Augmentation (JMDA) with an Additive Mixup at the input level, diversifying training samples and restricting mixup operations to the same camera view to avoid distribution shifts. Ablation studies confirm each component contributes. LSTC-MDA achieves state-of-the-art results: 94.1% and 97.5% on NTU ...