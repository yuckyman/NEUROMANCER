---
title: Causal Reasoning Elicits Controllable 3D Scene Generation
link: https://arxiv.org/abs/2509.15249
summary: 'The article discusses CausalStruct, an approach that uses large language models (LLMs) to embed causal reasoning into 3D scene generation. The framework constructs causal graphs where nodes represent objects and attributes, while edges encode causal dependencies and physical constraints. CausalStruct iteratively refines the scene layout by enforcing a causal order to determine the placement of objects and applying interventions based on physics-driven constraints. These interventions ensure consistency with textual descriptions and real-world dynamics.

The authors note that existing methods struggle with modeling complex logical dependencies and physical constraints between objects, making them less effective in adapting to dynamic and realistic environments. CausalStruct addresses this issue by incorporating causal reasoning into 3D scene generation, enabling the framework to adapt to various types of scenes and contexts.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: fb95dba5330d5dfef6f9465d685290fa820d04eb17af0c55b8a730a47274f187
feed_title: cs.AI updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.AI
date_processed: '2025-09-22T17:07:10.858063'
category: 24-computing
---

arXiv:2509.15249v1 Announce Type: cross Abstract: Existing 3D scene generation methods often struggle to model the complex logical dependencies and physical constraints between objects, limiting their ability to adapt to dynamic and realistic environments. We propose CausalStruct, a novel framework that embeds causal reasoning into 3D scene generation. Utilizing large language models (LLMs), We construct causal graphs where nodes represent objects and attributes, while edges encode causal dependencies and physical constraints. CausalStruct iteratively refines the scene layout by enforcing causal order to determine the placement order of objects and applies causal intervention to adjust the spatial configuration according to physics-driven constraints, ensuring consistency with textual descriptions and real-world dynamics. The refined scene causal graph informs subsequent optimization steps, employing a Proportional-Integral-Derivative(PID) controller to iteratively tune object scales a...