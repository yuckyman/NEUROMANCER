---
title: Effects of segmentation errors on downstream-analysis in highly-multiplexed
  tissue imaging
link: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1013350
summary: 'This article discusses high-throughput single-cell imaging technologies and their applications in capturing spatial protein expression at the single-cell level. However, these advancements rely on accurate cell segmentation to generate expression profiles. Despite its importance, there is a gap in quantifying how segmentation inaccuracies propagate through analytical pipelines, particularly affecting cell clustering and phenotyping.

The authors introduce a framework that uses affine transformations to simulate realistic segmentation errors. This approach allows them to evaluate the robustness of downstream analyses under controlled perturbation conditions. The study demonstrates that even moderate segmentation errors can significantly distort estimated prototypic images, which may affect the accuracy of protein expression measurements.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 9866164018418b5110cda27b705f812da25a8af6f63f1d1642add53b669d28b3
feed_title: PLOS Computational Biology
feed_url: https://journals.plos.org/ploscompbiol/feed/atom
date_processed: '2025-09-22T17:07:11.250687'
category: 24-computing
---

by Matthias Bruhns, Jan T. Schleicher, Maximilian Wirth, Marcello Zago, Sepideh Babaei, Manfred Claassen Highly multiplexed single-cell imaging technologies have revolutionized our ability to capture spatial protein expression at the single-cell level, thereby enabling a deeper understanding of tissue organization and function. However, these advancements rely on accurate cell segmentation, which defines cell boundaries to generate expression profiles. Despite its importance, there is a gap in quantifying how segmentation inaccuracies propagate through analytical pipelines, particularly affecting cell clustering and phenotyping. We introduce a framework that uses affine transformations to simulate realistic segmentation errors. Our approach mimics the variations induced by segmentation algorithms, allowing us to evaluate the robustness of downstream analyses under controlled perturbation conditions. We show that even moderate segmentation errors can significantly distort estimated prot...