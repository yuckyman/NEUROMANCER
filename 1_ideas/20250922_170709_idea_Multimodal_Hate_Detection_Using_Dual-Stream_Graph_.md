---
title: Multimodal Hate Detection Using Dual-Stream Graph Neural Networks
link: https://arxiv.org/abs/2509.13515
summary: 'The article discusses a new multimodal dual-stream graph neural network (MS-GNN) model designed for detecting and classifying hate videos. The model is based on the idea of separating video content into multiple instances, which allows it to capture the unique characteristics of each instance without being affected by uniform treatment of all content. By assigning importance weights to these features, the model highlights hateful instances in the video, making it more effective at distinguishing between different types of hate videos. The authors also discuss how this approach can be applied to existing multimodal fusion methods and provide a comparison with other approaches.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: e010dc640ca77406c461e5325b68a41370df74ee9d0b7aa8df1a318b2c35c613
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:09.903477'
category: 24-computing
---

arXiv:2509.13515v1 Announce Type: new Abstract: Hateful videos present serious risks to online safety and real-world well-being, necessitating effective detection methods. Although multimodal classification approaches integrating information from several modalities outperform unimodal ones, they typically neglect that even minimal hateful content defines a video's category. Specifically, they generally treat all content uniformly, instead of emphasizing the hateful components. Additionally, existing multimodal methods cannot systematically capture structured information in videos, limiting the effectiveness of multimodal fusion. To address these limitations, we propose a novel multimodal dual-stream graph neural network model. It constructs an instance graph by separating the given video into several instances to extract instance-level features. Then, a complementary weight graph assigns importance weights to these features, highlighting hateful instances. Importance weights and instan...