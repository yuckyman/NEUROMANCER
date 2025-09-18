---
type: note
category: 24-computing
created: 2025-09-18 11:57
modified: 2025-09-18 11:57
tags:
- agentic
- jwt
- autonomous agents
- permission management
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_Agentic_JWT__A_Secure_Delegation_Protocol_for_Auto.txt
---


# A-JWT: A Secure Delegation Protocol for Autonomous AI Agents

## summary
A new authorization mechanism for autonomous artificial intelligence agents, integrating user intent checks and workflow assertions.

## content
RSS Feed: cs.AI updates on arXiv.org
Source: https://arxiv.org/rss/cs.AI
Link: https://arxiv.org/abs/2509.13597

Agentic JWT: A Secure Delegation Protocol for Autonomous AI Agents

arXiv:2509.13597v1 Announce Type: cross Abstract: Autonomous LLM agents can issue thousands of API calls per hour without human oversight. OAuth 2.0 assumes deterministic clients, but in agentic settings stochastic reasoning, prompt injection, or multi-agent orchestration can silently expand privileges. We introduce Agentic JWT (A-JWT), a dual-faceted intent token that binds each agent's action to verifiable user intent and, optionally, to a specific workflow step. A-JWT carries an agent's identity as a one-way checksum hash derived from its prompt, tools and configuration, and a chained delegation assertion to prove which downstream agent may execute a given task, and per-agent proof-of-possession keys to prevent replay and in-process impersonation. We define a new authorization mechanism and add a lightweight client shim library that self-verifies code at run time, mints intent tokens, tracks workflow steps and derives keys, thus enabling secure agent identity and separation even wit...

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


## Scraped from https://arxiv.org/abs/2509.13597
[2509.13597] Agentic JWT: A Secure Delegation Protocol for Autonomous AI Agents Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2509.13597 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Cryptography and Security arXiv:2509.13597 (cs) [Submitted on 16 Sep 2025] Title:Agentic JWT: A Secure Delegation Protocol for Autonomous AI Agents Authors:Abhishek Goswami View a PDF of the paper titled Agentic JWT: A Secure Delegation Protocol for Autonomous AI Agents, by Abhishek Goswami View PDF HTML (experimental) Abstract:Autonomous LLM agents can issue thousands of API calls per hour without human oversight. OAuth 2.0 assumes deterministic clients, but in agentic settings stochastic reasoning, prompt injection, or multi-agent orchestration can silently expand privileges. We introduce Agentic JWT (A-JWT), a dual-faceted intent token that binds each agent&#39;s action to verifiable user intent and, optionally, to a specific workflow step. A-JWT carries an agent&#39;s identity as a one-way checksum hash derived from its prompt, tools and configuration, and a chained delegation assertion to prove which downstream agent may execute a given task, and per-agent proof-of-possession keys to prevent replay and in-process impersonation. We define a new authorization mechanism and add a lightweight client shim library that self-verifies code at run time, mints intent tokens, tracks workflow steps and derives keys, thus enabling secure agent identity and separation even within a single process. We illustrate a comprehensive threat model for agentic applications, implement a Python proof-of-concept and show functional blocking of scope-viol...


## connections
- processed from phone shortcut
