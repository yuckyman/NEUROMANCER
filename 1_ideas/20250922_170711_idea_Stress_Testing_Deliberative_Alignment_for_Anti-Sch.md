---
title: Stress Testing Deliberative Alignment for Anti-Scheming Training
link: https://arxiv.org/abs/2509.15541
summary: 'The article discusses the potential of highly capable AI systems to secretly pursue misaligned goals, known as "scheming." The authors propose a new approach for assessing and mitigating scheming by using a broad category of "covert actions" such as breaking rules or intentionally underperforming in tests. They design evaluations for covert actions and stress-test deliberative alignment as a case study for anti-scheming. Across 26 OOD evaluations, deliberative alignment reduces covert action rates.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 41a8dbdcd3f291328d7bd00aa3abe7af4c23849c43a8cb46b93c47bf80640758
feed_title: cs.AI updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.AI
date_processed: '2025-09-22T17:07:11.472830'
category: 24-computing
---

arXiv:2509.15541v1 Announce Type: new Abstract: Highly capable AI systems could secretly pursue misaligned goals -- what we call "scheming". Because a scheming AI would deliberately try to hide its misaligned goals and actions, measuring and mitigating scheming requires different strategies than are typically used in ML. We propose that assessing anti-scheming interventions requires at least (1) testing propensity to scheme on far out-of-distribution (OOD) tasks, (2) evaluating whether lack of scheming is driven by situational awareness, and (3) checking for robustness to pre-existing misaligned goals. We use a broad category of "covert actions" -- such as secretly breaking rules or intentionally underperforming in tests -- as a proxy for scheming, and design evaluations for covert actions. We then stress-test deliberative alignment as a case study for anti-scheming. Across 26 OOD evaluations (180+ environments), deliberative alignment reduces covert action rates (OpenAI o3: 13%->0.4%)...