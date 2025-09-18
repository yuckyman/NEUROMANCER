---
type: note
category: development
created: 2025-09-18 11:51
modified: 2025-09-18 11:51
tags: ['derivative-informed', 'neural operators', 'subsurface fluid-flow']
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_A_reduced-order_derivative-informed_neural_operato.txt
---

# Reduced-Order Derivative-Informed Neural Operator for Subsurface Fluid-Flow S...

## summary
This note presents a reduced-order derivative-informed neural operator (R-DOI) for subsurface fluid-flow simulations. The key contribution is the use of explicit Jacobians to enhance the accuracy of surrogate models without compromising computational efficiency.

## content
RSS Feed: cs.AI updates on arXiv.org
Source: https://arxiv.org/rss/cs.AI
Link: https://arxiv.org/abs/2509.13620

A reduced-order derivative-informed neural operator for subsurface fluid-flow

arXiv:2509.13620v1 Announce Type: cross Abstract: Neural operators have emerged as cost-effective surrogates for expensive fluid-flow simulators, particularly in computationally intensive tasks such as permeability inversion from time-lapse seismic data, and uncertainty quantification. In these applications, the fidelity of the surrogate's gradients with respect to system parameters is crucial, as the accuracy of downstream tasks, such as optimization and Bayesian inference, relies directly on the quality of the derivative information. Recent advances in physics-informed methods have leveraged derivative information to improve surrogate accuracy. However, incorporating explicit Jacobians can become computationally prohibitive, as the complexity typically scales quadratically with the number of input parameters. To address this limitation, we propose DeFINO (Derivative-based Fisher-score Informed Neural Operator), a reduced-order, derivative-informed training framework. DeFINO integrate...

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


## Scraped from https://arxiv.org/abs/2509.13620
[2509.13620] A reduced-order derivative-informed neural operator for subsurface fluid-flow Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; physics &gt; arXiv:2509.13620 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Physics > Computational Physics arXiv:2509.13620 (physics) [Submitted on 17 Sep 2025] Title:A reduced-order derivative-informed neural operator for subsurface fluid-flow Authors:Jeongjin (Jayjay)Park, Grant Bruer, Huseyin Tuna Erdinc, Abhinav Prakash Gahlot, Felix J. Herrmann View a PDF of the paper titled A reduced-order derivative-informed neural operator for subsurface fluid-flow, by Jeongjin (Jayjay) Park and 4 other authors View PDF HTML (experimental) Abstract:Neural operators have emerged as cost-effective surrogates for expensive fluid-flow simulators, particularly in computationally intensive tasks such as permeability inversion from time-lapse seismic data, and uncertainty quantification. In these applications, the fidelity of the surrogate&#39;s gradients with respect to system parameters is crucial, as the accuracy of downstream tasks, such as optimization and Bayesian inference, relies directly on the quality of the derivative information. Recent advances in physics-informed methods have leveraged derivative information to improve surrogate accuracy. However, incorporating explicit Jacobians can become computationally prohibitive, as the complexity typically scales quadratically with the number of input parameters. To address this limitation, we propose DeFINO (Derivative-based Fisher-score Informed Neural Operator), a reduced-order, derivative-informed training framework. DeFINO integrates Fourier neural operators (FNOs) w...


## connections
- processed from phone shortcut
