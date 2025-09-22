---
title: Implicit Kinodynamic Motion Retargeting for Human-to-humanoid Imitation Learning
link: https://arxiv.org/abs/2509.15443
summary: 'The article discusses an approach called Implicit Kinodynamic Motion Retargeting (IKMR) for human-to-humanoid humanoid imitation learning. The key points are:

1. Human-to-humanoid imitation learning aims to learn a humanoid whole-body controller from human motion.

2. Current methods focus on motion retargeting frame by frame, which lacks scalability.

3. To address this issue, the authors propose IKMR, a novel efficient and scalable retargeting framework that combines kinematics and dynamics.

4. IKMR:
   - Pretrains motion topology feature representation
   - Uses dual encoder-decoder architecture for learning a motion domain mapping
   - Integrates imitation learning with the motion retargeting network to refine motion into physically feasible trajectories
   - Fine-tunes using tracking results

5. The authors demonstrate that IKMR can enable robots to acquire reference trajectories when exploring locomotion skills.

6. The approach is scalable and efficient, making it suitable for large-scale human motion processing tasks.

Overall, the article presents a novel framework for human-to-humanoid humanoid imitation learning that combines kinematics and dynamics for more effective motion retargeting.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 03e2a1e5952e0d4bfea4edbc1e59e680210e9b48c462249a7d9457a93a12f209
feed_title: cs.AI updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.AI
date_processed: '2025-09-22T17:07:10.753867'
category: 24-computing
---

arXiv:2509.15443v1 Announce Type: cross Abstract: Human-to-humanoid imitation learning aims to learn a humanoid whole-body controller from human motion. Motion retargeting is a crucial step in enabling robots to acquire reference trajectories when exploring locomotion skills. However, current methods focus on motion retargeting frame by frame, which lacks scalability. Could we directly convert large-scale human motion into robot-executable motion through a more efficient approach? To address this issue, we propose Implicit Kinodynamic Motion Retargeting (IKMR), a novel efficient and scalable retargeting framework that considers both kinematics and dynamics. In kinematics, IKMR pretrains motion topology feature representation and a dual encoder-decoder architecture to learn a motion domain mapping. In dynamics, IKMR integrates imitation learning with the motion retargeting network to refine motion into physically feasible trajectories. After fine-tuning using the tracking results, IKMR ...