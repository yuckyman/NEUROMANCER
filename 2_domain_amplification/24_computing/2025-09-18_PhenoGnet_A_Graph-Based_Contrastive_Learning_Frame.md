---
type: note
category: 24-computing
created: 2025-09-18 12:11
modified: 2025-09-18 12:11
tags:
- graph
- contrastive learning
- gene functional interaction networks
- human phenotype ontology
- disease similarity prediction
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_PhenoGnet__A_Graph-Based_Contrastive_Learning_Fram.txt
---


# PhenoGnet: A Graph-Based Contrastive Learning Framework for Disease Similarit...

## summary
PhenoGnet is a novel graph-based contrastive learning framework designed to predict disease similarity by integrating gene functional interaction networks with the Human Phenotype Ontology.

## content
RSS Feed: cs.AI updates on arXiv.org
Source: https://arxiv.org/rss/cs.AI
Link: https://arxiv.org/abs/2509.14037

PhenoGnet: A Graph-Based Contrastive Learning Framework for Disease Similarity Prediction

arXiv:2509.14037v1 Announce Type: cross Abstract: Understanding disease similarity is critical for advancing diagnostics, drug discovery, and personalized treatment strategies. We present PhenoGnet, a novel graph-based contrastive learning framework designed to predict disease similarity by integrating gene functional interaction networks with the Human Phenotype Ontology (HPO). PhenoGnet comprises two key components: an intra-view model that separately encodes gene and phenotype graphs using Graph Convolutional Networks (GCNs) and Graph Attention Networks (GATs), and a cross view model implemented as a shared weight multilayer perceptron (MLP) that aligns gene and phenotype embeddings through contrastive learning. The model is trained using known gene phenotype associations as positive pairs and randomly sampled unrelated pairs as negatives. Diseases are represented by the mean embeddings of their associated genes and/or phenotypes, and pairwise similarity is computed via cosine simil...

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


## Scraped from https://arxiv.org/abs/2509.14037
[2509.14037] PhenoGnet: A Graph-Based Contrastive Learning Framework for Disease Similarity Prediction Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; q-bio &gt; arXiv:2509.14037 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Quantitative Biology > Genomics arXiv:2509.14037 (q-bio) [Submitted on 17 Sep 2025] Title:PhenoGnet: A Graph-Based Contrastive Learning Framework for Disease Similarity Prediction Authors:Ranga Baminiwatte, Kazi Jewel Rana, Aaron J. Masino View a PDF of the paper titled PhenoGnet: A Graph-Based Contrastive Learning Framework for Disease Similarity Prediction, by Ranga Baminiwatte and 2 other authors View PDF HTML (experimental) Abstract:Understanding disease similarity is critical for advancing diagnostics, drug discovery, and personalized treatment strategies. We present PhenoGnet, a novel graph-based contrastive learning framework designed to predict disease similarity by integrating gene functional interaction networks with the Human Phenotype Ontology (HPO). PhenoGnet comprises two key components: an intra-view model that separately encodes gene and phenotype graphs using Graph Convolutional Networks (GCNs) and Graph Attention Networks (GATs), and a cross view model implemented as a shared weight multilayer perceptron (MLP) that aligns gene and phenotype embeddings through contrastive learning. The model is trained using known gene phenotype associations as positive pairs and randomly sampled unrelated pairs as negatives. Diseases are represented by the mean embeddings of their associated genes and/or phenotypes, and pairwise similarity is computed via cosine similarity. Evaluation on a curated benchmark of 1,100 similar a...


## connections
- processed from phone shortcut
