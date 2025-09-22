---
title: A Real-Time Multi-Model Parametric Representation of Point Clouds
link: https://arxiv.org/abs/2509.14773
summary: 'The article discusses a new approach to parametric representations of point clouds, specifically for tasks such as memory-efficient mapping and multi-robot collaboration. The authors propose a multi-model parametric representation with real-time surface detection and fitting capabilities. They use the Gaussian mixture model (GMM) to segment the point cloud into multiple clusters, then select flat clusters and merge them into planes or curved surfaces. These models are equipped with 2D voxel-based boundary descriptions for easy fitting of planes and B-spline surfaces. The authors also discuss the advantages and limitations of this approach compared to existing methods, such as spline surfaces and quadrics.'
tags:
- unclassified
content_hash: a5bdd0383f8dac9eec47ac6b3e333c9a75ef0563606208c35d6132e83e2e7b29
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:09.910432'
---

arXiv:2509.14773v1 Announce Type: new Abstract: In recent years, parametric representations of point clouds have been widely applied in tasks such as memory-efficient mapping and multi-robot collaboration. Highly adaptive models, like spline surfaces or quadrics, are computationally expensive in detection or fitting. In contrast, real-time methods, such as Gaussian mixture models or planes, have low degrees of freedom, making high accuracy with few primitives difficult. To tackle this problem, a multi-model parametric representation with real-time surface detection and fitting is proposed. Specifically, the Gaussian mixture model is first employed to segment the point cloud into multiple clusters. Then, flat clusters are selected and merged into planes or curved surfaces. Planes can be easily fitted and delimited by a 2D voxel-based boundary description method. Surfaces with curvature are fitted by B-spline surfaces and the same boundary description method is employed. Through evaluati...