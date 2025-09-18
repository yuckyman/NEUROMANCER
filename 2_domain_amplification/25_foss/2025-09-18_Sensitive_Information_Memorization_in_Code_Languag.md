---
type: note
category: 25-foss
created: 2025-09-18 11:55
modified: 2025-09-18 11:55
tags:
- code
- language models
- privacy
- de-duplication
- unsolicited data
- open-source
- selfhosting
- decentralized
- foss
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_Scrub_It_Out__Erasing_Sensitive_Memorization_in_Co.txt
---


# Sensitive Information Memorization in Code Language Models

## summary
This research proposes methods to mitigate the memorization of sensitive training data by code language models, such as differential privacy and cross-source type. The key idea is that these models can accidentally generate verbatim versions of confidential information when specifically prompted.

## content
RSS Feed: cs.AI updates on arXiv.org
Source: https://arxiv.org/rss/cs.AI
Link: https://arxiv.org/abs/2509.13755

Scrub It Out! Erasing Sensitive Memorization in Code Language Models via Machine Unlearning

arXiv:2509.13755v1 Announce Type: cross Abstract: While Code Language Models (CLMs) have demonstrated superior performance in software engineering tasks such as code generation and summarization, recent empirical studies reveal a critical privacy vulnerability: these models exhibit unintended memorization of sensitive training data, enabling verbatim reproduction of confidential information when specifically prompted. To address this issue, several approaches, including training data de-duplication and differential privacy augmentation, have been proposed. However, these methods require full-model retraining for deployed CLMs, which incurs substantial computational costs. In this paper, we aim to answer the following research question: Can sensitive information memorized by CLMs be erased effectively and efficiently? We conduct a pioneering investigation into erasing sensitive memorization in CLMs through machine unlearning - a post-hoc modification method that removes specific informa...

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


## Scraped from https://arxiv.org/abs/2509.13755
[2509.13755] Scrub It Out! Erasing Sensitive Memorization in Code Language Models via Machine Unlearning Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2509.13755 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Software Engineering arXiv:2509.13755 (cs) [Submitted on 17 Sep 2025] Title:Scrub It Out! Erasing Sensitive Memorization in Code Language Models via Machine Unlearning Authors:Zhaoyang Chu, Yao Wan, Zhikun Zhang, Di Wang, Zhou Yang, Hongyu Zhang, Pan Zhou, Xuanhua Shi, Hai Jin, David Lo View a PDF of the paper titled Scrub It Out! Erasing Sensitive Memorization in Code Language Models via Machine Unlearning, by Zhaoyang Chu and 9 other authors View PDF HTML (experimental) Abstract:While Code Language Models (CLMs) have demonstrated superior performance in software engineering tasks such as code generation and summarization, recent empirical studies reveal a critical privacy vulnerability: these models exhibit unintended memorization of sensitive training data, enabling verbatim reproduction of confidential information when specifically prompted. To address this issue, several approaches, including training data de-duplication and differential privacy augmentation, have been proposed. However, these methods require full-model retraining for deployed CLMs, which incurs substantial computational costs. In this paper, we aim to answer the following research question: Can sensitive information memorized by CLMs be erased effectively and efficiently? We conduct a pioneering investigation into erasing sensitive memorization in CLMs through machine unlearning - a post-hoc modification method that removes specific inf...


## connections
- processed from phone shortcut
