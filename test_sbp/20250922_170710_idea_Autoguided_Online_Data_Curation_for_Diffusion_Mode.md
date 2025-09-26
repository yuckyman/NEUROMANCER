---
title: Autoguided Online Data Curation for Diffusion Model Training
link: https://arxiv.org/abs/2509.15267
summary: 'The article discusses the potential benefits of using recently developed autoguidance and online data selection methods for improving the efficiency of generative model training. Specifically, it compares these methods with traditional approaches to improve sample quality and diversity in image generation tasks.

Key points:

1. Autoguidance and online data selection are new methods that can help improve training efficiency.
2. The authors evaluate their effectiveness by comparing them with earlier methods (AJEST) on both synthetic data generation and 3D image generation tasks.
3. They find that autoguidance consistently improves sample quality and diversity, especially in terms of time efficiency compared to AJEST alone.
4. However, AJEST has a higher overhead due to its early application phase.

Overall, the article suggests that these new methods can help improve generative model training by reducing unnecessary processing steps and increasing sample quality.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 6153e894c4e7ee4a80f24aa79d00d2be74ae33c1b55a80c9cedae054d7a7a820
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:10.787262'
category: 24-computing
---

arXiv:2509.15267v1 Announce Type: new Abstract: The costs of generative model compute rekindled promises and hopes for efficient data curation. In this work, we investigate whether recently developed autoguidance and online data selection methods can improve the time and sample efficiency of training generative diffusion models. We integrate joint example selection (JEST) and autoguidance into a unified code base for fast ablation and benchmarking. We evaluate combinations of data curation on a controlled 2-D synthetic data generation task as well as (3x64x64)-D image generation. Our comparisons are made at equal wall-clock time and equal number of samples, explicitly accounting for the overhead of selection. Across experiments, autoguidance consistently improves sample quality and diversity. Early AJEST (applying selection only at the beginning of training) can match or modestly exceed autoguidance alone in data efficiency on both tasks. However, its time overhead and added complexity...