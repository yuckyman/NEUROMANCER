---
title: 'MEC-Quant: Maximum Entropy Coding for Extremely Low Bit Quantization-Aware
  Training'
link: https://arxiv.org/abs/2509.15514
summary: 'The article discusses a new approach called Maximum Entropy Coding Quantization (MEC-Quant), which is designed to improve the performance of quantized neural networks. The authors argue that current methods like QAT, which use quantization for better training efficiency, are not always effective in reducing biases and improving generalization capabilities. MEC-Quant addresses this by explicitly optimizing the structure of the learned representation, making it less biased and more generalizable to unseen data.

To achieve this, the authors propose a new objective function called the Minimum Entropy Coding Length (MEC-L) that is end-to-end trainable. This makes the optimization process faster and easier than traditional methods. Additionally, they introduce a scalable reformulation of the MEC-L based on Mixture Of Experts (MOE), which allows for efficient computation while still being effective in reducing biases.

The main contributions of this work are:
1. A principled objective that explicitly optimizes the structure of the learned representation.
2. An end-to-end trainable objective function.
3. A scalable reformulation of the objective based on Mixture Of Experts (MOE).
4. Fast computation and improved generalization capabilities compared to traditional methods.

The authors argue that this approach can lead to better performance in quantized neural networks, potentially overcoming some limitations of current QAT techniques.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: b6bcb6fdda5785b90bc698de911a2d4e2194cc28d0166d693a619077c986811a
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:09.863074'
category: 24-computing
---

arXiv:2509.15514v1 Announce Type: new Abstract: Quantization-Aware Training (QAT) has driven much attention to produce efficient neural networks. Current QAT still obtains inferior performances compared with the Full Precision (FP) counterpart. In this work, we argue that quantization inevitably introduce biases into the learned representation, especially under the extremely low-bit setting. To cope with this issue, we propose Maximum Entropy Coding Quantization (MEC-Quant), a more principled objective that explicitly optimizes on the structure of the representation, so that the learned representation is less biased and thus generalizes better to unseen in-distribution samples. To make the objective end-to-end trainable, we propose to leverage the minimal coding length in lossy data coding as a computationally tractable surrogate for the entropy, and further derive a scalable reformulation of the objective based on Mixture Of Experts (MOE) that not only allows fast computation but also...