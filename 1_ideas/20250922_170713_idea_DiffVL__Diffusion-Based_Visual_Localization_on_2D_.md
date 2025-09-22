---
title: 'DiffVL: Diffusion-Based Visual Localization on 2D Maps via BEV-Conditioned
  GPS Denoising'
link: https://arxiv.org/abs/2509.14565
summary: 'This article discusses a new framework called DiffVL for accurate visual localization in autonomous driving systems. The key idea behind DiffVL is to reformulate the problem of visual localization as a GPS denoising task using diffusion models. DiffVL focuses on the noisy GPS trajectory, which can be recovered through iterative diffusion refinement. Unlike previous methods that only focus on high-definition maps, DiffVL aims to address the issue of urban environments with multipath errors and noisy GPS signals. The framework is based on diffusion models and uses visual BEV features and SD maps as input data.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 55e718882a6796835867ff519fbd6f1b386a33e74b37ad7fb7ea366fbf193044
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:13.170934'
category: 24-computing
---

arXiv:2509.14565v1 Announce Type: new Abstract: Accurate visual localization is crucial for autonomous driving, yet existing methods face a fundamental dilemma: While high-definition (HD) maps provide high-precision localization references, their costly construction and maintenance hinder scalability, which drives research toward standard-definition (SD) maps like OpenStreetMap. Current SD-map-based approaches primarily focus on Bird's-Eye View (BEV) matching between images and maps, overlooking a ubiquitous signal-noisy GPS. Although GPS is readily available, it suffers from multipath errors in urban environments. We propose DiffVL, the first framework to reformulate visual localization as a GPS denoising task using diffusion models. Our key insight is that noisy GPS trajectory, when conditioned on visual BEV features and SD maps, implicitly encode the true pose distribution, which can be recovered through iterative diffusion refinement. DiffVL, unlike prior BEV-matching methods (e.g....