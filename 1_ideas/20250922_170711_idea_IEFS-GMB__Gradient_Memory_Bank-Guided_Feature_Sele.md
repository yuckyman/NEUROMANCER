---
title: 'IEFS-GMB: Gradient Memory Bank-Guided Feature Selection Based on Information
  Entropy for EEG Classification of Neurological Disorders'
link: https://arxiv.org/abs/2509.15259
summary: 'The article discusses the use of deep learning-based EEG classification for automated neurological disorders detection. However, the low signal-to-noise ratio of EEG signals makes traditional FS methods ineffective. To address this issue, the authors propose a new method called IEFS-GMB (Information Entropy-Based Feature Selection guided by a Gradient Memory Bank). The approach constructs a dynamic memory bank storing historical gradients and computes feature importance via information entropy. It then applies entropy-based weighting to select informative EEG features. This method is designed specifically for EEG diagnosis and addresses the limitations of existing FS methods, such as architecture dependence and lack of interpretability. The authors also discuss the advantages of their method over traditional FS methods, including its ability to handle variability in EEG signals and its robustness to variations in data.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 5b5ccf1dadf0a8ff04d305dca9ae9d27b52fcfdcfef112cbf60eefed0ea8b1c0
feed_title: cs.AI updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.AI
date_processed: '2025-09-22T17:07:11.856895'
category: 24-computing
---

arXiv:2509.15259v1 Announce Type: cross Abstract: Deep learning-based EEG classification is crucial for the automated detection of neurological disorders, improving diagnostic accuracy and enabling early intervention. However, the low signal-to-noise ratio of EEG signals limits model performance, making feature selection (FS) vital for optimizing representations learned by neural network encoders. Existing FS methods are seldom designed specifically for EEG diagnosis; many are architecture-dependent and lack interpretability, limiting their applicability. Moreover, most rely on single-iteration data, resulting in limited robustness to variability. To address these issues, we propose IEFS-GMB, an Information Entropy-based Feature Selection method guided by a Gradient Memory Bank. This approach constructs a dynamic memory bank storing historical gradients, computes feature importance via information entropy, and applies entropy-based weighting to select informative EEG features. Experime...