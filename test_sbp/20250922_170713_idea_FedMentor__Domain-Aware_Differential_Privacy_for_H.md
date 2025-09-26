---
title: 'FedMentor: Domain-Aware Differential Privacy for Heterogeneous Federated LLMs
  in Mental Health'
link: https://arxiv.org/abs/2509.14275
summary: 'The article discusses a federated fine-tuning framework called FedMentor that integrates Low-Rank Adaptation (LoRA) and domain-aware Differential Privacy (DP) to meet per-domain privacy budgets while maintaining performance. Each client applies a custom DP noise scale proportional to its data sensitivity, and the server reduces noise when utility falls below a threshold. The authors evaluate FedMentor on three mental health datasets and show that it improves safety over standard Federated Learning without privacy by up to 3 points and lowers toxicity, while maintaining utility within 0.5% of the non-private baseline and close to the centralized upper bound.

Key takeaways:

1. FedMentor is a federated fine-tuning framework for Large Language Models (LLMs) in sensitive domains.
2. It integrates Low-Rank Adaptation (LoRA) and domain-aware Differential Privacy (DP).
3. Each client applies a custom DP noise scale proportional to its data sensitivity, and the server reduces noise when utility falls below a threshold.
4. The authors evaluate FedMentor on three mental health datasets and show that it improves safety over standard Federated Learning without privacy by up to 3 points and lowers toxicity, while maintaining utility within 0.5% of the non-private baseline and close to the centralized upper bound.

The framework scales to backbones with up to 1.7B pa.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 2741acb8ef7c85c189bcad5de48aae4042552dfc8f2c482f87d0d845ea9e19c8
feed_title: cs.AI updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.AI
date_processed: '2025-09-22T17:07:13.071016'
category: 24-computing
---

arXiv:2509.14275v1 Announce Type: cross Abstract: Privacy-preserving adaptation of Large Language Models (LLMs) in sensitive domains (e.g., mental health) requires balancing strict confidentiality with model utility and safety. We propose FedMentor, a federated fine-tuning framework that integrates Low-Rank Adaptation (LoRA) and domain-aware Differential Privacy (DP) to meet per-domain privacy budgets while maintaining performance. Each client (domain) applies a custom DP noise scale proportional to its data sensitivity, and the server adaptively reduces noise when utility falls below a threshold. In experiments on three mental health datasets, we show that FedMentor improves safety over standard Federated Learning without privacy, raising safe output rates by up to three points and lowering toxicity, while maintaining utility (BERTScore F1 and ROUGE-L) within 0.5% of the non-private baseline and close to the centralized upper bound. The framework scales to backbones with up to 1.7B pa...