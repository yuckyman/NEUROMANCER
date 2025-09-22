---
title: 'DACoN: DINO for Anime Paint Bucket Colorization with Any Number of Reference
  Images'
link: https://arxiv.org/abs/2509.14685
summary: 'The article discusses a new framework called DACoN (Deep Auto-Colorization of Line Drawings) that addresses the challenges in automatic colorization of line drawings by leveraging foundation models to capture part-level semantics. The key features include:

1. **Multi-Reference Image Handling**: DACoN allows for any number of references, unlike previous methods that rely on a fixed set of images.

2. **Feature Fusion**: It combines low-resolution semantic features from foundation models with high-resolution spatial features from CNNs to improve feature extraction and colorization accuracy.

3. **Quantitative Evaluation**: The article provides quantitative evaluations using various metrics such as Mean Absolute Error (MAE) for colorization performance, which shows the benefits of using multiple reference images in DACoN.

4. **Qualitative Evaluation**: Qualitative evaluations demonstrate that DACoN achieves superior colorization performance compared to previous methods.

5. **Future Work**: The authors suggest further research on improving the model's robustness and handling occlusions, pose variations, and viewpoint changes.

Overall, DACoN aims to provide a more flexible and effective solution for automatic line drawing colorization by leveraging deep learning techniques and foundation models.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: ae13d64cb900d9c5baea057c760ccbede0c728fae525d379161ad039e1e1e6d1
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:10.746150'
category: 24-computing
---

arXiv:2509.14685v1 Announce Type: new Abstract: Automatic colorization of line drawings has been widely studied to reduce the labor cost of hand-drawn anime production. Deep learning approaches, including image/video generation and feature-based correspondence, have improved accuracy but struggle with occlusions, pose variations, and viewpoint changes. To address these challenges, we propose DACoN, a framework that leverages foundation models to capture part-level semantics, even in line drawings. Our method fuses low-resolution semantic features from foundation models with high-resolution spatial features from CNNs for fine-grained yet robust feature extraction. In contrast to previous methods that rely on the Multiplex Transformer and support only one or two reference images, DACoN removes this constraint, allowing any number of references. Quantitative and qualitative evaluations demonstrate the benefits of using multiple reference images, achieving superior colorization performance...