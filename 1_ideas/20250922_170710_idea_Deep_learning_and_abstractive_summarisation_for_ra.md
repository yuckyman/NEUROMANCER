---
title: 'Deep learning and abstractive summarisation for radiological reports: an empirical
  study for adapting the PEGASUS models'' family with scarce data'
link: https://arxiv.org/abs/2509.15419
summary: 'The article discusses the challenges in automated medical text summarization due to the sensitivity of sensitive domains like medicine. It proposes a method called fine-tuning for abstractive summarisation models and provides insights on how to avoid overfitting and underfitting. The authors used PEGASUS, a model family with a non-domain-specific encoder-decoder architecture, to investigate this issue in a radiological reports dataset. They evaluated the performance of the model across different checkpoints using lexical and semantic metrics during training on fixed-size validation sets.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 147fed7944b2209b34462f4adcf4eeada27f0166859a2c383fd9ae5b0d7cdd10
feed_title: cs.AI updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.AI
date_processed: '2025-09-22T17:07:10.176388'
category: 24-computing
---

arXiv:2509.15419v1 Announce Type: cross Abstract: Regardless of the rapid development of artificial intelligence, abstractive summarisation is still challenging for sensitive and data-restrictive domains like medicine. With the increasing number of imaging, the relevance of automated tools for complex medical text summarisation is expected to become highly relevant. In this paper, we investigated the adaptation via fine-tuning process of a non-domain-specific abstractive summarisation encoder-decoder model family, and gave insights to practitioners on how to avoid over- and underfitting. We used PEGASUS and PEGASUS-X, on a medium-sized radiological reports public dataset. For each model, we comprehensively evaluated two different checkpoints with varying sizes of the same training data. We monitored the models' performances with lexical and semantic metrics during the training history on the fixed-size validation set. PEGASUS exhibited different phases, which can be related to epoch-wi...