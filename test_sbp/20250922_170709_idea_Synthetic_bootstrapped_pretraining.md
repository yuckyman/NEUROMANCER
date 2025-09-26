---
title: Synthetic bootstrapped pretraining
link: https://arxiv.org/abs/2509.15248
summary: 'The article discusses Synthetic Bootstrapped Pretraining (SBP), a language model pretraining procedure that first learns a model of relations between documents from the pretraining dataset and then synthesizes a vast new corpus for joint training. The authors validate SBP by designing a compute-matched pretraining setup and pretrain a 3B-parameter model on up to 1T tokens from scratch, finding that it consistently improves upon a strong repetition baseline and delivers a significant fraction of performance improvement attainable by an oracle upper bound with access to 20x more unique data. The authors also provide qualitative analysis revealing that the synthesized documents go beyond mere paraphrases.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: df2c7f29834eebed1f2fe645adc0ea25158c0be4ed54d3698ab25dabc0daa256
feed_title: cs.AI updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.AI
date_processed: '2025-09-22T17:07:09.836813'
category: 24-computing
---

arXiv:2509.15248v1 Announce Type: cross Abstract: We introduce Synthetic Bootstrapped Pretraining (SBP), a language model (LM) pretraining procedure that first learns a model of relations between documents from the pretraining dataset and then leverages it to synthesize a vast new corpus for joint training. While the standard pretraining teaches LMs to learn causal correlations among tokens within a single document, it is not designed to efficiently model the rich, learnable inter-document correlations that can potentially lead to better performance. We validate SBP by designing a compute-matched pretraining setup and pretrain a 3B-parameter model on up to 1T tokens from scratch. We find SBP consistently improves upon a strong repetition baseline and delivers a significant fraction of performance improvement attainable by an oracle upper bound with access to 20x more unique data. Qualitative analysis reveals that the synthesized documents go beyond mere paraphrases -- SBP first abstrac...