---
title: 'Enhancing Sa2VA for Referent Video Object Segmentation: 2nd Solution for 7th
  LSVOS RVOS Track'
link: https://arxiv.org/abs/2509.15546
summary: 'The article discusses a new type of video object segmentation (RVOS) method that combines large language models with semantic information to improve the accuracy of video object detection and segmentation. The authors present a training-free framework called RVOS-2 that significantly enhances Sa2VA's performance on this task, achieving an F1 score of 64.14% on MeViS test set. The key components of their method are a Video-Language Checker to identify matches between the query and video content and a Key-Frame Sampler to adaptively select informative frames for better object detection and segmentation.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: f31dec6e8f5177087051594ceffa48b9e87ef4ea431ffc39760b3aeed3a689b9
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:10.191968'
category: 24-computing
---

arXiv:2509.15546v1 Announce Type: new Abstract: Referential Video Object Segmentation (RVOS) aims to segment all objects in a video that match a given natural language description, bridging the gap between vision and language understanding. Recent work, such as Sa2VA, combines Large Language Models (LLMs) with SAM~2, leveraging the strong video reasoning capability of LLMs to guide video segmentation. In this work, we present a training-free framework that substantially improves Sa2VA's performance on the RVOS task. Our method introduces two key components: (1) a Video-Language Checker that explicitly verifies whether the subject and action described in the query actually appear in the video, thereby reducing false positives; and (2) a Key-Frame Sampler that adaptively selects informative frames to better capture both early object appearances and long-range temporal context. Without any additional training, our approach achieves a J&amp;F score of 64.14% on the MeViS test set, ranking ...