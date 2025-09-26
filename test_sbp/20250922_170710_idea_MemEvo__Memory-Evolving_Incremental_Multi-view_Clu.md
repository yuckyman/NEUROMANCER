---
title: 'MemEvo: Memory-Evolving Incremental Multi-view Clustering'
link: https://arxiv.org/abs/2509.14544
summary: 'The article discusses an incremental multi-view clustering algorithm called "MemEvo," which aims to achieve stable clustering results while addressing the stability-plasticity dilemma (SPD). The SPD is characterized by the model's need for enough plasticity to adapt to new data, but it must also maintain sufficient stability to prevent catastrophic forgetting. Inspired by the hippocampal-prefrontal cortex collaborative memory mechanism in neuroscience, the authors propose a method called "MemEvo" that balances these requirements.

The key components of MemEvo include:
1. A view alignment module that captures gain information from new views.
2. A cognitive forgetting mechanism that simulates decay patterns of human memory to modulate weights.
3. A prefrontal cortex-inspired knowledge representation system.

The authors also propose a method called "Incremental Multi-view Clustering" (IMVC) which is an extension of the original incremental multi-view clustering algorithm, aiming to achieve stable clustering results while addressing SPD in incremental views.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 2894877499e391d4d5064580cdf4373994ff95f8f67d4df229901e1309989bc4
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:10.611472'
category: 24-computing
---

arXiv:2509.14544v1 Announce Type: new Abstract: Incremental multi-view clustering aims to achieve stable clustering results while addressing the stability-plasticity dilemma (SPD) in incremental views. At the core of SPD is the challenge that the model must have enough plasticity to quickly adapt to new data, while maintaining sufficient stability to consolidate long-term knowledge and prevent catastrophic forgetting. Inspired by the hippocampal-prefrontal cortex collaborative memory mechanism in neuroscience, we propose a Memory-Evolving Incremental Multi-view Clustering method (MemEvo) to achieve this balance. First, we propose a hippocampus-inspired view alignment module that captures the gain information of new views by aligning structures in continuous representations. Second, we introduce a cognitive forgetting mechanism that simulates the decay patterns of human memory to modulate the weights of historical knowledge. Additionally, we design a prefrontal cortex-inspired knowledge...