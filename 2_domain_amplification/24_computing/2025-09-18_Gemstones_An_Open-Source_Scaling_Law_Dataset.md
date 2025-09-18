---
type: note
category: 24-computing
created: 2025-09-18 12:04
modified: 2025-09-18 12:04
tags:
- scaling-laws
- gemstones
- model-suite
- transformers
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_Gemstones__A_Model_Suite_for_Multi-Faceted_Scaling.txt
---


# Gemstones: An Open-Source Scaling Law Dataset

## summary
A dataset of checkpoints from transformers with different architectural shapes and hyperparameters, enabling more complex studies of scaling laws.

## content
RSS Feed: cs.AI updates on arXiv.org
Source: https://arxiv.org/rss/cs.AI
Link: https://arxiv.org/abs/2502.06857

Gemstones: A Model Suite for Multi-Faceted Scaling Laws

arXiv:2502.06857v2 Announce Type: replace-cross Abstract: Scaling laws are typically fit using a family of models with a narrow range of frozen hyper-parameter choices. In this work we study scaling laws using multiple architectural shapes and hyperparameter choices, highlighting their impact on resulting prescriptions. As a primary artifact of our research, we release the Gemstones: an open-source scaling law dataset, consisting of over 4000 checkpoints from transformers with up to 2 billion parameters and diverse architectural shapes; including ablations over learning rate and cooldown. Our checkpoints enable more complex studies of scaling, such as analyzing the relationship between width and depth. By examining our model suite, we find that the prescriptions of scaling laws can be highly sensitive to the experimental design process and the specific model checkpoints used during fitting.

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


## Scraped from https://arxiv.org/abs/2502.06857
[2502.06857] Gemstones: A Model Suite for Multi-Faceted Scaling Laws Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2502.06857 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Machine Learning arXiv:2502.06857 (cs) [Submitted on 7 Feb 2025 (v1), last revised 16 Sep 2025 (this version, v2)] Title:Gemstones: A Model Suite for Multi-Faceted Scaling Laws Authors:Sean McLeish, John Kirchenbauer, David Yu Miller, Siddharth Singh, Abhinav Bhatele, Micah Goldblum, Ashwinee Panda, Tom Goldstein View a PDF of the paper titled Gemstones: A Model Suite for Multi-Faceted Scaling Laws, by Sean McLeish and 7 other authors View PDF HTML (experimental) Abstract:Scaling laws are typically fit using a family of models with a narrow range of frozen hyper-parameter choices. In this work we study scaling laws using multiple architectural shapes and hyperparameter choices, highlighting their impact on resulting prescriptions. As a primary artifact of our research, we release the Gemstones: an open-source scaling law dataset, consisting of over 4000 checkpoints from transformers with up to 2 billion parameters and diverse architectural shapes; including ablations over learning rate and cooldown. Our checkpoints enable more complex studies of scaling, such as analyzing the relationship between width and depth. By examining our model suite, we find that the prescriptions of scaling laws can be highly sensitive to the experimental design process and the specific model checkpoints used during fitting. Subjects: Machine Learning (cs.LG); Artificial Intelligence (cs.AI) Cite as: arXiv:2502.06857 [cs.LG] &nbsp; (or arXiv:2502.06857v2 [cs.LG] for t...


## connections
- processed from phone shortcut
