---
type: note
category: development and techniques
created: 2025-09-18 12:08
modified: 2025-09-18 12:08
tags: ['faithful reasoning', 'machine learning', 'large language models', 'causal inference']
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_FRIT__Using_Causal_Importance_to_Improve_Chain-of-.txt
---

# Improving Large Language Model Performance through Chain-of-Thought Reasoning

## summary
We introduce a scalable alignment method called Faithful Reasoning via Intervention Training (FRIT) for improving the Chain-of-Thought (CoT) reasoning in large language model performance. FRIT generates synthetic training data by intervening on individual CoTs to produce faithful/unfaithful pairs that help identify when reasonin steps cause or do not affect the final answer.

## content
RSS Feed: cs.AI updates on arXiv.org
Source: https://arxiv.org/rss/cs.AI
Link: https://arxiv.org/abs/2509.13334

FRIT: Using Causal Importance to Improve Chain-of-Thought Faithfulness

arXiv:2509.13334v1 Announce Type: new Abstract: Chain-of-thought (CoT) reasoning has emerged as a powerful tool for improving large language model performance on complex tasks, but recent work shows that reasoning steps often fail to causally influence the final answer, creating brittle and untrustworthy outputs. Prior approaches focus primarily on measuring faithfulness, while methods for systematically improving it remain limited. We introduce Faithful Reasoning via Intervention Training (FRIT), a scalable alignment method that trains models to produce causally consistent reasoning by learning from systematically corrupted examples. FRIT generates synthetic training data by intervening on individual reasoning steps in model-generated CoTs, creating faithful/unfaithful pairs that highlight when reasoning breaks down. We then apply Direct Preference Optimization to teach models to prefer causally consistent reasoning paths. Evaluating on Qwen3-8B and Mistral-7B-v0.1 across factual and ...

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


## Scraped from https://arxiv.org/abs/2509.13334
[2509.13334] FRIT: Using Causal Importance to Improve Chain-of-Thought Faithfulness Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2509.13334 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Artificial Intelligence arXiv:2509.13334 (cs) [Submitted on 10 Sep 2025] Title:FRIT: Using Causal Importance to Improve Chain-of-Thought Faithfulness Authors:Anand Swaroop, Akshat Nallani, Saksham Uboweja, Adiliia Uzdenova, Michael Nguyen, Kevin Zhu, Sunishchal Dev, Ashwinee Panda, Vasu Sharma, Maheep Chaudhary View a PDF of the paper titled FRIT: Using Causal Importance to Improve Chain-of-Thought Faithfulness, by Anand Swaroop and 9 other authors View PDF HTML (experimental) Abstract:Chain-of-thought (CoT) reasoning has emerged as a powerful tool for improving large language model performance on complex tasks, but recent work shows that reasoning steps often fail to causally influence the final answer, creating brittle and untrustworthy outputs. Prior approaches focus primarily on measuring faithfulness, while methods for systematically improving it remain limited. We introduce Faithful Reasoning via Intervention Training (FRIT), a scalable alignment method that trains models to produce causally consistent reasoning by learning from systematically corrupted examples. FRIT generates synthetic training data by intervening on individual reasoning steps in model-generated CoTs, creating faithful/unfaithful pairs that highlight when reasoning breaks down. We then apply Direct Preference Optimization to teach models to prefer causally consistent reasoning paths. Evaluating on Qwen3-8B and Mistral-7B-v0.1 across factual and symbolic r...


## connections
- processed from phone shortcut
