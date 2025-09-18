---
type: note
category: 24-computing
created: 2025-09-18 11:51
modified: 2025-09-18 11:51
tags:
- physics-informed
- deep-learning
- neural-networks
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_Self-adaptive_weights_based_on_balanced_residual_d.txt
---


# Physics-Informed Neural Networks and Deep Operator Networks

## summary
We present a novel approach to train physics-informed neural networks and deep operator networks. The method balances residual decay rates across different training points, leading to improved convergence rates and enhanced performance.

## content
RSS Feed: cs.AI updates on arXiv.org
Source: https://arxiv.org/rss/cs.AI
Link: https://arxiv.org/abs/2407.01613

Self-adaptive weights based on balanced residual decay rate for physics-informed neural networks and deep operator networks

arXiv:2407.01613v2 Announce Type: replace-cross Abstract: Physics-informed deep learning has emerged as a promising alternative for solving partial differential equations. However, for complex problems, training these networks can still be challenging, often resulting in unsatisfactory accuracy and efficiency. In this work, we demonstrate that the failure of plain physics-informed neural networks arises from the significant discrepancy in the convergence rate of residuals at different training points, where the slowest convergence rate dominates the overall solution convergence. Based on these observations, we propose a pointwise adaptive weighting method that balances the residual decay rate across different training points. The performance of our proposed adaptive weighting method is compared with current state-of-the-art adaptive weighting methods on benchmark problems for both physics-informed neural networks and physics-informed deep operator networks. Through extensive numerical ...

## Scraped from https://arxiv.org/rss/cs.AI
<?xml version='1.0' encoding='UTF-8'?>
<rss xmlns:arxiv="http://arxiv.org/schemas/atom" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:content="http://purl.org/rss/1.0/modules/content/" version="2.0">
  <channel>
    <title>cs.AI updates on arXiv.org</title>
    <link>http://rss.arxiv.org/rss/cs.AI</link>
    <description>cs.AI updates on the arXiv.org e-print archive.</description>
    <atom:link href="http://rss.arxiv.org/rss/cs.AI" rel="self" type="application/rss+xml"/>
    <docs>http://www.rssboard.org/rss-specification</docs>
    <language>en-us</language>
    <lastBuildDate>Thu, 18 Sep 2025 04:00:02 +0000</lastBuildDate>
    <managingEditor>rss-help@arxiv.org</managingEditor>
    <pubDate>Thu, 18 Sep 2025 00:00:00 -0400</pubDate>
    <skipDays>
      <day>Sunday</day>
      <day>Saturday</day>
    </skipDays>
    <item>
      <title>Explicit Reasoning Makes Better Judges: A Systematic Study on Accuracy, Efficiency, and Robustness</title>
      <link>https://arxiv.org/abs/2509.13332</link>
      <description>arXiv:2509.13332v1 Announce Type: new 
Abstract: As Large Language Models (LLMs) are increasingly adopted as automated judges in benchmarking and reward modeling, ensuring their reliability, efficiency, and robustness has become critical. In this work, we present a systematic comparison of "thinking" and "non-thinking" LLMs in the LLM-as-a-judge paradigm using open-source Qwen 3 models of relatively small sizes (0.6B, 1.7B, and 4B parameters). We evaluate both accuracy and computational efficiency (FLOPs) on RewardBench tasks, and further examine augmentation strategies for non-thinking models, including in-context learning, rubric-guided judging, reference-based evaluation, and n-best aggregation. Our results show that despite these enhancements, non-thinking models generally fall short of their thinking counterparts. Our results show that thinking models achieve approximately 10% points higher accuracy with lit...


## Scraped from https://arxiv.org/abs/2407.01613
[2407.01613] Self-adaptive weights based on balanced residual decay rate for physics-informed neural networks and deep operator networks Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2407.01613 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Machine Learning arXiv:2407.01613 (cs) [Submitted on 28 Jun 2024 (v1), last revised 16 Sep 2025 (this version, v2)] Title:Self-adaptive weights based on balanced residual decay rate for physics-informed neural networks and deep operator networks Authors:Wenqian Chen, Amanda A. Howard, Panos Stinis View a PDF of the paper titled Self-adaptive weights based on balanced residual decay rate for physics-informed neural networks and deep operator networks, by Wenqian Chen and 2 other authors View PDF HTML (experimental) Abstract:Physics-informed deep learning has emerged as a promising alternative for solving partial differential equations. However, for complex problems, training these networks can still be challenging, often resulting in unsatisfactory accuracy and efficiency. In this work, we demonstrate that the failure of plain physics-informed neural networks arises from the significant discrepancy in the convergence rate of residuals at different training points, where the slowest convergence rate dominates the overall solution convergence. Based on these observations, we propose a pointwise adaptive weighting method that balances the residual decay rate across different training points. The performance of our proposed adaptive weighting method is compared with current state-of-the-art adaptive weighting methods on benchmark problems for both physics-informed neural networks an...


## connections
- processed from phone shortcut
