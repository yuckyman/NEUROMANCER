---
title: 'ChannelFlow-Tools: A Standardized Dataset Creation Pipeline for 3D Obstructed
  Channel Flows'
link: https://arxiv.org/abs/2509.15236
summary: 'The article describes "ChannelFlow-Tools," a configuration-driven framework for generating 3D obstructed channel flows from programmatic CAD solids using machine learning algorithms. The toolchain integrates geometry synthesis, feasibility checks, signed distance field (SDF) voxelization, automated solver orchestration on HPC (waLBerla LBM), and Cartesian resampling to co-registered multi-resolution tensors. A single configuration governs all stages, enabling deterministic reproduction and controlled ablations. The tool is used in a case study where 10k+ scenes spanning Re=100-15000 with diverse shapes and poses are generated. An end-to-end evaluation of storage trade-offs from the emitted artifacts, a minimal 3D U-Net at 128x32x32, and example surrogate models with dataset size is presented to illustrate that standardized representations support reproducible ML training.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 29df81c5a8916102cf32b984175e2663db9c6d6ce678b793ab5cf91d2842aadf
feed_title: cs.AI updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.AI
date_processed: '2025-09-22T17:07:10.164221'
category: 24-computing
---

arXiv:2509.15236v1 Announce Type: cross Abstract: We present ChannelFlow-Tools, a configuration-driven framework that standardizes the end-to-end path from programmatic CAD solid generation to ML-ready inputs and targets for 3D obstructed channel flows. The toolchain integrates geometry synthesis with feasibility checks, signed distance field (SDF) voxelization, automated solver orchestration on HPC (waLBerla LBM), and Cartesian resampling to co-registered multi-resolution tensors. A single Hydra/OmegaConf configuration governs all stages, enabling deterministic reproduction and controlled ablations. As a case study, we generate 10k+ scenes spanning Re=100-15000 with diverse shapes and poses. An end-to-end evaluation of storage trade-offs directly from the emitted artifacts, a minimal 3D U-Net at 128x32x32, and example surrogate models with dataset size illustrate that the standardized representations support reproducible ML training. ChannelFlow-Tools turns one-off dataset creation in...