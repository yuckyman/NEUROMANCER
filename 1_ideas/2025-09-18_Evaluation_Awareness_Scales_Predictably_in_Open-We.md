---
type: note
category: development
created: 2025-09-18 12:01
modified: 2025-09-18 12:01
tags: ['large-language-models', 'evaluation-awareness']
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_Evaluation_Awareness_Scales_Predictably_in_Open-We.txt
---

# Evaluation Awareness Scales Predictably in Open-Weights Large Language Models

## summary
We investigated evaluation awareness across different model sizes from $0.27$B to $70$B parameters using linear probing on steering vector activations. Our findings reveal a clear power-law scaling: as model size increases, evaluation awareness improves predictively.

## content
RSS Feed: cs.AI updates on arXiv.org
Source: https://arxiv.org/rss/cs.AI
Link: https://arxiv.org/abs/2509.13333

Evaluation Awareness Scales Predictably in Open-Weights Large Language Models

arXiv:2509.13333v1 Announce Type: new Abstract: Large language models (LLMs) can internally distinguish between evaluation and deployment contexts, a behaviour known as \emph{evaluation awareness}. This undermines AI safety evaluations, as models may conceal dangerous capabilities during testing. Prior work demonstrated this in a single $70$B model, but the scaling relationship across model sizes remains unknown. We investigate evaluation awareness across $15$ models scaling from $0.27$B to $70$B parameters from four families using linear probing on steering vector activations. Our results reveal a clear power-law scaling: evaluation awareness increases predictably with model size. This scaling law enables forecasting deceptive behavior in future larger models and guides the design of scale-aware evaluation strategies for AI safety. A link to the implementation of this paper can be found at https://anonymous.4open.science/r/evaluation-awareness-scaling-laws/README.md.

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


## Scraped from https://arxiv.org/abs/2509.13333
[2509.13333] Evaluation Awareness Scales Predictably in Open-Weights Large Language Models Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2509.13333 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Artificial Intelligence arXiv:2509.13333 (cs) [Submitted on 10 Sep 2025] Title:Evaluation Awareness Scales Predictably in Open-Weights Large Language Models Authors:Maheep Chaudhary, Ian Su, Nikhil Hooda, Nishith Shankar, Julia Tan, Kevin Zhu, Ashwinee Panda, Ryan Lagasse, Vasu Sharma View a PDF of the paper titled Evaluation Awareness Scales Predictably in Open-Weights Large Language Models, by Maheep Chaudhary and 8 other authors View PDF HTML (experimental) Abstract:Large language models (LLMs) can internally distinguish between evaluation and deployment contexts, a behaviour known as \emph{evaluation awareness}. This undermines AI safety evaluations, as models may conceal dangerous capabilities during testing. Prior work demonstrated this in a single $70$B model, but the scaling relationship across model sizes remains unknown. We investigate evaluation awareness across $15$ models scaling from $0.27$B to $70$B parameters from four families using linear probing on steering vector activations. Our results reveal a clear power-law scaling: evaluation awareness increases predictably with model size. This scaling law enables forecasting deceptive behavior in future larger models and guides the design of scale-aware evaluation strategies for AI safety. A link to the implementation of this paper can be found at this https URL. Subjects: Artificial Intelligence (cs.AI) Cite as: arXiv:2509.13333 [cs.AI] &nbsp; (or arXiv:2509.13...


## connections
- processed from phone shortcut
