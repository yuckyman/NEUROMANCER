---
title: 'CCrepairBench: A High-Fidelity Benchmark and Reinforcement Learning Framework
  for C++ Compilation Repair'
link: https://arxiv.org/abs/2509.15690
summary: 'The article discusses the challenge of automated repair for C++ compilation errors and presents a new approach to resolve these issues using large-scale datasets. The authors introduce a novel dataset called CCrepair that is constructed through a sophisticated pipeline, which they argue can generate semantically correct patches. They also propose a Reinforcement Learning (RL) paradigm guided by a hybrid reward signal, shifting the focus from mere compilability to the semantic quality of the fix. Finally, they establish a robust evaluation system centered on an LLM-as-a-Judge whose reliability has been rigorously validated. The authors argue that their approach can help developers produce more accurate and reliable fixes for C++ compilation errors.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: f73dd698c0443464abb7298273865c979e8e20e985ac44a1d47b20e85b465046
feed_title: cs.AI updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.AI
date_processed: '2025-09-22T17:07:10.614958'
category: 24-computing
---

arXiv:2509.15690v1 Announce Type: new Abstract: The automated repair of C++ compilation errors presents a significant challenge, the resolution of which is critical for developer productivity. Progress in this domain is constrained by two primary factors: the scarcity of large-scale, high-fidelity datasets and the limitations of conventional supervised methods, which often fail to generate semantically correct patches.This paper addresses these gaps by introducing a comprehensive framework with three core contributions. First, we present CCrepair, a novel, large-scale C++ compilation error dataset constructed through a sophisticated generate-and-verify pipeline. Second, we propose a Reinforcement Learning (RL) paradigm guided by a hybrid reward signal, shifting the focus from mere compilability to the semantic quality of the fix. Finally, we establish the robust, two-stage evaluation system providing this signal, centered on an LLM-as-a-Judge whose reliability has been rigorously valid...