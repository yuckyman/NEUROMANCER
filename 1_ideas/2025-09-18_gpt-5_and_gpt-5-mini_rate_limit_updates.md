---
type: note
category: development
created: 2025-09-18 11:53
modified: 2025-09-18 11:53
tags: ['dev-log', 'project', 'research', 'idea']
status: draft
source: inbox_processing
original_file: 20250918_114949_rss_gpt-5_and_gpt-5-mini_rate_limit_updates.txt
---

# gpt-5 and gpt-5-mini rate limit updates

## summary
OpenAI increased the rate limits for their two main GPT-5 models, showing that those tiers are based on how much money you have spent on the OpenAI API. The gpt-5 and gpt-5-mini rates here show tier 5 stays at 40M tokens per minute.

## content
RSS Feed: Simon Willison's Weblog
Source: https://simonwillison.net/atom/everything/
Link: https://simonwillison.net/2025/Sep/12/gpt-5-rate-limits/#atom-everything

gpt-5 and gpt-5-mini rate limit updates

gpt-5 and gpt-5-mini rate limit updates OpenAI have increased the rate limits for their two main GPT-5 models. These look significant: gpt-5 Tier 1: 30K → 500K TPM (1.5M batch) Tier 2: 450K → 1M (3M batch) Tier 3: 800K → 2M Tier 4: 2M → 4M gpt-5-mini Tier 1: 200K → 500K (5M batch) GPT-5 rate limits here show tier 5 stays at 40M tokens per minute. The GPT-5 mini rate limits for tiers 2 through 5 are 2M, 4M, 10M and 180M TPM respectively. As a reminder, those tiers are assigned based on how much money you have spent on the OpenAI API - from $5 for tier 1 up through $50, $100, $250 and then $1,000 for tier For comparison, Anthropic's current top tier is Tier 4 ($400 spent) which provides 2M maximum input tokens per minute and 400,000 maximum output tokens, though you can contact their sales team for higher limits than that. Gemini's top tier is Tier 3 for $1,000 spent and currently gives you 8M TPM for Gemini 2.5 Pro and Flash and 30M TPM for the Flash-Lite and 2.0 Flash models. So OpenAI...

## Scraped from https://simonwillison.net/atom/everything/
<?xml version="1.0" encoding="utf-8"?>
<feed xml:lang="en-us" xmlns="http://www.w3.org/2005/Atom"><title>Simon Willison's Weblog</title><link href="http://simonwillison.net/" rel="alternate"/><link href="http://simonwillison.net/atom/everything/" rel="self"/><id>http://simonwillison.net/</id><updated>2025-09-17T23:53:38+00:00</updated><author><name>Simon Willison</name></author><entry><title>Anthropic: A postmortem of three recent issues</title><link href="https://simonwillison.net/2025/Sep/17/anthropic-postmortem/#atom-everything" rel="alternate"/><published>2025-09-17T23:53:38+00:00</published><updated>2025-09-17T23:53:38+00:00</updated><id>https://simonwillison.net/2025/Sep/17/anthropic-postmortem/#atom-everything</id><summary type="html">
    
&lt;p&gt;&lt;strong&gt;&lt;a href="https://www.anthropic.com/engineering/a-postmortem-of-three-recent-issues"&gt;Anthropic: A postmortem of three recent issues&lt;/a&gt;&lt;/strong&gt;&lt;/p&gt;
Anthropic had a very bad month in terms of model reliability:&lt;/p&gt;
&lt;blockquote&gt;
&lt;p&gt;Between August and early September, three infrastructure bugs intermittently degraded Claude's response quality. We've now resolved these issues and want to explain what happened. [...]&lt;/p&gt;
&lt;p&gt;To state it plainly: We never reduce model quality due to demand, time of day, or server load. The problems our users reported were due to infrastructure bugs alone. [...]&lt;/p&gt;
&lt;p&gt;We don't typically share this level of technical detail about our infrastructure, but the scope and complexity of these issues justified a more comprehensive explanation.&lt;/p&gt;
&lt;/blockquote&gt;
&lt;p&gt;I'm really glad Anthropic are publishing this in so much detail. Their reputation for serving their models reliably has taken a notable hit.&lt;/p&gt;
&lt;p&gt;I hadn't appreciated the additional complexity caused by their mixture of different serving platforms:&lt;/p&gt;
&lt;blockquote&gt;
&lt;p&gt;We deploy Claude across multiple hardwar...


## Scraped from https://simonwillison.net/2025/Sep/12/gpt-5-rate-limits/#atom-everything
gpt-5 and gpt-5-mini rate limit updates Simon Willison’s Weblog Subscribe gpt-5 and gpt-5-mini rate limit updates. OpenAI have increased the rate limits for their two main GPT-5 models. These look significant: gpt-5 Tier 1: 30K → 500K TPM (1.5M batch) Tier 2: 450K → 1M (3M batch) Tier 3: 800K → 2M Tier 4: 2M → 4M gpt-5-mini Tier 1: 200K → 500K (5M batch) GPT-5 rate limits here show tier 5 stays at 40M tokens per minute. The GPT-5 mini rate limits for tiers 2 through 5 are 2M, 4M, 10M and 180M TPM respectively. As a reminder, those tiers are assigned based on how much money you have spent on the OpenAI API - from $5 for tier 1 up through $50, $100, $250 and then $1,000 for tier For comparison, Anthropic's current top tier is Tier 4 ($400 spent) which provides 2M maximum input tokens per minute and 400,000 maximum output tokens, though you can contact their sales team for higher limits than that. Gemini's top tier is Tier 3 for $1,000 spent and currently gives you 8M TPM for Gemini 2.5 Pro and Flash and 30M TPM for the Flash-Lite and 2.0 Flash models. So OpenAI's new rate limit increases for their top performing model pulls them ahead of Anthropic but still leaves them significantly behind Gemini. GPT-5 mini remains the champion for smaller models with that enormous 180M TPS limit for its top tier. Posted 12th September 2025 at 11:14 pm Recent articles My review of Claude&#x27;s new Code Interpreter, released under a very confusing name - 9th September 2025 Recreating the Apollo AI adoption rate chart with GPT-5, Python and Pyodide - 9th September 2025 GPT-5 Thinking in ChatGPT (aka Research Goblin) is shockingly good at search - 6th September 2025 ai 1566 openai 348 generative-ai 1375 llms 1346 anthropic 184 gemini 111 llm-pricing 54 gpt-5 18 Monthly briefing Sponsor me for $10/month and get a curated email digest of the month's most important LLM developments. Pay me to send you less! Sponsor &amp; subscribe Colophon &copy; 2002 2003 2004 2005 2006 2007 2008 2009 20...


## connections
- processed from phone shortcut
