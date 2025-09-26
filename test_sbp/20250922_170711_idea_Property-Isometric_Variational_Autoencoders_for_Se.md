---
title: Property-Isometric Variational Autoencoders for Sequence Modeling and Design
link: https://arxiv.org/abs/2509.14287
summary: 'The article discusses a new approach called PrIVAE (Pragmatic Variational Autoencoder) for optimizing complex properties of biomolecules such as DNA, RNA, and peptides. The key features are:

1. It uses geometry-preserving variational autoencoders to learn embeddings that respect the geometric structure of their property space.
2. It models the property space as a high-dimensional manifold that can be locally approximated by a nearest neighbor graph.
3. It employs this model to optimize properties like emission spectra, stability, and antimicrobial activity across different target microbes.

The authors aim to overcome the limitations of existing models that rely on simple binary labels (e.g., binding/non-binding) rather than high-dimensional complex properties. By learning latent sequence embeddings that respect the geometry of their property space, PrIVAE aims to enable more effective optimization in this area.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: a186238241e51a6150b4b00aa1249e36acfc4a86c5936df6115ad3c36824eaac
feed_title: cs.AI updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.AI
date_processed: '2025-09-22T17:07:11.037978'
category: 24-computing
---

arXiv:2509.14287v1 Announce Type: cross Abstract: Biological sequence design (DNA, RNA, or peptides) with desired functional properties has applications in discovering novel nanomaterials, biosensors, antimicrobial drugs, and beyond. One common challenge is the ability to optimize complex high-dimensional properties such as target emission spectra of DNA-mediated fluorescent nanoparticles, photo and chemical stability, and antimicrobial activity of peptides across target microbes. Existing models rely on simple binary labels (e.g., binding/non-binding) rather than high-dimensional complex properties. To address this gap, we propose a geometry-preserving variational autoencoder framework, called PrIVAE, which learns latent sequence embeddings that respect the geometry of their property space. Specifically, we model the property space as a high-dimensional manifold that can be locally approximated by a nearest neighbor graph, given an appropriately defined distance measure. We employ the...