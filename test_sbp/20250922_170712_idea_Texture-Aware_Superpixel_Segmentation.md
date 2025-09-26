---
title: Texture-Aware Superpixel Segmentation
link: https://arxiv.org/abs/1901.11111
summary: 'The paper presents a new SuperPixel algorithm called Texture-Aware SuperPixel (TASP). The main idea is that most existing SuperPixel algorithms compute both spatial and color features at the pixel level. This can lead to problems when trying to group pixels with similar local texture properties, as they may need fine parameter tuning. TASP addresses this issue by automatically adjusting its spatial constraint based on the local feature variance of the pixels it segments. Additionally, TASP ensures that superpixels have a high degree of texture homogeneity by proposing a new pixel-to-superci patch-based distance metric. The results show that TASP outperforms state-of-the-art methods in both texture and natural color image datasets.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: beaa3d0c823503854f362a70969d01bfb0e2f8e7b1f8fc3b27044d15652ce403
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:12.582415'
category: 24-computing
---

arXiv:1901.11111v4 Announce Type: replace Abstract: Most superpixel algorithms compute a trade-off between spatial and color features at the pixel level. Hence, they may need fine parameter tuning to balance the two measures, and highly fail to group pixels with similar local texture properties. In this paper, we address these issues with a new Texture-Aware SuperPixel (TASP) method. To accurately segment textured and smooth areas, TASP automatically adjusts its spatial constraint according to the local feature variance. Then, to ensure texture homogeneity within superpixels, a new pixel to superpixel patch-based distance is proposed. TASP outperforms the segmentation accuracy of the state-of-the-art methods on texture and also natural color image datasets.