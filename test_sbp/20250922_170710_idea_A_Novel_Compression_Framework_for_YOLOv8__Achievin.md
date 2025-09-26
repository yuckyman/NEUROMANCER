---
title: 'A Novel Compression Framework for YOLOv8: Achieving Real-Time Aerial Object
  Detection on Edge Devices via Structured Pruning and Channel-Wise Distillation'
link: https://arxiv.org/abs/2509.12918
summary: 'The article discusses a new method called "YOLOv8" that combines sparsity-aware training, structured channel pruning, and Channel-Wise Knowledge Distillation (CWD) to improve the efficiency of deep learning models used in aerial object detection. The authors propose a three-stage compression pipeline for YOLOv8, which involves dynamic sparsity during model optimization, batch normalization scaling factors for structured channel pruning, and CWD for knowledge transfer from the original model. This approach aims to reduce model size without compromising performance on resource-constrained devices.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: c9782c07924317db196e491b4ad3441d29e48d36ba3b252bcc6f093f7f4b7fa0
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:10.448475'
category: 24-computing
---

arXiv:2509.12918v2 Announce Type: replace Abstract: Efficient deployment of deep learning models for aerial object detection on resource-constrained devices requires significant compression without com-promising performance. In this study, we propose a novel three-stage compression pipeline for the YOLOv8 object detection model, integrating sparsity-aware training, structured channel pruning, and Channel-Wise Knowledge Distillation (CWD). First, sparsity-aware training introduces dynamic sparsity during model optimization, effectively balancing parameter reduction and detection accuracy. Second, we apply structured channel pruning by leveraging batch normalization scaling factors to eliminate redundant channels, significantly reducing model size and computational complexity. Finally, to mitigate the accuracy drop caused by pruning, we employ CWD to transfer knowledge from the original model, using an adjustable temperature and loss weighting scheme tailored for small and medium object ...