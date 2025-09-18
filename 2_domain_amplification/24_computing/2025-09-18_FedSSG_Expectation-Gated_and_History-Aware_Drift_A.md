---
type: note
category: 24-computing
created: 2025-09-18 12:10
modified: 2025-09-18 12:10
tags:
- dev-log
- project
- research
- idea
- technical
- personal
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_FedSSG__Expectation-Gated_and_History-Aware_Drift_.txt
---


# FedSSG: Expectation-Gated and History-Aware Drift Alignment for Federated Lea...

## summary
FedSSG is a stochastic sampling-guided, history-aware drift alignment method for federated learning. It maintains a per-client drift memory that accumulates local model differences as a lightweight sketch of historical gradients, gates both the memory update and the local alignment term by a smooth function of observed/expected participation ratio.

## content
RSS Feed: cs.AI updates on arXiv.org
Source: https://arxiv.org/rss/cs.AI
Link: https://arxiv.org/abs/2509.13895

FedSSG: Expectation-Gated and History-Aware Drift Alignment for Federated Learning

arXiv:2509.13895v1 Announce Type: cross Abstract: Non-IID data and partial participation induce client drift and inconsistent local optima in federated learning, causing unstable convergence and accuracy loss. We present FedSSG, a stochastic sampling-guided, history-aware drift alignment method. FedSSG maintains a per-client drift memory that accumulates local model differences as a lightweight sketch of historical gradients; crucially, it gates both the memory update and the local alignment term by a smooth function of the observed/expected participation ratio (a phase-by-expectation signal derived from the server sampler). This statistically grounded gate stays weak and smooth when sampling noise dominates early, then strengthens once participation statistics stabilize, contracting the local-global gap without extra communication. Across CIFAR-10/100 with 100/500 clients and 2-15 percent participation, FedSSG consistently outperforms strong drift-aware baselines and accelerates conve...

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


## Scraped from https://arxiv.org/abs/2509.13895
[2509.13895] FedSSG: Expectation-Gated and History-Aware Drift Alignment for Federated Learning Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2509.13895 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Machine Learning arXiv:2509.13895 (cs) [Submitted on 17 Sep 2025] Title:FedSSG: Expectation-Gated and History-Aware Drift Alignment for Federated Learning Authors:Zhanting Zhou, Jinshan Lai, Fengchun Zhang, Zeqin Wu, Fengli Zhang View a PDF of the paper titled FedSSG: Expectation-Gated and History-Aware Drift Alignment for Federated Learning, by Zhanting Zhou and Jinshan Lai and Fengchun Zhang and Zeqin Wu and Fengli Zhang View PDF HTML (experimental) Abstract:Non-IID data and partial participation induce client drift and inconsistent local optima in federated learning, causing unstable convergence and accuracy loss. We present FedSSG, a stochastic sampling-guided, history-aware drift alignment method. FedSSG maintains a per-client drift memory that accumulates local model differences as a lightweight sketch of historical gradients; crucially, it gates both the memory update and the local alignment term by a smooth function of the observed/expected participation ratio (a phase-by-expectation signal derived from the server sampler). This statistically grounded gate stays weak and smooth when sampling noise dominates early, then strengthens once participation statistics stabilize, contracting the local-global gap without extra communication. Across CIFAR-10/100 with 100/500 clients and 2-15 percent participation, FedSSG consistently outperforms strong drift-aware baselines and accelerates convergence; on our benchmarks ...


## connections
- processed from phone shortcut
