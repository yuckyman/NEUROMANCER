---
type: note
category: 24-computing
created: 2025-09-19 17:59
modified: 2025-09-19 17:59
tags:
- tag1
- tag2
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 20250918_114949_rss_Anthropic_status__Model_output_quality.txt
content_hash: 695708512443a230274475a8baa8d5cc9c445d22339355a7fd487dad4421a85c
---


# Update on Anthropic's Model Output Quality

## summary
Anthropic reported a model output quality bug affecting a small percentage of Sonnet 4 requests for almost a month, along with a Haiku issue. They've fixed the bugs and resolved some incidents.

## content
RSS Feed: Simon Willison's Weblog
Source: https://simonwillison.net/atom/everything/
Link: https://simonwillison.net/2025/Sep/9/anthropic-model-output-quality/#atom-everything

Anthropic status: Model output quality

Anthropic status: Model output quality Anthropic previously reported model serving bugs that affected Claude Opus 4 and 4.1 for 56.5 hours. They've now fixed additional bugs affecting "a small percentage" of Sonnet 4 requests for almost a month, plus a less long-lived Haiku 3.5 issue: Resolved issue 1 - A small percentage of Claude Sonnet 4 requests experienced degraded output quality due to a bug from Aug 5-Sep 4, with the impact increasing from Aug 29-Sep 4. A fix has been rolled out and this incident has been resolved. Resolved issue 2 - A separate bug affected output quality for some Claude Haiku 3.5 and Claude Sonnet 4 requests from Aug 26-Sep 5. A fix has been rolled out and this incident has been resolved. They directly address accusations that these stem from deliberate attempts to save money on serving models: Importantly, we never intentionally degrade model quality as a result of demand or other factors, and the issues mentioned above stem from unrelated bugs. The timing of ...

## Scraped from https://simonwillison.net/atom/everything/
<?xml version="1.0" encoding="utf-8"?>
<feed xml:lang="en-us" xmlns="http://www.w3.org/2005/Atom"><title>Simon Willison's Weblog</title><link href="http://simonwillison.net/" rel="alternate"/><link href="http://simonwillison.net/atom/everything/" rel="self"/><id>http://simonwillison.net/</id><updated>2025-09-19T19:13:45+00:00</updated><author><name>Simon Willison</name></author><entry><title>Magistral 1.2</title><link href="https://simonwillison.net/2025/Sep/19/magistral/#atom-everything" rel="alternate"/><published>2025-09-19T19:13:45+00:00</published><updated>2025-09-19T19:13:45+00:00</updated><id>https://simonwillison.net/2025/Sep/19/magistral/#atom-everything</id><summary type="html">
    &lt;p&gt;Mistral &lt;a href="https://twitter.com/MistralAI/status/1968670593412190381"&gt;quietly released&lt;/a&gt; two new models yesterday: &lt;a href="https://huggingface.co/mistralai/Magistral-Small-2509"&gt;Magistral Small 1.2&lt;/a&gt; (Apache 2.0, 
96.1 GB on Hugging Face) and Magistral Medium 1.2 (not open weights same as Mistral's other "medium" models.)&lt;/p&gt;
&lt;p&gt;Despite being described as "minor updates" to the Magistral 1.1 models these have one very notable improvement:&lt;/p&gt;
&lt;blockquote&gt;
&lt;ul&gt;
&lt;li&gt;Multimodality: Now equipped with a vision encoder, these models handle both text and images seamlessly.&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;p&gt;Magistral is Mistral's reasoning model, so we now have a new reasoning vision LLM.&lt;/p&gt;
&lt;p&gt;The other features from the tiny announcement on Twitter:&lt;/p&gt;
&lt;blockquote&gt;
&lt;ul&gt;
&lt;li&gt;Performance Boost: 15% improvements on math and coding benchmarks such as AIME 24/25 and LiveCodeBench v5/v6.&lt;/li&gt;
&lt;li&gt;Smarter Tool Use: Better tool usage with web search, code interpreter, and image generation.&lt;/li&gt;
&lt;li&gt;Better Tone &amp;amp; Persona: Responses are clearer, more natural, and better formatted for you.&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt...


## Scraped from https://simonwillison.net/2025/Sep/9/anthropic-model-output-quality/#atom-everything
Anthropic status: Model output quality Simon Willison’s Weblog Subscribe Anthropic status: Model output quality (via) Anthropic previously reported model serving bugs that affected Claude Opus 4 and 4.1 for 56.5 hours. They've now fixed additional bugs affecting "a small percentage" of Sonnet 4 requests for almost a month, plus a less long-lived Haiku 3.5 issue: Resolved issue 1 - A small percentage of Claude Sonnet 4 requests experienced degraded output quality due to a bug from Aug 5-Sep 4, with the impact increasing from Aug 29-Sep 4. A fix has been rolled out and this incident has been resolved. Resolved issue 2 - A separate bug affected output quality for some Claude Haiku 3.5 and Claude Sonnet 4 requests from Aug 26-Sep 5. A fix has been rolled out and this incident has been resolved. They directly address accusations that these stem from deliberate attempts to save money on serving models: Importantly, we never intentionally degrade model quality as a result of demand or other factors, and the issues mentioned above stem from unrelated bugs. The timing of these issues is really unfortunate, corresponding with the rollout of GPT-5 which I see as the non-Anthropic model to feel truly competitive with Claude for writing code since their release of Claude 3.5 back in June last year. Posted 9th September 2025 at 6:28 am Recent articles I think &quot;agent&quot; may finally have a widely enough agreed upon definition to be useful jargon now - 18th September 2025 My review of Claude&#x27;s new Code Interpreter, released under a very confusing name - 9th September 2025 Recreating the Apollo AI adoption rate chart with GPT-5, Python and Pyodide - 9th September 2025 ai 1569 generative-ai 1378 llms 1349 anthropic 184 claude 195 claude-4 13 gpt-5 18 Monthly briefing Sponsor me for $10/month and get a curated email digest of the month's most important LLM developments. Pay me to send you less! Sponsor &amp; subscribe Colophon &copy; 2002 2003 2004 2005 2006 2007 2008 2009...


## connections
- processed from phone shortcut
