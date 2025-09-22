---
title: Backdoor Mitigation via Invertible Pruning Masks
link: https://arxiv.org/abs/2509.15497
summary: 'The paper presents a novel approach for pruning neural networks, focusing on identifying critical parameters responsible for inducing backdoor behaviors in deep learning models. The authors propose a method called "pruning-based fine-tuning" (PFT) that leverages the advantages of both fine-tuning and pruning techniques. PFT involves two main components:

1. A selection mechanism to identify parameters essential for the main task but not necessarily beneficial for backdoor attacks.
2. An invertible pruning mask designed to remove the backdoor task while preserving it through the inverse mask.

The authors demonstrate that this approach outperforms existing fine-tuning-based approaches in terms of accuracy and robustness, particularly in low-data regimes where traditional methods may struggle. They also show that PFT can be applied to a wide range of architectures, including convolutional neural networks (CNNs), which is not typically addressed by previous pruning techniques.

The paper's key contributions include:

1. A novel selection mechanism for identifying critical parameters.
2. An invertible pruning mask designed to achieve two complementary goals: eliminating the backdoor task while preserving it through the inverse mask.
3. A bi-level optimization problem that jointly learns these selection variables and an invertible pruning mask.

The authors argue that PFT offers a promising alternative to traditional fine-tuning-based approaches, potentially leading to more robust and interpretable neural network architectures.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: f04f6507ada5d23d7fbe237d5ebf4d5a0c9e8a116a4b7ad624dfc1c733f94eab
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:10.730034'
category: 24-computing
---

arXiv:2509.15497v1 Announce Type: new Abstract: Model pruning has gained traction as a promising defense strategy against backdoor attacks in deep learning. However, existing pruning-based approaches often fall short in accurately identifying and removing the specific parameters responsible for inducing backdoor behaviors. Despite the dominance of fine-tuning-based defenses in recent literature, largely due to their superior performance, pruning remains a compelling alternative, offering greater interpretability and improved robustness in low-data regimes. In this paper, we propose a novel pruning approach featuring a learned \emph{selection} mechanism to identify parameters critical to both main and backdoor tasks, along with an \emph{invertible} pruning mask designed to simultaneously achieve two complementary goals: eliminating the backdoor task while preserving it through the inverse mask. We formulate this as a bi-level optimization problem that jointly learns selection variables,...