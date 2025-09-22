---
title: Defeating Nondeterminism in LLM Inference
link: https://simonwillison.net/2025/Sep/11/defeating-nondeterminism/#atom-everything
summary: 'Error communicating with Ollama API: 404 Client Error: Not Found for url:
  http://localhost:11434/api/generate'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 4e999547152d1aae1002485ba48b8cc762a1fed1b9a8c4c9eb21d55af712ab0f
feed_title: Simon Willison's Weblog
feed_url: https://simonwillison.net/atom/everything/
date_processed: '2025-09-22T17:07:12.274219'
category: 24-computing
---

Defeating Nondeterminism in LLM Inference A very common question I see about LLMs concerns why they can't be made to deliver the same response to the same prompt by setting a fixed random number seed. Like many others I had been lead to believe this was due to the non-associative nature of floating point arithmetic, where (a + b) + c ≠ a + (b + c), combining with unpredictable calculation orders on concurrent GPUs. This new paper calls that the "concurrency + floating point hypothesis": One common hypothesis is that some combination of floating-point non-associativity and concurrent execution leads to nondeterminism based on which concurrent core finishes first. We will call this the “concurrency + floating point” hypothesis for LLM inference nondeterminism. It then convincingly argues that this is not the core of the problem, because "in the typical forward pass of an LLM, there is usually not a single atomic add present." Why are LLMs so often non-deterministic then? [...] the primar...