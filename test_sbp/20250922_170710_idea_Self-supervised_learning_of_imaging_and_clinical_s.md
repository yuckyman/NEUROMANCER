---
title: Self-supervised learning of imaging and clinical signatures using a multimodal
  joint-embedding predictive architecture
link: https://arxiv.org/abs/2509.15470
summary: 'The article discusses the development of a new type of multimodal model for pulmonary nodule diagnosis, called Joint Embedding Predictive Architecture (JEPA). The authors use self-supervised learning from longitudinal and multimodal archives to address the challenges of limited labeled data and overfitting on the training distribution. They curate an unlabeled set of patients with CT scans and linked electronic health records from their home institution to power joint embedding predictive architecture (JEPA) pretraining. After supervised finetuning, they show that their approach outperforms a regularized multimodal model and imaging-only model in an internal cohort but underperforms in an external cohort.

The article also discusses the development of a synthetic environment that characterizes the context in which JEPA may underperform. This work innovates an approach that leverages unlabeled multimodal medical archives to improve the performance of the JEPA model.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 94427e5ecfc8310114c214432dcbe89df10947a340bdc2b1f475d1d3df54095b
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:10.988970'
category: 24-computing
---

arXiv:2509.15470v1 Announce Type: new Abstract: The development of multimodal models for pulmonary nodule diagnosis is limited by the scarcity of labeled data and the tendency for these models to overfit on the training distribution. In this work, we leverage self-supervised learning from longitudinal and multimodal archives to address these challenges. We curate an unlabeled set of patients with CT scans and linked electronic health records from our home institution to power joint embedding predictive architecture (JEPA) pretraining. After supervised finetuning, we show that our approach outperforms an unregularized multimodal model and imaging-only model in an internal cohort (ours: 0.91, multimodal: 0.88, imaging-only: 0.73 AUC), but underperforms in an external cohort (ours: 0.72, imaging-only: 0.75 AUC). We develop a synthetic environment that characterizes the context in which JEPA may underperform. This work innovates an approach that leverages unlabeled multimodal medical archi...