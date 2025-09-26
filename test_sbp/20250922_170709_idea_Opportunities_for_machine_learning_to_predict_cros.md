---
title: Opportunities for machine learning to predict cross-neutralization in FMDV
  serotype O
link: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1013491
summary: 'The article discusses the development of a machine learning approach to estimate antigenic similarity between serotype O foot-and-mouth disease viruses using VP1 sequence data and published virus neutralization titer results. The study involved 108 serum-virus pairs representing 73 distinct FMDV strains, which were used to train a model that can predict cross-neutralization between the viruses. The researchers optimized the model through tenfold cross-validation and sub-sampling to address class imbalance. They identified key factors such as pairwise amino acid distances, site-specific polymorphisms, and differences in potential N-glycosylation sites as predictors of cross-neutralization. The final model achieved high accuracy (0.96), sensitivity (0.93), and specificity (0.96) in training, demonstrating its effectiveness for disease management and vaccine selection.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 7fbb53244a53a12b40cb0fc91b7a70e56f6d558da06223a2a24e5fddde235f7d
feed_title: PLOS Computational Biology
feed_url: https://journals.plos.org/ploscompbiol/feed/atom
date_processed: '2025-09-22T17:07:09.868330'
category: 24-computing
---

by Dennis N. Makau, Jonathan Arzt, Kimberly VanderWaal Accurately estimating cross-neutralization between serotype O foot-and-mouth disease viruses (FMDVs) is critical for guiding vaccine selection and disease management. In this study, we developed a machine learning approach to estimate r1 values—an established measure of antigenic similarity—using VP1 sequence data and published virus neutralization titer (VNT) results. Our dataset comprised 108 serum-virus pairs representing 73 distinct FMDV strains. We applied Boruta feature selection and random forest classifiers, optimizing model performance through tenfold cross-validation and sub-sampling to address class imbalance. Predictors included pairwise amino acid distances, site-specific polymorphisms, and differences in potential N-glycosylation sites. Using a 0.3 r1 threshold to define cross-neutralization, the final model achieved high accuracy (0.96), sensitivity (0.93), and specificity (0.96) in training, and performed robustly o...