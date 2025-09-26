---
title: Fast and exact stochastic simulations of epidemics on static and temporal networks
link: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1013490
summary: '**Summary:** 

Epidemic models on complex networks have been widely used to assess how social structures influence the spread of diseases. However, their numerical simulation can be computationally heavy, especially for large networks. In this paper, we introduce NEXT-Net, a flexible implementation of the next reaction method for simulating epidemic spreading on both static and temporal weighted networks. We find that NEXT-Net is substantially faster than alternative algorithms while being exact. It permits efficiently simulating epidemics on networks with millions of nodes on a standard computer and allows simulating a broad range of epidemic models, including scenarios in which the network structure changes in response to the epidemic. The algorithm is implemented in C++ and accessible from Python and R, making it an ideal tool for a wide range of applications.

**Key Points:**

1. **Flexible Implementation:** NEXT-Net is designed as a flexible implementation that can be easily adapted to various types of networks.
2. **Speed and Efficiency:** It is faster than alternative algorithms while being exact, allowing efficient simulation on large-scale networks.
3. **Broad Range of Models:** It permits simulating a wide range of epidemic models, including those with temporal changes in the network structure.
4. **User-Friendly Interface:** The algorithm is accessible from Python and R, making it user-friendly for various applications.

**Notable Features:**

- **C++ Implementation:** The implementation is done in C++, which provides speed advantages over alternative languages like Java or Python.
- **Accessibility:** It is accessible from both Python and R, allowing users to use the algorithm on their own projects without needing to learn new programming languages.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: f341d75463616bfd32378a4b4e0cc42af60163d09c8db92aea477f92bbc4a511
feed_title: PLOS Computational Biology
feed_url: https://journals.plos.org/ploscompbiol/feed/atom
date_processed: '2025-09-22T17:07:10.261325'
category: 24-computing
---

by Samuel Cure, Florian G. Pflug, Simone Pigolotti Epidemic models on complex networks are widely used to assess how the social structure of a population affects epidemic spreading. However, their numerical simulation can be computationally heavy, especially for large networks. In this paper, we introduce NEXT-Net: a flexible implementation of the next reaction method for simulating epidemic spreading on both static and temporal weighted networks. We find that NEXT-Net is substantially faster than alternative algorithms, while being exact. It permits, in particular, to efficiently simulate epidemics on networks with millions of nodes on a standard computer. It also permits simulating a broad range of epidemic models on temporal networks, including scenarios in which the network structure changes in response to the epidemic. NEXT-Net is implemented in C++ and accessible from Python and R, thus combining speed with user friendliness. These features make our algorithm an ideal tool for a ...