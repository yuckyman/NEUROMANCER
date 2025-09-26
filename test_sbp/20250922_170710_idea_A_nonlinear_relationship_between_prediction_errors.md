---
title: A nonlinear relationship between prediction errors and learning rates in human
  reinforcement-learning
link: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1013445
summary: 'The article discusses the relationship between prediction errors (PEs) and learning rates (learning rates) in reinforcement-learning models. The authors demonstrate that the relationship is nonlinear over the PEs/learning rates space, and can be accounted for by an exponential-logarithmic function. They also provide a novel RL model that predicts how PEs and learning rates are related to each other.

The article presents simulations, reanalyses of readily available datasets, and a new experiment to study this relationship in detail.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: c18a94cfa3ccf27b1d1f1ae681f2b43e27b851beee0d80cd10fc3e1053b2db22
feed_title: PLOS Computational Biology
feed_url: https://journals.plos.org/ploscompbiol/feed/atom
date_processed: '2025-09-22T17:07:10.090827'
category: 24-computing
---

by Boluwatife Ikwunne, Jolie Parham, Erdem Pulcu Reinforcement-learning (RL) models have been pivotal to our understanding of how agents perform learning-based adaptions in dynamically changing environments. However, the exact nature of the relationship (e.g., linear, logarithmic etc.) between key components of RL models such as prediction errors (PEs; the difference between the agent’s expectation and the actual outcome) and learning rates (a coefficient used by agents to update their beliefs about the environment) has not been studied in detail. Here, across (i) simulations, (ii) reanalyses of readily available datasets and (iii) a novel experiment, we demonstrate that the relationship between PEs and learning rates is (i) nonlinear over the PE/ learning rates space, and (ii) it can be accounted for by an exponential-logarithmic function that can transform the magnitude of PEs instantaneously to learning rates in a novel RL model. In line with the temporal predictions of this model, ...