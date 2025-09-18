---
type: note
category: 24-computing
created: 2025-09-18 12:03
modified: 2025-09-18 12:03
tags:
- state space models
- graph learning
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_State_Space_Models_over_Directed_Graphs.txt
---


# State Space Models over Directed Graphs

## summary
Directed graphs are ubiquitous across numerous domains, where the directionality of edges encodes critical causal dependencies. Existing GNNs and graph Transformers face challenges in capturing long-range causal dependencies and balancing accuracy and efficiency when processing large-scale graph datasets.

## content
RSS Feed: cs.AI updates on arXiv.org
Source: https://arxiv.org/rss/cs.AI
Link: https://arxiv.org/abs/2509.13735

State Space Models over Directed Graphs

arXiv:2509.13735v1 Announce Type: cross Abstract: Directed graphs are ubiquitous across numerous domains, where the directionality of edges encodes critical causal dependencies. However, existing GNNs and graph Transformers tailored for directed graphs face two major challenges: (1) effectively capturing long-range causal dependencies derived from directed edges; (2) balancing accuracy and training efficiency when processing large-scale graph datasets. In recent years, state space models (SSMs) have achieved substantial progress in causal sequence tasks, and their variants designed for graphs have demonstrated state-of-the-art accuracy while maintaining high efficiency across various graph learning benchmarks. However, existing graph state space models are exclusively designed for undirected graphs, which limits their performance in directed graph learning. To this end, we propose an innovative approach DirEgo2Token which sequentializes directed graphs via k-hop ego graphs. This marks ...

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


## Scraped from https://arxiv.org/abs/2509.13735
[2509.13735] State Space Models over Directed Graphs Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2509.13735 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Machine Learning arXiv:2509.13735 (cs) [Submitted on 17 Sep 2025] Title:State Space Models over Directed Graphs Authors:Junzhi She, Xunkai Li, Rong-Hua Li, Guoren Wang View a PDF of the paper titled State Space Models over Directed Graphs, by Junzhi She and 3 other authors View PDF HTML (experimental) Abstract:Directed graphs are ubiquitous across numerous domains, where the directionality of edges encodes critical causal dependencies. However, existing GNNs and graph Transformers tailored for directed graphs face two major challenges: (1) effectively capturing long-range causal dependencies derived from directed edges; (2) balancing accuracy and training efficiency when processing large-scale graph datasets. In recent years, state space models (SSMs) have achieved substantial progress in causal sequence tasks, and their variants designed for graphs have demonstrated state-of-the-art accuracy while maintaining high efficiency across various graph learning benchmarks. However, existing graph state space models are exclusively designed for undirected graphs, which limits their performance in directed graph learning. To this end, we propose an innovative approach DirEgo2Token which sequentializes directed graphs via k-hop ego graphs. This marks the first systematic extension of state space models to the field of directed graph learning. Building upon this, we develop DirGraphSSM, a novel directed graph neural network architecture that implements state space model...


## connections
- processed from phone shortcut
