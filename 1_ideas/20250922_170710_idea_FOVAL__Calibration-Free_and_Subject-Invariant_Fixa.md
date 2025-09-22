---
title: 'FOVAL: Calibration-Free and Subject-Invariant Fixation Depth Estimation Across
  Diverse Eye-Tracking Datasets'
link: https://arxiv.org/abs/2408.03591
summary: 'The article discusses the development of FOVAL, an approach that combines spatiotemporal sequence modelling via Long Short-Term Memory (LSTM) networks with subject-invariant feature engineering and normalisation to estimate fixation depth in extended reality (XR), robotics, and human-computer interaction applications. The method is described as robust and scalable, achieving superior performance compared to existing methods such as Transformers, Temporal Convolutional Networks (TCNs), and CNNs.

The article provides a detailed analysis of the FOVAL approach, including its strengths and limitations. It compares FOVAL with other models in terms of accuracy, particularly in scenarios with limited and noisy gaze data. The results are validated using three benchmark datasets, and the method is further analyzed for inter-subject variability and domain shifts to provide insights into model robustness.

Overall, the article highlights the potential of FOVAL as a reliable and scalable solution for accurate fixation depth estimation in XR applications.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 5314edd7f28d98d8e1b80820f875ad269c78d27411660a42d5596f2bb8d04b8d
feed_title: cs.HC updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.HC
date_processed: '2025-09-22T17:07:10.385902'
category: 24-computing
---

arXiv:2408.03591v2 Announce Type: replace-cross Abstract: Accurate fixation depth estimation is essential for applications in extended reality (XR), robotics, and human-computer interaction. However, current methods heavily depend on user-specific calibration, which limits their scalability and usability. We introduce FOVAL, a robust calibration-free approach that combines spatiotemporal sequence modelling via Long Short-Term Memory (LSTM) networks with subject-invariant feature engineering and normalisation. Compared to Transformers, Temporal Convolutional Networks (TCNs), and CNNs, FOVAL achieves superior performance, particularly in scenarios with limited and noisy gaze data. Evaluations across three benchmark datasets using Leave-One-Out Cross-Validation (LOOCV) and cross-dataset validation show a mean absolute error (MAE) of 9.1 cm and strong generalisation without calibration. We further analyse inter-subject variability and domain shifts, providing insight into model robustness ...