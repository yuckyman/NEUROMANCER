---
title: Bidirectional dynamic threshold SNN for enhanced object detection with rich
  spike information
link: https://www.frontiersin.org/articles/10.3389/fnins.2025.1661916
summary: 'The article discusses a new type of neural network called Directly Trained SNN (BD-SNN) that is inspired by neuroscience principles and has shown promising results in object detection tasks. The key features of BD-SNN include:

1. It uses Bidirectional Dynamic Threshold neurons (BD-LIF) for information encoding.
2. It incorporates two new all-spike residual blocks, BD-Block1 and BD-Block2.
3. These blocks enhance the network's efficiency by dynamically adjusting thresholds and improving information extraction.

The article compares BD-SNN with state-of-the-art methods like EMS-YOLO, showing that it outperforms them in accuracy across diverse datasets. The results are validated through experiments on COCO and Gen1 datasets.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: ce1943195b2d57fe5fb1a37fe265d5bcb1fc54821ee3b8dd6d07b0ba1dd149b5
feed_title: Frontiers in Neuroscience | New and Recent Articles
feed_url: https://www.frontiersin.org/journals/neuroscience/rss
date_processed: '2025-09-22T17:07:10.685649'
category: 24-computing
---

Spiking Neural Networks (SNNs), inspired by neuroscience principles, have gained attention for their energy efficiency. However, directly trained SNNs lag behind Artificial Neural Networks (ANNs) in accuracy for complex tasks like object detection due to the limited information capacity of binary spike feature maps. To address this, we propose BD-SNN, a new directly trained SNN equipped with Bidirectional Dynamic Threshold neurons (BD-LIF). BD-LIF neurons emit +1 and –1 spikes and dynamically adjust their thresholds, enhancing the network's information encoding capacity and activation efficiency. Our BD-SNN incorporates two new all-spike residual blocks, BD-Block1 and BD-Block2, for efficient information extraction and multi-scale feature fusion, respectively. Experiments on the COCO and Gen1 datasets demonstrate that BD-SNN improves accuracy by 3.1% and 2.8% compared to the state-of-the-art EMS-YOLO method, respectively, validating BD-SNN's superior performance across diverse input sc...