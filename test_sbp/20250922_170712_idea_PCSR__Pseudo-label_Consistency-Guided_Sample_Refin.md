---
title: 'PCSR: Pseudo-label Consistency-Guided Sample Refinement for Noisy Correspondence
  Learning'
link: https://arxiv.org/abs/2509.15623
summary: 'The article discusses cross-modal retrieval methods that aim to align different modalities via semantic similarity but often overlook Noisy Correspondences in real data. Previous methods rely on coarse-grained categorizations and uniform training strategies without considering the intrinsic diversity within noisy instances. The authors introduce a novel framework, called Pseudo-label Consistency-Guided Sample Refinement (PCSR), which enhances correspondence reliability by explicitly dividing samples based on pseudo-label consistency.

The article emphasizes that existing methods often assume perfectly aligned image-text pairs, overlooking Noisy Correspondences in real data. These misaligned pairs can degrade retrieval performance and lead to suboptimal model optimization when applied to noisy instances. The authors propose a novel framework called PCSR that addresses these challenges by dividing samples based on pseudo-label consistency.

The article discusses the limitations of previous methods, such as relying on coarse-grained categorizations or uniform training strategies without considering intrinsic diversity within noisy instances. The authors argue that this approach can lead to suboptimal model optimization and poor performance in real-world applications.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: bf0cd1d6bd131b4b0a70cb05d2a8614f930acf35f774975a40d6967a3b249329
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:12.025137'
category: 24-computing
---

arXiv:2509.15623v1 Announce Type: new Abstract: Cross-modal retrieval aims to align different modalities via semantic similarity. However, existing methods often assume that image-text pairs are perfectly aligned, overlooking Noisy Correspondences in real data. These misaligned pairs misguide similarity learning and degrade retrieval performance. Previous methods often rely on coarse-grained categorizations that simply divide data into clean and noisy samples, overlooking the intrinsic diversity within noisy instances. Moreover, they typically apply uniform training strategies regardless of sample characteristics, resulting in suboptimal sample utilization for model optimization. To address the above challenges, we introduce a novel framework, called Pseudo-label Consistency-Guided Sample Refinement (PCSR), which enhances correspondence reliability by explicitly dividing samples based on pseudo-label consistency. Specifically, we first employ a confidence-based estimation to distinguis...