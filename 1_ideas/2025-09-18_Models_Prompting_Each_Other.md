---
type: note
category: projects
created: 2025-09-18 12:04
modified: 2025-09-18 12:04
tags: ['RPG', 'simulation', 'AI']
status: draft
source: inbox_processing
original_file: 20250918_114949_rss_Models_can_prompt_now.txt
---

# Models Prompting Each Other

## summary
I am finding that today's leading models are incrementally improving over time. A year ago, I was skeptical of the pattern where models were used to help build prompts. The models have seen a decent volume of good prompting examples and have been deliberately trained for this.

## content
RSS Feed: Simon Willison's Weblog
Source: https://simonwillison.net/atom/everything/
Link: https://simonwillison.net/2025/Sep/14/models-can-prompt/#atom-everything

Models can prompt now

Here's an interesting example of models incrementally improving over time: I am finding that today's leading models are competent at writing prompts for themselves and each other. A year ago I was quite skeptical of the pattern where models are used to help build prompts. Prompt engineering was still a young enough discipline that I did not expect the models to have enough training data to be able to prompt themselves better than a moderately experienced human. The Claude 4 and GPT-5 families both have training cut-off dates within the past year - recent enough that they've seen a decent volume of good prompting examples. I expect they have also been deliberately trained for this. Anthropic make extensive use of sub-agent patterns in Claude Code, and published a fascinating article on that pattern (my notes on that). I don't have anything solid to back this up - it's more of a hunch based on anecdotal evidence where various of my requests for a model to write a prompt have returned use...

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


## Scraped from https://simonwillison.net/2025/Sep/14/models-can-prompt/#atom-everything
Models can prompt now Simon Willison’s Weblog Subscribe Here's an interesting example of models incrementally improving over time: I am finding that today's leading models are competent at writing prompts for themselves and each other. A year ago I was quite skeptical of the pattern where models are used to help build prompts. Prompt engineering was still a young enough discipline that I did not expect the models to have enough training data to be able to prompt themselves better than a moderately experienced human. The Claude 4 and GPT-5 families both have training cut-off dates within the past year - recent enough that they've seen a decent volume of good prompting examples. I expect they have also been deliberately trained for this. Anthropic make extensive use of sub-agent patterns in Claude Code, and published a fascinating article on that pattern (my notes on that). I don't have anything solid to back this up - it's more of a hunch based on anecdotal evidence where various of my requests for a model to write a prompt have returned useful results over the last few months. Posted 14th September 2025 at 8:25 pm Recent articles My review of Claude&#x27;s new Code Interpreter, released under a very confusing name - 9th September 2025 Recreating the Apollo AI adoption rate chart with GPT-5, Python and Pyodide - 9th September 2025 GPT-5 Thinking in ChatGPT (aka Research Goblin) is shockingly good at search - 6th September 2025 prompt-engineering 160 llms 1346 ai 1566 generative-ai 1375 gpt-5 18 anthropic 184 claude 195 claude-code 26 claude-4 13 Monthly briefing Sponsor me for $10/month and get a curated email digest of the month's most important LLM developments. Pay me to send you less! Sponsor &amp; subscribe Colophon &copy; 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025


## connections
- processed from phone shortcut
