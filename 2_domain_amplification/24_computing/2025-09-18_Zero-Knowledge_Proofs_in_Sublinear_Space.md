---
type: note
category: 24-computing
created: 2025-09-18 11:53
modified: 2025-09-18 11:53
tags:
- zero-knowledge-proofs
- sublinear-space
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_Zero-Knowledge_Proofs_in_Sublinear_Space.txt
---


# Zero-Knowledge Proofs in Sublinear Space

## summary
We present a new proof system for proving the correctness of computations without revealing private information, achieving sublinear memory requirements. Our approach processes computations in blocks using a space-efficient tree algorithm and reduces memory from linear scaling to square-root scaling.

## content
RSS Feed: cs.AI updates on arXiv.org
Source: https://arxiv.org/rss/cs.AI
Link: https://arxiv.org/abs/2509.05326

Zero-Knowledge Proofs in Sublinear Space

arXiv:2509.05326v2 Announce Type: replace-cross Abstract: Zero-knowledge proofs allow verification of computations without revealing private information. However, existing systems require memory proportional to the computation size, which has historically limited use in large-scale applications and on mobile and edge devices. We solve this fundamental bottleneck by developing, to our knowledge, the first proof system with sublinear memory requirements for mainstream cryptographic constructions. Our approach processes computations in blocks using a space-efficient tree algorithm, reducing memory from linear scaling to square-root scaling--from $\Theta(T)$ to $O(\sqrt{T} + \log T \log\log T)$ for computation size $T$--while maintaining the same proof generation time through a constant number of streaming passes. For widely-used linear polynomial commitment schemes (KZG/IPA), our method produces identical proofs and verification when using the same parameters and hashing only aggregate co...

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


## Scraped from https://arxiv.org/abs/2509.05326
[2509.05326] Zero-Knowledge Proofs in Sublinear Space Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2509.05326 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Cryptography and Security arXiv:2509.05326 (cs) [Submitted on 30 Aug 2025 (v1), last revised 17 Sep 2025 (this version, v2)] Title:Zero-Knowledge Proofs in Sublinear Space Authors:Logan Nye View a PDF of the paper titled Zero-Knowledge Proofs in Sublinear Space, by Logan Nye View PDF HTML (experimental) Abstract:Zero-knowledge proofs allow verification of computations without revealing private information. However, existing systems require memory proportional to the computation size, which has historically limited use in large-scale applications and on mobile and edge devices. We solve this fundamental bottleneck by developing, to our knowledge, the first proof system with sublinear memory requirements for mainstream cryptographic constructions. Our approach processes computations in blocks using a space-efficient tree algorithm, reducing memory from linear scaling to square-root scaling--from $\Theta(T)$ to $O(\sqrt{T} + \log T \log\log T)$ for computation size $T$--while maintaining the same proof generation time through a constant number of streaming passes. For widely-used linear polynomial commitment schemes (KZG/IPA), our method produces identical proofs and verification when using the same parameters and hashing only aggregate commitments into the challenge generation, preserving proof size and security. Hash-based systems also achieve square-root memory scaling though with slightly different proof structures. This advance enables zero-knowledge proofs...


## connections
- processed from phone shortcut
