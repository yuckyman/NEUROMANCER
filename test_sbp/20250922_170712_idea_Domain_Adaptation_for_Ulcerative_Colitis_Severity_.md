---
title: Domain Adaptation for Ulcerative Colitis Severity Estimation Using Patient-Level
  Diagnoses
link: https://arxiv.org/abs/2509.14573
summary: 'The article discusses a novel weakly supervised domain adaptation method for estimating the severity of ulcerative colitis (UC). The authors propose a method called "Shared Aggregation Tokens" and a Max-Severity Triplet Loss, which aligns class-wise distributions across domains using patient-level diagnostic results. They demonstrate that this approach can be used to improve the accuracy of UC severity estimation in hospitals with varying imaging devices and clinical settings.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 8e48208c6656bb1f3774d0c9721a93abefc449799761e631e1fc509bec79ccc3
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:12.046962'
category: 24-computing
---

arXiv:2509.14573v1 Announce Type: new Abstract: The development of methods to estimate the severity of Ulcerative Colitis (UC) is of significant importance. However, these methods often suffer from domain shifts caused by differences in imaging devices and clinical settings across hospitals. Although several domain adaptation methods have been proposed to address domain shift, they still struggle with the lack of supervision in the target domain or the high cost of annotation. To overcome these challenges, we propose a novel Weakly Supervised Domain Adaptation method that leverages patient-level diagnostic results, which are routinely recorded in UC diagnosis, as weak supervision in the target domain. The proposed method aligns class-wise distributions across domains using Shared Aggregation Tokens and a Max-Severity Triplet Loss, which leverages the characteristic that patient-level diagnoses are determined by the most severe region within each patient. Experimental results demonstrat...