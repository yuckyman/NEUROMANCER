---
title: 'AutoEdit: Automatic Hyperparameter Tuning for Image Editing'
link: https://arxiv.org/abs/2509.15031
summary: 'The article discusses the development and application of diffusion models in text-guided image editing, which have revolutionized this process but also present challenges related to hyperparameter tuning. To address these issues, a new approach called reinforcement learning is proposed. The framework establishes a Markov Decision Process that dynamically adjusts hyperparameters across denoising steps, integrating editing objectives into a reward function. This method achieves time efficiency while maintaining optimal hyperparameter configurations.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: b5ea669924152eabc490aed910e480a0480e037898f8c36988c0fb295b313fc7
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:10.230431'
category: 24-computing
---

arXiv:2509.15031v1 Announce Type: new Abstract: Recent advances in diffusion models have revolutionized text-guided image editing, yet existing editing methods face critical challenges in hyperparameter identification. To get the reasonable editing performance, these methods often require the user to brute-force tune multiple interdependent hyperparameters, such as inversion timesteps and attention modification, \textit{etc.} This process incurs high computational costs due to the huge hyperparameter search space. We consider searching optimal editing's hyperparameters as a sequential decision-making task within the diffusion denoising process. Specifically, we propose a reinforcement learning framework, which establishes a Markov Decision Process that dynamically adjusts hyperparameters across denoising steps, integrating editing objectives into a reward function. The method achieves time efficiency through proximal policy optimization while maintaining optimal hyperparameter configur...