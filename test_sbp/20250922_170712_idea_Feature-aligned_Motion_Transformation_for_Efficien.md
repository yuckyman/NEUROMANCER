---
title: Feature-aligned Motion Transformation for Efficient Dynamic Point Cloud Compression
link: https://arxiv.org/abs/2509.14591
summary: 'The article discusses the development of a new method called Feature-aligned Motion Transformation (FMT) for dynamic point clouds in applications like immersive reality and robotics. FMT replaces explicit motion vectors with a spatiotemporal alignment strategy, which implicitly models continuous temporal variations using aligned features. The authors also introduce a random access (RA) reference strategy that enables bidirectional motion referencing between the original and transformed data.

Key points:
1. Dynamic point clouds are used in various applications.
2. Efficient compression depends on accurate motion estimation and compensation.
3. Current methods often rely on explicit motion vectors, which struggle to capture dynamics and fail to exploit temporal correlations.
4. FMT addresses these challenges by replacing explicit motion vectors with a spatiotemporal alignment strategy that models continuous temporal variations using aligned features.
5. The authors also introduce a random access (RA) reference strategy that enables bidirectional motion referencing between the original and transformed data.

The main contribution of this work is the introduction of FMT, which provides a more effective method for dynamic point cloud compression by leveraging spatiotemporal alignment strategies and random access mechanisms.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 59c2b2c2f5738c30f8e32aa3a5c40619048f228219c4c9a5b154871a2aed7dc8
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:12.806654'
category: 24-computing
---

arXiv:2509.14591v1 Announce Type: new Abstract: Dynamic point clouds are widely used in applications such as immersive reality, robotics, and autonomous driving. Efficient compression largely depends on accurate motion estimation and compensation, yet the irregular structure and significant local variations of point clouds make this task highly challenging. Current methods often rely on explicit motion estimation, whose encoded vectors struggle to capture intricate dynamics and fail to fully exploit temporal correlations. To overcome these limitations, we introduce a Feature-aligned Motion Transformation (FMT) framework for dynamic point cloud compression. FMT replaces explicit motion vectors with a spatiotemporal alignment strategy that implicitly models continuous temporal variations, using aligned features as temporal context within a latent-space conditional encoding framework. Furthermore, we design a random access (RA) reference strategy that enables bidirectional motion referenc...