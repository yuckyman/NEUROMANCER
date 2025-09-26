---
title: 'OpenViGA: Video Generation for Automotive Driving Scenes by Streamlining and
  Fine-Tuning Open Source Models with Public Data'
link: https://arxiv.org/abs/2509.15479
summary: 'The article discusses a new approach to generating realistic driving scenes using video inputs. The authors present OpenViGA, an open-source system that combines tokenization, future state prediction, and video decoding into one component. They provide a detailed analysis of the three components of their system by evaluating them separately through quantitative and qualitative methods. The authors note that these approaches often utilize large models with limited insight into design choices and lack publicly available code and datasets.

The main contributions of this work are:
1. A new approach to video generation for automotive driving scenes.
2. A detailed analysis of the three components of their system by evaluating them separately through quantitative and qualitative methods.
3. The authors' use of powerful pre-trained open-source models from various domains, such as BDD100K, to build upon and fine-tune these models on GPU.

The article presents a new approach that combines tokenization, future state prediction, and video decoding into one component, offering a more comprehensive solution for generating realistic driving scenes.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 1efff352867c48b2b94bf4f08e8bd2537360062675eb51d8b976365e36f3a61a
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:10.550389'
category: 24-computing
---

arXiv:2509.15479v1 Announce Type: new Abstract: Recent successful video generation systems that predict and create realistic automotive driving scenes from short video inputs assign tokenization, future state prediction (world model), and video decoding to dedicated models. These approaches often utilize large models that require significant training resources, offer limited insight into design choices, and lack publicly available code and datasets. In this work, we address these deficiencies and present OpenViGA, an open video generation system for automotive driving scenes. Our contributions are: Unlike several earlier works for video generation, such as GAIA-1, we provide a deep analysis of the three components of our system by separate quantitative and qualitative evaluation: Image tokenizer, world model, video decoder. Second, we purely build upon powerful pre-trained open source models from various domains, which we fine-tune by publicly available automotive data (BDD100K) on GPU...