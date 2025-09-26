---
title: Temporal Representation Learning of Phenotype Trajectories for pCR Prediction
  in Breast Cancer
link: https://arxiv.org/abs/2509.14872
summary: 'The article discusses an approach to predicting the progression and response to treatment for breast cancer patients undergoing neoadjuvant chemotherapy (NACT). The authors propose a method called "early dynamics learning" that uses MRI data from the patient's breast forms to predict successful response. They use a multi-task model, which combines information from different tasks like appearance, temporal continuity, and comparability in the non-responder cohort. In experiments on a publicly available dataset, their linear classifier achieves a balanced accuracy of 0.761 using only pre-treatment data (T0), indicating that it can effectively predict response to NACT.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: e04419c57ec84a25309ae1b9714d2756b28c7a1d86f31f1933c153048fa09d1a
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:09.826861'
category: 24-computing
---

arXiv:2509.14872v1 Announce Type: new Abstract: Effective therapy decisions require models that predict the individual response to treatment. This is challenging since the progression of disease and response to treatment vary substantially across patients. Here, we propose to learn a representation of the early dynamics of treatment response from imaging data to predict pathological complete response (pCR) in breast cancer patients undergoing neoadjuvant chemotherapy (NACT). The longitudinal change in magnetic resonance imaging (MRI) data of the breast forms trajectories in the latent space, serving as basis for prediction of successful response. The multi-task model represents appearance, fosters temporal continuity and accounts for the comparably high heterogeneity in the non-responder cohort.In experiments on the publicly available ISPY-2 dataset, a linear classifier in the latent trajectory space achieves a balanced accuracy of 0.761 using only pre-treatment data (T0), 0.811 using ...