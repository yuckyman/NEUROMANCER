---
title: 'GUI-ARP: Enhancing Grounding with Adaptive Region Perception for GUI Agents'
link: https://arxiv.org/abs/2509.15532
summary: 'The article discusses a new framework called GUI-ARP (Grounding for Visual Recognition) that enables adaptive multi-stage inference in high-resolution screenshots. The authors propose this by using the Adaptive Region Perception (ARP) and Adaptive Stage Controlling (ASC) techniques to dynamically exploit visual attention for cropping task-relevant regions during single-stage inference. This approach is achieved through a two-phase training pipeline that integrates supervised fine-tuning with reinforcement fine-tuning based on Group Relative Policy Optimization (GRPO). The authors evaluate the proposed framework using ScreenSpot-Pro and UI-Vision benchmarks, demonstrating state-of-the-art performance with a 7B model achieving 60.8% accuracy on ScreenSpot-Pro and 30.9% on UI-Vision benchmark.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 9df34c1aa95185dfd54898247f8e11a50d161b9c663aaf0866877b696653bf06
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:10.719899'
category: 24-computing
---

arXiv:2509.15532v1 Announce Type: new Abstract: Existing GUI grounding methods often struggle with fine-grained localization in high-resolution screenshots. To address this, we propose GUI-ARP, a novel framework that enables adaptive multi-stage inference. Equipped with the proposed Adaptive Region Perception (ARP) and Adaptive Stage Controlling (ASC), GUI-ARP dynamically exploits visual attention for cropping task-relevant regions and adapts its inference strategy, performing a single-stage inference for simple cases and a multi-stage analysis for more complex scenarios. This is achieved through a two-phase training pipeline that integrates supervised fine-tuning with reinforcement fine-tuning based on Group Relative Policy Optimization (GRPO). Extensive experiments demonstrate that the proposed GUI-ARP achieves state-of-the-art performance on challenging GUI grounding benchmarks, with a 7B model reaching 60.8% accuracy on ScreenSpot-Pro and 30.9% on UI-Vision benchmark. Notably, GUI-...