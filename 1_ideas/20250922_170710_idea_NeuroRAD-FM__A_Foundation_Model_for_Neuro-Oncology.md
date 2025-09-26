---
title: 'NeuroRAD-FM: A Foundation Model for Neuro-Oncology with Distributionally Robust
  Training'
link: https://arxiv.org/abs/2509.15416
summary: 'The article discusses a new neuro-oncology specific machine learning model called DRO-MG. The authors developed this model to address the challenges of heterogeneous data and tumor complexity in neuro-oncology research. They used a distributionally robust loss function, self-supervised backbones (BYOL, DINO, MAE, MoCo), and distributed optimization techniques to improve generalization across institutions. The model was pretrained on multi-institutional brain tumor MRI data and applied DRO to mitigate site and class imbalance in the training set. The authors demonstrated that the new model outperforms existing FMs in predicting uncommon molecular markers and improving survival prediction.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 8001522a70e268a73096b9395cecbdd8ca8132f9a350ecc5a933f169ed7af882
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:10.949626'
category: 24-computing
---

arXiv:2509.15416v1 Announce Type: new Abstract: Neuro-oncology poses unique challenges for machine learning due to heterogeneous data and tumor complexity, limiting the ability of foundation models (FMs) to generalize across cohorts. Existing FMs also perform poorly in predicting uncommon molecular markers, which are essential for treatment response and risk stratification. To address these gaps, we developed a neuro-oncology specific FM with a distributionally robust loss function, enabling accurate estimation of tumor phenotypes while maintaining cross-institution generalization. We pretrained self-supervised backbones (BYOL, DINO, MAE, MoCo) on multi-institutional brain tumor MRI and applied distributionally robust optimization (DRO) to mitigate site and class imbalance. Downstream tasks included molecular classification of common markers (MGMT, IDH1, 1p/19q, EGFR), uncommon alterations (ATRX, TP53, CDKN2A/2B, TERT), continuous markers (Ki-67, TP53), and overall survival prediction ...