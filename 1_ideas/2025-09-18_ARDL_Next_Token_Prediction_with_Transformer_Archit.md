---
type: note
category: development
created: 2025-09-18 11:56
modified: 2025-09-18 11:56
tags: ['arxiv', 'next-token-prediction', 'transformers', 'proposal']
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_From_Next_Token_Prediction_to__STRIPS__World_Model.txt
---

# ARDL: Next Token Prediction with Transformer Architectures

## summary
An article discussing the application of next token prediction techniques to learning propositional STRIPS world models, using a deep learning architecture (transformers) and gradient descent.

## content
RSS Feed: cs.AI updates on arXiv.org
Source: https://arxiv.org/rss/cs.AI
Link: https://arxiv.org/abs/2509.13389

From Next Token Prediction to (STRIPS) World Models -- Preliminary Results

arXiv:2509.13389v1 Announce Type: new Abstract: We consider the problem of learning propositional STRIPS world models from action traces alone, using a deep learning architecture (transformers) and gradient descent. The task is cast as a supervised next token prediction problem where the tokens are the actions, and an action $a$ may follow an action sequence if the hidden effects of the previous actions do not make an action precondition of $a$ false. We show that a suitable transformer architecture can faithfully represent propositional STRIPS world models, and that the models can be learned from sets of random valid (positive) and invalid (negative) action sequences alone. A number of experiments are reported.

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


## Scraped from https://arxiv.org/abs/2509.13389
[2509.13389] From Next Token Prediction to (STRIPS) World Models -- Preliminary Results Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2509.13389 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Artificial Intelligence arXiv:2509.13389 (cs) [Submitted on 16 Sep 2025] Title:From Next Token Prediction to (STRIPS) World Models -- Preliminary Results Authors:Carlos Núñez-Molina, Vicenç Gómez, Hector Geffner View a PDF of the paper titled From Next Token Prediction to (STRIPS) World Models -- Preliminary Results, by Carlos N\&#39;u\~nez-Molina and 2 other authors View PDF HTML (experimental) Abstract:We consider the problem of learning propositional STRIPS world models from action traces alone, using a deep learning architecture (transformers) and gradient descent. The task is cast as a supervised next token prediction problem where the tokens are the actions, and an action $a$ may follow an action sequence if the hidden effects of the previous actions do not make an action precondition of $a$ false. We show that a suitable transformer architecture can faithfully represent propositional STRIPS world models, and that the models can be learned from sets of random valid (positive) and invalid (negative) action sequences alone. A number of experiments are reported. Comments: 10 pages, 3 figures Subjects: Artificial Intelligence (cs.AI) ACM&nbsp;classes: I.2.4; I.2.6; I.2.8 Cite as: arXiv:2509.13389 [cs.AI] &nbsp; (or arXiv:2509.13389v1 [cs.AI] for this version) &nbsp; https://doi.org/10.48550/arXiv.2509.13389 Focus to learn more arXiv-issued DOI via DataCite (pending registration) Submission history From: Carlos Núñez Molina ...


## connections
- processed from phone shortcut
