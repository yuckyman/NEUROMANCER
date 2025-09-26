---
title: Real World Robotic Exploration using Deep Neural Networks Trained in Photorealistic
  Reconstructed Environments
link: https://arxiv.org/abs/2509.13342
summary: 'The article discusses an existing deep neural network approach for determining a robot's pose from visual information (RGB images). The authors modify this approach to improve its localization performance without impacting its training ease. They extend the loss function in such a way that it combines positional and rotational errors, increasing robustness to perceptual aliasing. In indoor scenes, the localization accuracy improves by up to 9.64% and 2.99%, respectively, compared to the original network. The authors also use photogrammetry data to produce a pose-labelled dataset for training the modified model on local environments. This trained model forms the basis of a navigation algorithm that is tested in real-time on a TurtleBot robot.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 3cdca47440d86db471c84332945692b78f80a7dd61e03017caed5d601a08f946
feed_title: cs.AI updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.AI
date_processed: '2025-09-22T17:07:09.964837'
category: 24-computing
---

arXiv:2509.13342v1 Announce Type: cross Abstract: In this work, an existing deep neural network approach for determining a robot's pose from visual information (RGB images) is modified, improving its localization performance without impacting its ease of training. Explicitly, the network's loss function is extended in a manner which intuitively combines the positional and rotational error in order to increase robustness to perceptual aliasing. An improvement in the localization accuracy for indoor scenes is observed: with decreases of up to 9.64% and 2.99% in the median positional and rotational error respectively, when compared to the unmodified network. Additionally, photogrammetry data is used to produce a pose-labelled dataset which allows the above model to be trained on a local environment, resulting in localization accuracies of 0.11m & 0.89 degrees. This trained model forms the basis of a navigation algorithm, which is tested in real-time on a TurtleBot (a wheeled robotic devic...