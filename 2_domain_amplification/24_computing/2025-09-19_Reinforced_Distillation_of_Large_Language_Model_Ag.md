---
type: note
category: 24-computing
created: 2025-09-19 17:55
modified: 2025-09-19 17:55
tags:
- large language models
- distillation
- student-centered
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 20250919_175447_rss_From_Correction_to_Mastery__Reinforced_Distillatio.txt
content_hash: d15743c454852d788aa0b9a68307708281954dee30692055a9b154d0b09676c1
---


# Reinforced Distillation of Large Language Model Agents

## summary
SCoRe: A student-centered framework for fine-tuning large language model agents by training trajectories and intervening only at critical errors.

## content
RSS Feed: cs.AI updates on arXiv.org
Source: https://arxiv.org/rss/cs.AI
Link: https://arxiv.org/abs/2509.14257

From Correction to Mastery: Reinforced Distillation of Large Language Model Agents

arXiv:2509.14257v1 Announce Type: cross Abstract: Large Language Model agents excel at solving complex tasks through iterative reasoning and tool use, but typically depend on ultra-large, costly backbones. Existing distillation approaches train smaller students to imitate full teacher trajectories, yet reasoning and knowledge gaps between the teacher and student often lead to compounding errors. We propose SCoRe, a student-centered framework in which the student generates trajectories and the teacher intervenes only at the first critical error, producing training data matched to the student's ability and exposing specific weaknesses. The student is first fine-tuned on corrected trajectories. Subsequently, short-horizon reinforcement learning starts from the verified prefix before the first critical error, with target rewards assigned at that step. This design encourages autonomous problem-solving beyond imitation and improves training stability. Particularly, on 12 challenging benchmar...

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


## Scraped from https://arxiv.org/abs/2509.14257
[2509.14257] From Correction to Mastery: Reinforced Distillation of Large Language Model Agents Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2509.14257 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Computation and Language arXiv:2509.14257 (cs) [Submitted on 12 Sep 2025] Title:From Correction to Mastery: Reinforced Distillation of Large Language Model Agents Authors:Yuanjie Lyu, Chengyu Wang, Jun Huang, Tong Xu View a PDF of the paper titled From Correction to Mastery: Reinforced Distillation of Large Language Model Agents, by Yuanjie Lyu and 3 other authors View PDF HTML (experimental) Abstract:Large Language Model agents excel at solving complex tasks through iterative reasoning and tool use, but typically depend on ultra-large, costly backbones. Existing distillation approaches train smaller students to imitate full teacher trajectories, yet reasoning and knowledge gaps between the teacher and student often lead to compounding errors. We propose SCoRe, a student-centered framework in which the student generates trajectories and the teacher intervenes only at the first critical error, producing training data matched to the student&#39;s ability and exposing specific weaknesses. The student is first fine-tuned on corrected trajectories. Subsequently, short-horizon reinforcement learning starts from the verified prefix before the first critical error, with target rewards assigned at that step. This design encourages autonomous problem-solving beyond imitation and improves training stability. Particularly, on 12 challenging benchmarks, a 7B-parameter student distilled with SCoRe matches the agentic performance of...


## connections
- processed from phone shortcut
