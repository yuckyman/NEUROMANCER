---
type: note
category: 24-computing
created: 2025-09-19 17:56
modified: 2025-09-19 17:56
tags:
- deception
- large language models
- representation flips
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_When_Truthful_Representations_Flip_Under_Deceptive.txt
content_hash: ef9b2d81bcef238ed6cd7322e121585cd1a9f7a757491c6c1cc5baec490ac8ff
---


# Understanding Deceptive Instructions in Large Language Models

## summary
We investigate when and how deceptive instructions affect the internal representations of large language models like LLMs. We analyze two models: Llama-3.1-8B-Instruct and Gemma-2-9B-Instruct. Our findings suggest that truthful/neutral instructions do not necessarily lead to a flip in the model's instructed True/False output, but they may affect its truthful representation more than deception.

## content
RSS Feed: cs.AI updates on arXiv.org
Source: https://arxiv.org/rss/cs.AI
Link: https://arxiv.org/abs/2507.22149

When Truthful Representations Flip Under Deceptive Instructions?

arXiv:2507.22149v2 Announce Type: replace Abstract: Large language models (LLMs) tend to follow maliciously crafted instructions to generate deceptive responses, posing safety challenges. How deceptive instructions alter the internal representations of LLM compared to truthful ones remains poorly understood beyond output analysis. To bridge this gap, we investigate when and how these representations ``flip'', such as from truthful to deceptive, under deceptive versus truthful/neutral instructions. Analyzing the internal representations of Llama-3.1-8B-Instruct and Gemma-2-9B-Instruct on a factual verification task, we find the model's instructed True/False output is predictable via linear probes across all conditions based on the internal representation. Further, we use Sparse Autoencoders (SAEs) to show that the Deceptive instructions induce significant representational shifts compared to Truthful/Neutral representations (which are similar), concentrated in early-to-mid layers and det...

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
    <lastBuildDate>Fri, 19 Sep 2025 04:00:15 +0000</lastBuildDate>
    <managingEditor>rss-help@arxiv.org</managingEditor>
    <pubDate>Fri, 19 Sep 2025 00:00:00 -0400</pubDate>
    <skipDays>
      <day>Sunday</day>
      <day>Saturday</day>
    </skipDays>
    <item>
      <title>Unified Crew Planning and Replanning Optimization in Multi-Line Metro Systems Considering Workforce Heterogeneity</title>
      <link>https://arxiv.org/abs/2509.14251</link>
      <description>arXiv:2509.14251v1 Announce Type: new 
Abstract: Metro crew planning is a key component of smart city development as it directly impacts the operational efficiency and service reliability of public transportation. With the rapid expansion of metro networks, effective multi-line scheduling and emergency management have become essential for large-scale seamless operations. However, current research focuses primarily on individual metro lines,with insufficient attention on cross-line coordination and rapid replanning during disruptions. Here, a unified optimization framework is presented for multi-line metro crew planning and replanning with heterogeneous workforce. Specifically, a hierarchical time-space network model is proposed to represent the unified crew action space, and computationally efficient constraints and formulations are derived for the crew's heterogeneous qualifications and preference...


## Scraped from https://arxiv.org/abs/2507.22149
[2507.22149] When Truthful Representations Flip Under Deceptive Instructions? Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2507.22149 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Artificial Intelligence arXiv:2507.22149 (cs) [Submitted on 29 Jul 2025 (v1), last revised 16 Sep 2025 (this version, v2)] Title:When Truthful Representations Flip Under Deceptive Instructions? Authors:Xianxuan Long, Yao Fu, Runchao Li, Mu Sheng, Haotian Yu, Xiaotian Han, Pan Li View a PDF of the paper titled When Truthful Representations Flip Under Deceptive Instructions?, by Xianxuan Long and 6 other authors View PDF HTML (experimental) Abstract:Large language models (LLMs) tend to follow maliciously crafted instructions to generate deceptive responses, posing safety challenges. How deceptive instructions alter the internal representations of LLM compared to truthful ones remains poorly understood beyond output analysis. To bridge this gap, we investigate when and how these representations ``flip&#39;&#39;, such as from truthful to deceptive, under deceptive versus truthful/neutral instructions. Analyzing the internal representations of Llama-3.1-8B-Instruct and Gemma-2-9B-Instruct on a factual verification task, we find the model&#39;s instructed True/False output is predictable via linear probes across all conditions based on the internal representation. Further, we use Sparse Autoencoders (SAEs) to show that the Deceptive instructions induce significant representational shifts compared to Truthful/Neutral representations (which are similar), concentrated in early-to-mid layers and detectable even on complex datasets. We also ident...


## connections
- processed from phone shortcut
