---
title: 'Not All Degradations Are Equal: A Targeted Feature Denoising Framework for
  Generalizable Image Super-Resolution'
link: https://arxiv.org/abs/2509.14841
summary: 'The article discusses the Generalizable Image Super-Resolution (GISR) method, which aims to enhance model generalization capabilities under unknown degradations. It introduces several approaches such as Dropout and Feature Alignment, but these methods assume that models overfit to all degradation types, including noise. The authors propose a targeted feature denoising framework called "Noise Detection and Denoising" (NDD) that can be seamlessly integrated with existing super-resolution techniques.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 43e910b6c40da490e74aeb316df609fbef38c74ec5429da74ca079261cb8831e
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:13.619897'
category: 24-computing
---

arXiv:2509.14841v1 Announce Type: new Abstract: Generalizable Image Super-Resolution aims to enhance model generalization capabilities under unknown degradations. To achieve this goal, the models are expected to focus only on image content-related features instead of overfitting degradations. Recently, numerous approaches such as Dropout and Feature Alignment have been proposed to suppress models' natural tendency to overfit degradations and yield promising results. Nevertheless, these works have assumed that models overfit to all degradation types (e.g., blur, noise, JPEG), while through careful investigations in this paper, we discover that models predominantly overfit to noise, largely attributable to its distinct degradation pattern compared to other degradation types. In this paper, we propose a targeted feature denoising framework, comprising noise detection and denoising modules. Our approach presents a general solution that can be seamlessly integrated with existing super-resol...