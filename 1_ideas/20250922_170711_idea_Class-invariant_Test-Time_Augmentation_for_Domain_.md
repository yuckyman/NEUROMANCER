---
title: Class-invariant Test-Time Augmentation for Domain Generalization
link: https://arxiv.org/abs/2509.14420
summary: 'The article discusses a new approach to domain generalization (DG) in deep learning called Class-Invariant Test-Time Augmentation (CI-TTA). CI-TTA is an alternative method that generates multiple variants of each input image through elastic and grid deformations, while still belonging to the same class as the original input. The authors compare CI-TTA with other DG methods on two datasets: PACS and Office-Home. They find that CI-TTA achieves consistent gains across different DG algorithms and backbacks.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: cf7d29d4a122ab45e051ae10e0347221efd918a5a203c6e1563c97612d58bbb8
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:11.598863'
category: 24-computing
---

arXiv:2509.14420v1 Announce Type: new Abstract: Deep models often suffer significant performance degradation under distribution shifts. Domain generalization (DG) seeks to mitigate this challenge by enabling models to generalize to unseen domains. Most prior approaches rely on multi-domain training or computationally intensive test-time adaptation. In contrast, we propose a complementary strategy: lightweight test-time augmentation. Specifically, we develop a novel Class-Invariant Test-Time Augmentation (CI-TTA) technique. The idea is to generate multiple variants of each input image through elastic and grid deformations that nevertheless belong to the same class as the original input. Their predictions are aggregated through a confidence-guided filtering scheme that remove unreliable outputs, ensuring the final decision relies on consistent and trustworthy cues. Extensive Experiments on PACS and Office-Home datasets demonstrate consistent gains across different DG algorithms and backb...