---
title: Synthetic-to-Real Object Detection using YOLOv11 and Domain Randomization Strategies
link: https://arxiv.org/abs/2509.15045
summary: 'This paper presents a method to train an object detection model using only synthetic data and domain randomization strategies. The authors conducted extensive experimentation with different types of synthetic data and dataset composition to evaluate the model's performance. They found that increasing synthetic dataset diversity, specifically by including varied perspectives and complex backgrounds, combined with carefully tuned data augmentation, was crucial in bridging the domain gap. The best performing model achieved a final mAP@50 score of 96%, which is considered excellent for this type of task.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 454f58eaafc0353fea5ebc048d002ef59e3113aad7883bea5c3697295bcae0e8
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:12.387306'
category: 24-computing
---

arXiv:2509.15045v1 Announce Type: new Abstract: This paper addresses the synthetic-to-real domain gap in object detection, focusing on training a YOLOv11 model to detect a specific object (a soup can) using only synthetic data and domain randomization strategies. The methodology involves extensive experimentation with data augmentation, dataset composition, and model scaling. While synthetic validation metrics were consistently high, they proved to be poor predictors of real-world performance. Consequently, models were also evaluated qualitatively, through visual inspection of predictions, and quantitatively, on a manually labeled real-world test set, to guide development. Final mAP@50 scores were provided by the official Kaggle competition. Key findings indicate that increasing synthetic dataset diversity, specifically by including varied perspectives and complex backgrounds, combined with carefully tuned data augmentation, were crucial in bridging the domain gap. The best performing ...