---
title: Large Vision Models Can Solve Mental Rotation Problems
link: https://arxiv.org/abs/2509.15271
summary: 'The article discusses a systematic evaluation of different vision transformers (ViT), CLIP, DINOv2, and DINOv3 for mental-rotation tasks. It compares their performance across various block structures, including simple block structures used by Shepard and Metzler to study human cognition, more complex block figures, text representations, and photo-realistic objects. The evaluation shows that ViT models perform better in capturing geometric structure compared to supervised models. Additionally, the paper suggests that model representations are layer-by-layer processed, with intermediate layers performing better than final ones as task difficulty increases.

The article highlights the importance of mental-rotation tasks for understanding how vision transformers develop similar abilities and provides a comprehensive evaluation of their performance across different block structures.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: c1e81e344c409aa1e8c1ddfadfeb0c1dbfacccf14a0adccc568194fe57ef31c8
feed_title: cs.AI updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.AI
date_processed: '2025-09-22T17:07:12.539351'
category: 24-computing
---

arXiv:2509.15271v1 Announce Type: cross Abstract: Mental rotation is a key test of spatial reasoning in humans and has been central to understanding how perception supports cognition. Despite the success of modern vision transformers, it is still unclear how well these models develop similar abilities. In this work, we present a systematic evaluation of ViT, CLIP, DINOv2, and DINOv3 across a range of mental-rotation tasks, from simple block structures similar to those used by Shepard and Metzler to study human cognition, to more complex block figures, three types of text, and photo-realistic objects. By probing model representations layer by layer, we examine where and how these networks succeed. We find that i) self-supervised ViTs capture geometric structure better than supervised ViTs; ii) intermediate layers perform better than final layers; iii) task difficulty increases with rotation complexity and occlusion, mirroring human reaction times and suggesting similar constraints in em...