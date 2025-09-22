---
title: 'CAGE: Continuity-Aware edGE Network Unlocks Robust Floorplan Reconstruction'
link: https://arxiv.org/abs/2509.15459
summary: 'The article discusses the development of CAGE (Continuity-Aware edGE) network, which is a robust framework for reconstructing vector floorplans directly from point-cloud density maps. The authors propose a native edge-centric formulation that models each wall segment as a directed, geometrically continuous edge. This representation enables inference of coherent floorplan structures while improving robustness and reducing artifacts compared to traditional corner-based polygon representations.

The article also discusses the use of a dual-query transformer decoder for integrating perturbed and latent queries within a denoising framework, which helps in refining the reconstruction process.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: cf371d41e23c85e813cc7258af163a20a157a79dd92c7ec58c5e4a7cac4590c8
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:10.199293'
category: 24-computing
---

arXiv:2509.15459v1 Announce Type: new Abstract: We present \textbf{CAGE} (\textit{Continuity-Aware edGE}) network, a \textcolor{red}{robust} framework for reconstructing vector floorplans directly from point-cloud density maps. Traditional corner-based polygon representations are highly sensitive to noise and incomplete observations, often resulting in fragmented or implausible layouts. Recent line grouping methods leverage structural cues to improve robustness but still struggle to recover fine geometric details. To address these limitations, we propose a \textit{native} edge-centric formulation, modeling each wall segment as a directed, geometrically continuous edge. This representation enables inference of coherent floorplan structures, ensuring watertight, topologically valid room boundaries while improving robustness and reducing artifacts. Towards this design, we develop a dual-query transformer decoder that integrates perturbed and latent queries within a denoising framework, wh...