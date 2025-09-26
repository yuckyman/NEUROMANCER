---
title: 'pFedSAM: Personalized Federated Learning of Segment Anything Model for Medical
  Image Segmentation'
link: https://arxiv.org/abs/2509.15638
summary: 'The article discusses a new federated learning framework called "Segment Anything Model" (SAM). SAM is designed for medical image segmentation, but it faces challenges due to its lightweight architecture. The authors present the first personalized federated SAM framework specifically tailored for heterogeneous data scenarios in medical image segmentation. Their approach involves two key innovations: an aggregated strategy that captures commonalities among clients while retaining the L-MoE component and a decoupled global-local fine-tuning mechanism. This framework aims to improve privacy constraints and enhance the performance of federated learning algorithms, particularly in healthcare applications where data sharing across institutions is crucial.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 4c5d1625d5d31b783199b748c7b3e8f394860759d7f8a5e72324bf3bced56674
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:10.029047'
category: 24-computing
---

arXiv:2509.15638v1 Announce Type: new Abstract: Medical image segmentation is crucial for computer-aided diagnosis, yet privacy constraints hinder data sharing across institutions. Federated learning addresses this limitation, but existing approaches often rely on lightweight architectures that struggle with complex, heterogeneous data. Recently, the Segment Anything Model (SAM) has shown outstanding segmentation capabilities; however, its massive encoder poses significant challenges in federated settings. In this work, we present the first personalized federated SAM framework tailored for heterogeneous data scenarios in medical image segmentation. Our framework integrates two key innovations: (1) a personalized strategy that aggregates only the global parameters to capture cross-client commonalities while retaining the designed L-MoE (Localized Mixture-of-Experts) component to preserve domain-specific features; and (2) a decoupled global-local fine-tuning mechanism that leverages a te...