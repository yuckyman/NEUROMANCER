---
title: 'Brain-HGCN: A Hyperbolic Graph Convolutional Network for Brain Functional
  Network Analysis'
link: https://arxiv.org/abs/2509.14965
summary: 'The article discusses a new framework called Brain-HGCN (Hyperbolic Graph Neural Networks) that uses geometric deep learning techniques to model the brain's functional networks. The authors propose a novel hyperbolic graph attention layer with a signed aggregation mechanism, which is used to process excitatory and inhibitory connections in the brain. This method effectively represents the hierarchical structure of the network without high distortion, making it suitable for clinical applications.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 3e47faa59eed38d2dfd54a1ac6b31b786d946bd676f7f9bb43463523c754fe9f
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:10.512151'
category: 24-computing
---

arXiv:2509.14965v1 Announce Type: new Abstract: Functional magnetic resonance imaging (fMRI) provides a powerful non-invasive window into the brain's functional organization by generating complex functional networks, typically modeled as graphs. These brain networks exhibit a hierarchical topology that is crucial for cognitive processing. However, due to inherent spatial constraints, standard Euclidean GNNs struggle to represent these hierarchical structures without high distortion, limiting their clinical performance. To address this limitation, we propose Brain-HGCN, a geometric deep learning framework based on hyperbolic geometry, which leverages the intrinsic property of negatively curved space to model the brain's network hierarchy with high fidelity. Grounded in the Lorentz model, our model employs a novel hyperbolic graph attention layer with a signed aggregation mechanism to distinctly process excitatory and inhibitory connections, ultimately learning robust graph-level represe...