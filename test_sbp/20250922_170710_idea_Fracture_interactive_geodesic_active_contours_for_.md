---
title: Fracture interactive geodesic active contours for bone segmentation
link: https://arxiv.org/abs/2509.14817
summary: 'The article discusses a new approach called "fracture interactive geodesic active contour algorithm" for bone segmentation. The main idea is that traditional active contour models often struggle with edge obstruction, edge leakage, and bone fracture issues. To address these problems, the authors propose a novel algorithm that combines the classical geodesic active contour model with a new edge-detector function to better capture bone features and perform robustly in the presence of bone fractures and soft tissues.

The algorithm uses an edge-detector function that combines the intensity and gradient norms, which guides the contour towards bone edges without being obstructed by other soft tissues. Additionally, distance information is introduced into the contour evolution as an adaptive step size to stabilize the evolution and help the contour stop at bone edges and fractures. This embedding provides a way to improve the segmentation accuracy in cases of edge obstruction or fracture.

The authors also discuss how this algorithm can be used for bone segmentation tasks, such as detecting and segmenting bones from medical images.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 241bcb872df903cceed5d09a6797186099624b9b4e011fa9afc92070d3487f34
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:10.087596'
category: 24-computing
---

arXiv:2509.14817v1 Announce Type: new Abstract: For bone segmentation, the classical geodesic active contour model is usually limited by its indiscriminate feature extraction, and then struggles to handle the phenomena of edge obstruction, edge leakage and bone fracture. Thus, we propose a fracture interactive geodesic active contour algorithm tailored for bone segmentation, which can better capture bone features and perform robustly to the presence of bone fractures and soft tissues. Inspired by orthopedic knowledge, we construct a novel edge-detector function that combines the intensity and gradient norm, which guides the contour towards bone edges without being obstructed by other soft tissues and therefore reduces mis-segmentation. Furthermore, distance information, where fracture prompts can be embedded, is introduced into the contour evolution as an adaptive step size to stabilize the evolution and help the contour stop at bone edges and fractures. This embedding provides a way t...