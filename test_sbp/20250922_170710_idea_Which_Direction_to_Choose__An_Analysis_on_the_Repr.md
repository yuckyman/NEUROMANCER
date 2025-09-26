---
title: Which Direction to Choose? An Analysis on the Representation Power of Self-Supervised
  ViTs in Downstream Tasks
link: https://arxiv.org/abs/2509.15272
summary: 'The article discusses self-supervised learning (SSL) for vision transformers (ViTs), a technique that has shown promising results in pre-training tasks like image classification and segmentation. The key points are:

1. SSL techniques have been effective in recent years for computer vision tasks, including image classification and segmentation.

2. Two main objectives dominate SSL research: Contrastive Learning and Masked Image Modeling.

3. Features extracted from the final transformer attention block (keys, queries, values) as well as those obtained after the feed-forward layer are commonly used to address downstream tasks.

4. However, existing approaches often process these features through additional transformation layers, such as lightweight heads or combined with distillation, to achieve better task performance.

5. These methods can improve task outcomes but may not always be more effective than traditional approaches that directly use the ViT features without any transformations.

The article emphasizes the importance of maintaining a balance between using modern techniques and preserving the core capabilities of ViTs for downstream tasks.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: e2e6e001c70090c4d7ebd4acb7fb03d68705b68ef13fa810f77114ebb083f466
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:10.305065'
category: 24-computing
---

arXiv:2509.15272v1 Announce Type: new Abstract: Self-Supervised Learning (SSL) for Vision Transformers (ViTs) has recently demonstrated considerable potential as a pre-training strategy for a variety of computer vision tasks, including image classification and segmentation, both in standard and few-shot downstream contexts. Two pre-training objectives dominate the landscape of SSL techniques: Contrastive Learning and Masked Image Modeling. Features (or tokens) extracted from the final transformer attention block -- specifically, the keys, queries, and values -- as well as features obtained after the final block's feed-forward layer, have become a common foundation for addressing downstream tasks. However, in many existing approaches, these pre-trained ViT features are further processed through additional transformation layers, often involving lightweight heads or combined with distillation, to achieve superior task performance. Although such methods can improve task outcomes, to the be...