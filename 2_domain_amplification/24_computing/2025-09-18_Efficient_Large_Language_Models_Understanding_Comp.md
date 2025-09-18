---
type: note
category: 24-computing
created: 2025-09-18 12:04
modified: 2025-09-18 12:04
tags:
- LLM
- arXiv
- algorithmic complexity
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_Reasoning_Efficiently_Through_Adaptive_Chain-of-Th.txt
---


# Efficient Large Language Models: Understanding Computational Costs

## summary
This paper explores the computational efficiency of Large Language Models (LLMs) by analyzing their CoT reasoning capabilities. The study shows that while long outputs can improve accuracy and robustness, excessive reasoning often leads to truncation, decreased accuracy, and latency exceeding five times for successful outputs.

## content
RSS Feed: cs.AI updates on arXiv.org
Source: https://arxiv.org/rss/cs.AI
Link: https://arxiv.org/abs/2509.14093

Reasoning Efficiently Through Adaptive Chain-of-Thought Compression: A Self-Optimizing Framework

arXiv:2509.14093v1 Announce Type: cross Abstract: Chain-of-Thought (CoT) reasoning enhances Large Language Models (LLMs) by prompting intermediate steps, improving accuracy and robustness in arithmetic, logic, and commonsense tasks. However, this benefit comes with high computational costs: longer outputs increase latency, memory usage, and KV-cache demands. These issues are especially critical in software engineering tasks where concise and deterministic outputs are required. To investigate these trade-offs, we conduct an empirical study based on code generation benchmarks. The results reveal that longer CoT does not always help. Excessive reasoning often causes truncation, accuracy drops, and latency up to five times higher, with failed outputs consistently longer than successful ones. These findings challenge the assumption that longer reasoning is inherently better and highlight the need for adaptive CoT control. Motivated by this, we propose SEER (Self-Enhancing Efficient Reasonin...

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


## Scraped from https://arxiv.org/abs/2509.14093
[2509.14093] Reasoning Efficiently Through Adaptive Chain-of-Thought Compression: A Self-Optimizing Framework Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2509.14093 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Software Engineering arXiv:2509.14093 (cs) [Submitted on 17 Sep 2025] Title:Reasoning Efficiently Through Adaptive Chain-of-Thought Compression: A Self-Optimizing Framework Authors:Kerui Huang, Shuhan Liu, Xing Hu, Tongtong Xu, Lingfeng Bao, Xin Xia View a PDF of the paper titled Reasoning Efficiently Through Adaptive Chain-of-Thought Compression: A Self-Optimizing Framework, by Kerui Huang and 5 other authors View PDF HTML (experimental) Abstract:Chain-of-Thought (CoT) reasoning enhances Large Language Models (LLMs) by prompting intermediate steps, improving accuracy and robustness in arithmetic, logic, and commonsense tasks. However, this benefit comes with high computational costs: longer outputs increase latency, memory usage, and KV-cache demands. These issues are especially critical in software engineering tasks where concise and deterministic outputs are required. To investigate these trade-offs, we conduct an empirical study based on code generation benchmarks. The results reveal that longer CoT does not always help. Excessive reasoning often causes truncation, accuracy drops, and latency up to five times higher, with failed outputs consistently longer than successful ones. These findings challenge the assumption that longer reasoning is inherently better and highlight the need for adaptive CoT control. Motivated by this, we propose SEER (Self-Enhancing Efficient Reasoning), an adaptive framework...


## connections
- processed from phone shortcut
