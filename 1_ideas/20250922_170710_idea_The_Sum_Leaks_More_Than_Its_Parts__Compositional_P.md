---
title: 'The Sum Leaks More Than Its Parts: Compositional Privacy Risks and Mitigations
  in Multi-Agent Collaboration'
link: https://arxiv.org/abs/2509.14284
summary: 'The article discusses the concept of compositional privacy leakage in multi-agent systems using large language models. It proposes two defense strategies for mitigating this risk:

1. **Theory-of-Mind Defense (ToM)**: This strategy involves defender agents anticipating how their responses might be exploited by adversaries, allowing them to detect and mitigate potential privacy risks.

2. **Collaborative Consensus Defense (CoDef)**: Defender agents collaborate with each other to ensure that the collective output of multiple agents is consistent and reliable, thereby reducing the risk of compositional privacy leakage.

The article highlights the importance of understanding how LLMs interact with their environment and the potential for these interactions to lead to privacy risks. It also suggests a way to address these risks by incorporating defensive mechanisms into the system design.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 33ce6c31b942923d858649b136ad9c236f1c80503df50d4703565f7208b0fbc6
feed_title: cs.AI updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.AI
date_processed: '2025-09-22T17:07:10.740614'
category: 24-computing
---

arXiv:2509.14284v1 Announce Type: cross Abstract: As large language models (LLMs) become integral to multi-agent systems, new privacy risks emerge that extend beyond memorization, direct inference, or single-turn evaluations. In particular, seemingly innocuous responses, when composed across interactions, can cumulatively enable adversaries to recover sensitive information, a phenomenon we term compositional privacy leakage. We present the first systematic study of such compositional privacy leaks and possible mitigation methods in multi-agent LLM systems. First, we develop a framework that models how auxiliary knowledge and agent interactions jointly amplify privacy risks, even when each response is benign in isolation. Next, to mitigate this, we propose and evaluate two defense strategies: (1) Theory-of-Mind defense (ToM), where defender agents infer a questioner's intent by anticipating how their outputs may be exploited by adversaries, and (2) Collaborative Consensus Defense (CoDef...