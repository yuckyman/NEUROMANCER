---
type: note
category: 24-computing
created: 2025-09-19 17:57
modified: 2025-09-19 17:57
tags:
- cuda
- kernel
- verification
- optimization
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 20250919_175447_rss_Towards_Robust_Agentic_CUDA_Kernel_Benchmarking__V.txt
content_hash: 21f7652b5c327de8900828e0ad5440c13ff61e108c000409daa96d2816d99162
---


# Robust Agentic CUDA Kernel Benchmarking

## summary
This article introduces a new benchmark for evaluating kernel performance and correctness across diverse scenarios, aiming to improve the generalization assessment of CUDA kernels.

## content
RSS Feed: cs.AI updates on arXiv.org
Source: https://arxiv.org/rss/cs.AI
Link: https://arxiv.org/abs/2509.14279

Towards Robust Agentic CUDA Kernel Benchmarking, Verification, and Optimization

arXiv:2509.14279v1 Announce Type: cross Abstract: Recent advances in large language models (LLMs) demonstrate their effectiveness in scaling test-time compute for software engineering tasks. However, these approaches often focus on high-level solutions, with limited attention to optimizing low-level CUDA kernel implementations. Additionally, existing kernel generation benchmarks suffer from exploitable loopholes and insufficient diversity in testing conditions, hindering true generalization assessment. To address these limitations, we introduce robust-kbench, a new benchmark for rigorous evaluation of kernel performance and correctness across varied scenarios. Furthermore, we present a comprehensive agentic framework that automates CUDA kernel discovery, verification, and optimization. This pipeline enables frontier LLMs to translate torch code to CUDA kernels and iteratively improve their runtime within our robust evaluation setting. Our sequential workflow first translates PyTorch co...

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


## Scraped from https://arxiv.org/abs/2509.14279
[2509.14279] Towards Robust Agentic CUDA Kernel Benchmarking, Verification, and Optimization Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2509.14279 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Software Engineering arXiv:2509.14279 (cs) [Submitted on 16 Sep 2025] Title:Towards Robust Agentic CUDA Kernel Benchmarking, Verification, and Optimization Authors:Robert Tjarko Lange, Qi Sun, Aaditya Prasad, Maxence Faldor, Yujin Tang, David Ha View a PDF of the paper titled Towards Robust Agentic CUDA Kernel Benchmarking, Verification, and Optimization, by Robert Tjarko Lange and 5 other authors View PDF Abstract:Recent advances in large language models (LLMs) demonstrate their effectiveness in scaling test-time compute for software engineering tasks. However, these approaches often focus on high-level solutions, with limited attention to optimizing low-level CUDA kernel implementations. Additionally, existing kernel generation benchmarks suffer from exploitable loopholes and insufficient diversity in testing conditions, hindering true generalization assessment. To address these limitations, we introduce robust-kbench, a new benchmark for rigorous evaluation of kernel performance and correctness across varied scenarios. Furthermore, we present a comprehensive agentic framework that automates CUDA kernel discovery, verification, and optimization. This pipeline enables frontier LLMs to translate torch code to CUDA kernels and iteratively improve their runtime within our robust evaluation setting. Our sequential workflow first translates PyTorch code into equivalent CUDA kernels. It then optimizes their runtime using a no...


## connections
- processed from phone shortcut
