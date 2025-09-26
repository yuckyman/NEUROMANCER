---
title: 'The NazoNazo Benchmark: A Cost-Effective and Extensible Test of Insight-Based
  Reasoning in LLMs'
link: https://arxiv.org/abs/2509.14704
summary: 'The article discusses a new benchmark called Nazonazo, which is built from Japanese children's riddles to evaluate insight-based reasoning. The authors present results on 120 riddles and compare 38 frontier models with 126 adults. They find that the model that performs best is GPT-5, which achieves an accuracy of 52.9%. However, they also note that there are some limitations to this benchmark, such as its cost-effectiveness and extensibility. The article concludes by discussing the potential for using Nazonazo in other contexts and highlighting the importance of transparency and accountability in machine learning evaluation systems.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: d148b5349ab71877f3e55d6f93cd0af6daaf592630b80370be5b75b72297997f
feed_title: cs.AI updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.AI
date_processed: '2025-09-22T17:07:13.037589'
category: 24-computing
---

arXiv:2509.14704v1 Announce Type: new Abstract: Benchmark saturation and contamination undermine confidence in LLM evaluation. We present Nazonazo, a cost-effective and extensible benchmark built from Japanese children's riddles to test insight-based reasoning. Items are short (mostly one sentence), require no specialized domain knowledge, and can be generated at scale, enabling rapid refresh of blind sets when leakage is suspected. We evaluate 38 frontier models and 126 adults on 120 riddles. No model except for GPT-5 is comparable to human performance, which achieves a 52.9% mean accuracy. Model comparison on extended 201 items shows that reasoning models significantly outperform non-reasoning peers, while model size shows no reliable association with accuracy. Beyond aggregate accuracy, an informal candidate-tracking analysis of thought logs reveals many cases of verification failure: models often produce the correct solution among intermediate candidates yet fail to select it as th...