---
title: 'MAP: End-to-End Autonomous Driving with Map-Assisted Planning'
link: https://arxiv.org/abs/2509.13926
summary: 'The article discusses an end-to-end autonomous driving system that uses online mapping modules to enhance trajectory planning within a unified framework. The proposed MAP (Map-Assisted Planning) method integrates segmentation-based map features with current ego status through three modules: Plan-enhancing Online Mapping, Ego-status-guided Planning, and Weight Adapter based on current ego status. The authors conducted experiments on the DAIR-V2X-seq-SPD dataset to evaluate the performance of MAP compared to a baseline without post-processing. The results showed that MAP significantly reduces L2 displacement error, off-road rate, and overall score, even after excluding post-processing steps.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 4e805fb87623d32ffd35c2705b2d0b679c2af41a1231b3bc1704fbdb1bcc38a1
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:11.630447'
category: 24-computing
---

arXiv:2509.13926v1 Announce Type: cross Abstract: In recent years, end-to-end autonomous driving has attracted increasing attention for its ability to jointly model perception, prediction, and planning within a unified framework. However, most existing approaches underutilize the online mapping module, leaving its potential to enhance trajectory planning largely untapped. This paper proposes MAP (Map-Assisted Planning), a novel map-assisted end-to-end trajectory planning framework. MAP explicitly integrates segmentation-based map features and the current ego status through a Plan-enhancing Online Mapping module, an Ego-status-guided Planning module, and a Weight Adapter based on current ego status. Experiments conducted on the DAIR-V2X-seq-SPD dataset demonstrate that the proposed method achieves a 16.6% reduction in L2 displacement error, a 56.2% reduction in off-road rate, and a 44.5% improvement in overall score compared to the UniV2X baseline, even without post-processing. Furtherm...