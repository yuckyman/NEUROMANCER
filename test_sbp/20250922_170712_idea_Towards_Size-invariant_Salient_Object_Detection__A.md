---
title: 'Towards Size-invariant Salient Object Detection: A Generic Evaluation and
  Optimization Approach'
link: https://arxiv.org/abs/2509.15573
summary: 'The paper discusses an issue in salient object detection (SOD) where evaluation protocols for multiple salient objects of significantly different sizes within the same image can be biased due to their size-invariance property. The authors propose a novel perspective on this problem by showing that the evaluation outcome of an image under current SOD metrics is decomposed into several separable terms, with each term's contribution directly proportional to its corresponding region size. This decomposition helps in understanding how different regions within the image contribute to the overall prediction errors and can lead to biased performance assessments and practical degradation.

To address this challenge, a generic Size-Invariant (SII) evaluation protocol is proposed that considers all salient objects of the same size as a single entity, rather than treating each object separately. This approach aims to ensure that the evaluation protocols are unbiased and provide a fair assessment of the overall performance of SOD algorithms on images with multiple salient objects of significantly different sizes.'
tags:
- unclassified
content_hash: 4eaa39407402d4a7f8f502468efef22d58c0fb90431c2f41d10d08a612ee3075
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:12.620327'
---

arXiv:2509.15573v1 Announce Type: new Abstract: This paper investigates a fundamental yet underexplored issue in Salient Object Detection (SOD): the size-invariant property for evaluation protocols, particularly in scenarios when multiple salient objects of significantly different sizes appear within a single image. We first present a novel perspective to expose the inherent size sensitivity of existing widely used SOD metrics. Through careful theoretical derivations, we show that the evaluation outcome of an image under current SOD metrics can be essentially decomposed into a sum of several separable terms, with the contribution of each term being directly proportional to its corresponding region size. Consequently, the prediction errors would be dominated by the larger regions, while smaller yet potentially more semantically important objects are often overlooked, leading to biased performance assessments and practical degradation. To address this challenge, a generic Size-Invariant ...