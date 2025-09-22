---
title: Spike-based time-domain analog weighted-sum calculation model for extremely
  low power VLSI implementation of multi-layer neural networks
link: https://www.frontiersin.org/articles/10.3389/fnins.2025.1656892
summary: 'The article discusses a time-domain analog weighted-sum calculation model for multi-layer feedforward networks using complementary metal-oxide-semiconductor (CMOS) very-large-scale integration (VLSI) circuits. The model is based on an integrate-and-fire-type spiking neuron model and applies it to the calculation of weighted summations with positive and negative weights in each layer. The timings produced by this model are then fed into the next layers without their subtraction operation, allowing for efficient and low-power computation.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 2aa471a47a8a8f247413605904a7e2730b382490fd0f16da5a09e93e0d3bfc81
feed_title: Frontiers in Neuroscience | New and Recent Articles
feed_url: https://www.frontiersin.org/journals/neuroscience/rss
date_processed: '2025-09-22T17:07:10.024831'
category: 24-computing
---

In deep neural network (DNN) models, the weighted summation, or multiply-and-accumulate (MAC) operation, is an essential and heavy calculation task, which leads to high power consumption in current digital processors. The use of analog operation in complementary metal-oxide-semiconductor (CMOS) very-large-scale integration (VLSI) circuits is a promising method for achieving extremely low power-consumption operation for such calculation tasks. In this paper, a time-domain analog weighted-sum calculation model is proposed based on an integrate-and-fire-type spiking neuron model. The proposed calculation model is applied to multi-layer feedforward networks, in which weighted summations with positive and negative weights are separately performed, and two timings proportional to the positive and negative ones are produced, respectively, in each layer. The timings are then fed into the next layers without their subtraction operation. We also propose VLSI circuits to implement the proposed mo...