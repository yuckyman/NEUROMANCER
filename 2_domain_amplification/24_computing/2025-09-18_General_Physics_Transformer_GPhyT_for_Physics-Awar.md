---
type: note
category: 24-computing
created: 2025-09-18 12:06
modified: 2025-09-18 12:06
tags:
- transformers
- machine learning
- physics
- research
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_Towards_a_Physics_Foundation_Model.txt
---


# General Physics Transformer (GPhyT) for Physics-Aware Machine Learning

## summary
The GPhyT is a transformer-based model that trains on diverse simulation data and demonstrates foundation model capabilities, making physics-aware machine learning accessible for all.

## content
RSS Feed: cs.AI updates on arXiv.org
Source: https://arxiv.org/rss/cs.AI
Link: https://arxiv.org/abs/2509.13805

Towards a Physics Foundation Model

arXiv:2509.13805v1 Announce Type: cross Abstract: Foundation models have revolutionized natural language processing through a ``train once, deploy anywhere'' paradigm, where a single pre-trained model adapts to countless downstream tasks without retraining. Access to a Physics Foundation Model (PFM) would be transformative -- democratizing access to high-fidelity simulations, accelerating scientific discovery, and eliminating the need for specialized solver development. Yet current physics-aware machine learning approaches remain fundamentally limited to single, narrow domains and require retraining for each new system. We present the General Physics Transformer (GPhyT), trained on 1.8 TB of diverse simulation data, that demonstrates foundation model capabilities are achievable for physics. Our key insight is that transformers can learn to infer governing dynamics from context, enabling a single model to simulate fluid-solid interactions, shock waves, thermal convection, and multi-phas...

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


## Scraped from https://arxiv.org/abs/2509.13805
[2509.13805] Towards a Physics Foundation Model Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2509.13805 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Machine Learning arXiv:2509.13805 (cs) [Submitted on 17 Sep 2025] Title:Towards a Physics Foundation Model Authors:Florian Wiesner, Matthias Wessling, Stephen Baek View a PDF of the paper titled Towards a Physics Foundation Model, by Florian Wiesner and 2 other authors View PDF HTML (experimental) Abstract:Foundation models have revolutionized natural language processing through a ``train once, deploy anywhere&#39;&#39; paradigm, where a single pre-trained model adapts to countless downstream tasks without retraining. Access to a Physics Foundation Model (PFM) would be transformative -- democratizing access to high-fidelity simulations, accelerating scientific discovery, and eliminating the need for specialized solver development. Yet current physics-aware machine learning approaches remain fundamentally limited to single, narrow domains and require retraining for each new system. We present the General Physics Transformer (GPhyT), trained on 1.8 TB of diverse simulation data, that demonstrates foundation model capabilities are achievable for physics. Our key insight is that transformers can learn to infer governing dynamics from context, enabling a single model to simulate fluid-solid interactions, shock waves, thermal convection, and multi-phase dynamics without being told the underlying equations. GPhyT achieves three critical breakthroughs: (1) superior performance across multiple physics domains, outperforming specialized architectures by up to 29x, (2) zero-s...


## connections
- processed from phone shortcut
