---
title: 'MS-GS: Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild'
link: https://arxiv.org/abs/2509.15548
summary: 'In this paper, the authors present a novel framework called MS-GS (Multi-View Sparse-3D Geometry Segmentation) that addresses the challenges of in-the-wild photo collections with limited volumes and multiple appearances. The key to their approach is to use 3D Gaussian Splatting (3DGS), which can handle sparse initializations, but it tends to oversmooth and overfit. To improve these issues, they propose a new framework called MS-GS that uses structured motion (SfM) points for reliable alignment and geometry cues. Additionally, the authors introduce multi-view constraints using local semantic regions with a Structure-from-Motion (SfM) algorithm.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: ef341f85cd55ce74f81f5708f826e90a0e1e666ae8f0f25fb00aaf270eef988a
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:12.852524'
category: 24-computing
---

arXiv:2509.15548v1 Announce Type: new Abstract: In-the-wild photo collections often contain limited volumes of imagery and exhibit multiple appearances, e.g., taken at different times of day or seasons, posing significant challenges to scene reconstruction and novel view synthesis. Although recent adaptations of Neural Radiance Field (NeRF) and 3D Gaussian Splatting (3DGS) have improved in these areas, they tend to oversmooth and are prone to overfitting. In this paper, we present MS-GS, a novel framework designed with Multi-appearance capabilities in Sparse-view scenarios using 3DGS. To address the lack of support due to sparse initializations, our approach is built on the geometric priors elicited from monocular depth estimations. The key lies in extracting and utilizing local semantic regions with a Structure-from-Motion (SfM) points anchored algorithm for reliable alignment and geometry cues. Then, to introduce multi-view constraints, we propose a series of geometry-guided supervis...