---
title: 'DICE: Diffusion Consensus Equilibrium for Sparse-view CT Reconstruction'
link: https://arxiv.org/abs/2509.14566
summary: 'The article discusses a new approach to sparse-view computed tomography (CT) reconstruction called Diffusion Consensus Equilibrium (DICE). In this method, the data-consistency agent is implemented through a proximal operator that ensures measurement consistency between the reconstructed image and the true underlying image. The prior agent, on the other hand, relies on a diffusion model to accurately represent complex distributions in medical images. DICE alternates between these two agents, allowing for an iterative process of combining strong generative priors with data-consistent estimates. This approach aims to address the challenges associated with undersampling and ill-posed inverse problems in CT reconstruction by incorporating both types of prior information.'
tags:
- unclassified
content_hash: 313c1ac8e3a63878c5a145fba19907fecba22128fbbad82a4e7d6f369d9d9253
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:11.772750'
---

arXiv:2509.14566v1 Announce Type: new Abstract: Sparse-view computed tomography (CT) reconstruction is fundamentally challenging due to undersampling, leading to an ill-posed inverse problem. Traditional iterative methods incorporate handcrafted or learned priors to regularize the solution but struggle to capture the complex structures present in medical images. In contrast, diffusion models (DMs) have recently emerged as powerful generative priors that can accurately model complex image distributions. In this work, we introduce Diffusion Consensus Equilibrium (DICE), a framework that integrates a two-agent consensus equilibrium into the sampling process of a DM. DICE alternates between: (i) a data-consistency agent, implemented through a proximal operator enforcing measurement consistency, and (ii) a prior agent, realized by a DM performing a clean image estimation at each sampling step. By balancing these two complementary agents iteratively, DICE effectively combines strong generati...