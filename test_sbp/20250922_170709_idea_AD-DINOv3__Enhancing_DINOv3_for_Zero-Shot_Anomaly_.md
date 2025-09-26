---
title: 'AD-DINOv3: Enhancing DINOv3 for Zero-Shot Anomaly Detection with Anomaly-Aware
  Calibration'
link: https://arxiv.org/abs/2509.14084
summary: 'The article discusses ZSAD (Zero-Shot Anomaly Detection), an approach that aims to identify anomalies from novel categories without prior knowledge of the context or labels. Traditionally, most ZSAD works have relied on CLIP models, which calculate similarities between visual and text embeddings for anomaly detection. However, this model has limitations due to domain bias and inherent biases in pretrained representations.

To address these issues, the authors propose AD-DINOv3 (Adaptive DINOv3), a new version of DINOv3 that adapts the model's architecture and training process to work with ZSAD tasks. The key challenges addressed are:

1. Domain bias: Large-scale pretraining data often contains features from novel categories, leading to feature misalignment.
2. Global semantics bias: Pretrained representations tend to emphasize global semantics, which can lead to subtle anomalies being mistaken for normal foreground objects.

The authors propose an adaptive architecture that adjusts the model's parameters based on the specific anomaly detection task and the pretraining data. They also introduce a method called "adaptive DINOv3" to fine-tune the model during training, making it more efficient and effective in ZSAD tasks.

Overall, this work presents a promising solution for addressing the challenges of ZSAD by leveraging recent advancements in vision foundation models like DINOv3.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: b3768625694995ca4a29fb03b646311c0dc4684c702e72c1db339b286ff17e30
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:09.790844'
category: 24-computing
---

arXiv:2509.14084v1 Announce Type: new Abstract: Zero-Shot Anomaly Detection (ZSAD) seeks to identify anomalies from arbitrary novel categories, offering a scalable and annotation-efficient solution. Traditionally, most ZSAD works have been based on the CLIP model, which performs anomaly detection by calculating the similarity between visual and text embeddings. Recently, vision foundation models such as DINOv3 have demonstrated strong transferable representation capabilities. In this work, we are the first to adapt DINOv3 for ZSAD. However, this adaptation presents two key challenges: (i) the domain bias between large-scale pretraining data and anomaly detection tasks leads to feature misalignment; and (ii) the inherent bias toward global semantics in pretrained representations often leads to subtle anomalies being misinterpreted as part of the normal foreground objects, rather than being distinguished as abnormal regions. To overcome these challenges, we introduce AD-DINOv3, a novel v...