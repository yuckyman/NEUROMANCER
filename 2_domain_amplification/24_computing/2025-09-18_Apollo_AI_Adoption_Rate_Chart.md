---
type: note
category: 24-computing
created: 2025-09-18 12:11
modified: 2025-09-18 12:11
tags:
- AI adoption
- Apollo AI
- GPT-5
- Python
- Pyodide
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 20250918_114949_rss_Recreating_the_Apollo_AI_adoption_rate_chart_with_.txt
---


# Apollo AI Adoption Rate Chart

## summary
 recreating the Apollo AI adoption rate chart using GPT-5, Python and Pyodide

## content
RSS Feed: Simon Willison's Weblog
Source: https://simonwillison.net/atom/everything/
Link: https://simonwillison.net/2025/Sep/9/apollo-ai-adoption/#atom-everything

Recreating the Apollo AI adoption rate chart with GPT-5, Python and Pyodide

Apollo Global Management's "Chief Economist" Dr. Torsten Sløk released this interesting chart which appears to show a slowdown in AI adoption rates among large (&gt;250 employees) companies: Here's the full description that accompanied the chart: The US Census Bureau conducts a biweekly survey of 1.2 million firms, and one question is whether a business has used AI tools such as machine learning, natural language processing, virtual agents or voice recognition to help produce goods or services in the past two weeks. Recent data by firm size shows that AI adoption has been declining among companies with more than 250 employees, see chart below. (My first thought on seeing that chart is that I hope it represents the peak of inflated expectations leading into the trough of dissillusionment in the Gartner Hype Cycle (which Wikipedia calls "largely disputed, with studies pointing to it being inconsistently true at best"), since that means we might be reaching the end of the initial hype pha...

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


## Scraped from https://simonwillison.net/2025/Sep/9/apollo-ai-adoption/#atom-everything
Recreating the Apollo AI adoption rate chart with GPT-5, Python and Pyodide Simon Willison’s Weblog Subscribe Recreating the Apollo AI adoption rate chart with GPT-5, Python and Pyodide 9th September 2025 Apollo Global Management’s “Chief Economist” Dr. Torsten Sløk released this interesting chart which appears to show a slowdown in AI adoption rates among large (&gt;250 employees) companies: Here’s the full description that accompanied the chart: The US Census Bureau conducts a biweekly survey of 1.2 million firms, and one question is whether a business has used AI tools such as machine learning, natural language processing, virtual agents or voice recognition to help produce goods or services in the past two weeks. Recent data by firm size shows that AI adoption has been declining among companies with more than 250 employees, see chart below. (My first thought on seeing that chart is that I hope it represents the peak of inflated expectations leading into the trough of dissillusionment in the Gartner Hype Cycle (which Wikipedia calls “largely disputed, with studies pointing to it being inconsistently true at best”), since that means we might be reaching the end of the initial hype phase and heading towards the slope of enlightenment.) Finding the US Census data with GPT-5 search This is the first I’d heard of the US Census Bureau running a biweekly (that’s once every two weeks) survey about AI! I decided to track down the numbers and see if I could recreate the chart myself. And since GPT-5 is really good at search now I fed it the following prompt to see how well it could do: &gt; The US Census Bureau conducts a biweekly survey of 1.2 million firms, and one question is whether a business has used AI tools such as machine learning, natural language processing, virtual agents or voice recognition to help produce goods or services in the past two weeks. Recent data by firm size shows that AI adoption has been declining among companies with more than 250 employees, s...


## connections
- processed from phone shortcut
