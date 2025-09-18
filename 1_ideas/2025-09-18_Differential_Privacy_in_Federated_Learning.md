---
type: note
category: research
created: 2025-09-18 12:05
modified: 2025-09-18 12:05
tags: ['differential-privacy', 'federated-learning', 'machine-learning', 'distributed-data']
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_Differential_Privacy_in_Federated_Learning__Mitiga.txt
---

# Differential Privacy in Federated Learning

## summary
Federated learning is an extension of federated optimization that allows each client to process its own data. To mitigate inference attacks, this paper proposes randomized response mechanisms for the central server and clients.

## content
RSS Feed: cs.AI updates on arXiv.org
Source: https://arxiv.org/rss/cs.AI
Link: https://arxiv.org/abs/2509.13987

Differential Privacy in Federated Learning: Mitigating Inference Attacks with Randomized Response

arXiv:2509.13987v1 Announce Type: cross Abstract: Machine learning models used for distributed architectures consisting of servers and clients require large amounts of data to achieve high accuracy. Data obtained from clients are collected on a central server for model training. However, storing data on a central server raises concerns about security and privacy. To address this issue, a federated learning architecture has been proposed. In federated learning, each client trains a local model using its own data. The trained models are periodically transmitted to the central server. The server then combines the received models using federated aggregation algorithms to obtain a global model. This global model is distributed back to the clients, and the process continues in a cyclical manner. Although preventing data from leaving the clients enhances security, certain concerns still remain. Attackers can perform inference attacks on the obtained models to approximate the training dataset,...

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


## Scraped from https://arxiv.org/abs/2509.13987
[2509.13987] Differential Privacy in Federated Learning: Mitigating Inference Attacks with Randomized Response Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2509.13987 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Cryptography and Security arXiv:2509.13987 (cs) [Submitted on 17 Sep 2025] Title:Differential Privacy in Federated Learning: Mitigating Inference Attacks with Randomized Response Authors:Ozer Ozturk, Busra Buyuktanir, Gozde Karatas Baydogmus, Kazim Yildiz View a PDF of the paper titled Differential Privacy in Federated Learning: Mitigating Inference Attacks with Randomized Response, by Ozer Ozturk and 3 other authors View PDF HTML (experimental) Abstract:Machine learning models used for distributed architectures consisting of servers and clients require large amounts of data to achieve high accuracy. Data obtained from clients are collected on a central server for model training. However, storing data on a central server raises concerns about security and privacy. To address this issue, a federated learning architecture has been proposed. In federated learning, each client trains a local model using its own data. The trained models are periodically transmitted to the central server. The server then combines the received models using federated aggregation algorithms to obtain a global model. This global model is distributed back to the clients, and the process continues in a cyclical manner. Although preventing data from leaving the clients enhances security, certain concerns still remain. Attackers can perform inference attacks on the obtained models to approximate the training dataset, potentially caus...


## connections
- processed from phone shortcut
