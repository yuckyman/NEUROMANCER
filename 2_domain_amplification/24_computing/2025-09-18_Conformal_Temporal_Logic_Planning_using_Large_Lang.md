---
type: note
category: 24-computing
created: 2025-09-18 11:56
modified: 2025-09-18 11:56
tags:
- big-data
- AI
- RL
- Planning
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_Conformal_Temporal_Logic_Planning_using_Large_Lang.txt
---


# Conformal Temporal Logic Planning using Large Language Models

## summary
This paper addresses mobile robot mission planning problems in a formal language such as Conformal Temporal Logic (CTL) and Large Language Models. It proposes HERACLEs, a hierarchical neuro-symbolic planner that integrates existing symbolic planners.

## content
RSS Feed: cs.AI updates on arXiv.org
Source: https://arxiv.org/rss/cs.AI
Link: https://arxiv.org/abs/2309.10092

Conformal Temporal Logic Planning using Large Language Models

arXiv:2309.10092v5 Announce Type: replace-cross Abstract: This paper addresses planning problems for mobile robots. We consider missions that require accomplishing multiple high-level sub-tasks, expressed in natural language (NL), in a temporal and logical order. To formally define the mission, we treat these sub-tasks as atomic predicates in a Linear Temporal Logic (LTL) formula. We refer to this task specification framework as LTL-NL. Our goal is to design plans, defined as sequences of robot actions, accomplishing LTL-NL tasks. This action planning problem cannot be solved directly by existing LTL planners because of the NL nature of atomic predicates. To address it, we propose HERACLEs, a hierarchical neuro-symbolic planner that relies on a novel integration of (i) existing symbolic planners generating high-level task plans determining the order at which the NL sub-tasks should be accomplished; (ii) pre-trained Large Language Models (LLMs) to design sequences of robot actions based...

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


## Scraped from https://arxiv.org/abs/2309.10092
[2309.10092] Conformal Temporal Logic Planning using Large Language Models Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2309.10092 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Robotics arXiv:2309.10092 (cs) [Submitted on 18 Sep 2023 (v1), last revised 17 Sep 2025 (this version, v5)] Title:Conformal Temporal Logic Planning using Large Language Models Authors:Jun Wang, Jiaming Tong, Kaiyuan Tan, Yevgeniy Vorobeychik, Yiannis Kantaros View a PDF of the paper titled Conformal Temporal Logic Planning using Large Language Models, by Jun Wang and 4 other authors View PDF HTML (experimental) Abstract:This paper addresses planning problems for mobile robots. We consider missions that require accomplishing multiple high-level sub-tasks, expressed in natural language (NL), in a temporal and logical order. To formally define the mission, we treat these sub-tasks as atomic predicates in a Linear Temporal Logic (LTL) formula. We refer to this task specification framework as LTL-NL. Our goal is to design plans, defined as sequences of robot actions, accomplishing LTL-NL tasks. This action planning problem cannot be solved directly by existing LTL planners because of the NL nature of atomic predicates. To address it, we propose HERACLEs, a hierarchical neuro-symbolic planner that relies on a novel integration of (i) existing symbolic planners generating high-level task plans determining the order at which the NL sub-tasks should be accomplished; (ii) pre-trained Large Language Models (LLMs) to design sequences of robot actions based on these task plans; and (iii) conformal prediction acting as a formal interface between (i) an...


## connections
- processed from phone shortcut
