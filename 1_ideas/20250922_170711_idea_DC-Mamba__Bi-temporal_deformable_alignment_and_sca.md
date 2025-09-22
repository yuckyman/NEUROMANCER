---
title: 'DC-Mamba: Bi-temporal deformable alignment and scale-sparse enhancement for
  remote sensing change detection'
link: https://arxiv.org/abs/2509.15563
summary: 'The article discusses a new method called DC-Mamba that combines two lightweight modules for remote sensing change detection: Bi-Temporal Deformable Alignment (BTDA) and Scale-Sparse Change Amplifier (SSCA). BTDA is designed to correct spatial misalignments at the semantic feature level, while SSCA uses multi-source cues to selectively amplify high-confidence change signals before final classification. The authors argue that this approach improves accuracy by addressing issues like geometric misalignments and noise.'
tags:
- unclassified
content_hash: ab8f851915b401cb844b545ecbc95398f36f9bae8e83835aaf30992b030bd324
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:11.940081'
---

arXiv:2509.15563v1 Announce Type: new Abstract: Remote sensing change detection (RSCD) is vital for identifying land-cover changes, yet existing methods, including state-of-the-art State Space Models (SSMs), often lack explicit mechanisms to handle geometric misalignments and struggle to distinguish subtle, true changes from noise.To address this, we introduce DC-Mamba, an "align-then-enhance" framework built upon the ChangeMamba backbone. It integrates two lightweight, plug-and-play modules: (1) Bi-Temporal Deformable Alignment (BTDA), which explicitly introduces geometric awareness to correct spatial misalignments at the semantic feature level; and (2) a Scale-Sparse Change Amplifier(SSCA), which uses multi-source cues to selectively amplify high-confidence change signals while suppressing noise before the final classification. This synergistic design first establishes geometric consistency with BTDA to reduce pseudo-changes, then leverages SSCA to sharpen boundaries and enhance the ...