---
title: 'FlowDrive: Energy Flow Field for End-to-End Autonomous Driving'
link: https://arxiv.org/abs/2509.14303
summary: 'The article discusses a novel approach to autonomous driving that leverages multi-view images to construct end-to-end autonomous driving systems. The authors propose FlowDrive, which introduces physically interpretable energy-based flow fields including risk potential and lane attraction fields. These flow-aware features enable adaptive refinement of anchor trajectories and serve as an interpretive guidance for trajectory generation, allowing the system to consider both hard constraints imposed by geometrically occupied obstacles (e.g., vehicles, pedestrians) and soft, rule-based semantics with no explicit geometry (e.g., lane boundaries, traffic priors).'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 11bf69dea8e34671cd1eca869902ec7013f821951878d1a81afb148bf4531af1
feed_title: cs.AI updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.AI
date_processed: '2025-09-22T17:07:09.841758'
category: 24-computing
---

arXiv:2509.14303v1 Announce Type: cross Abstract: Recent advances in end-to-end autonomous driving leverage multi-view images to construct BEV representations for motion planning. In motion planning, autonomous vehicles need considering both hard constraints imposed by geometrically occupied obstacles (e.g., vehicles, pedestrians) and soft, rule-based semantics with no explicit geometry (e.g., lane boundaries, traffic priors). However, existing end-to-end frameworks typically rely on BEV features learned in an implicit manner, lacking explicit modeling of risk and guidance priors for safe and interpretable planning. To address this, we propose FlowDrive, a novel framework that introduces physically interpretable energy-based flow fields-including risk potential and lane attraction fields-to encode semantic priors and safety cues into the BEV space. These flow-aware features enable adaptive refinement of anchor trajectories and serve as interpretable guidance for trajectory generation. ...