---
type: note
category: ideas
created: 2025-09-18 12:10
modified: 2025-09-18 12:10
tags: ['icpc', 'openai', 'gemini']
status: draft
source: inbox_processing
original_file: 20250918_114949_rss_ICPC_medals_for_OpenAI_and_Gemini.txt
---

# Simone Willison's Weblog

## summary
The article provides details about the International Collegiate Programming Contest (ICPC) and its competitors, OpenAI and Gemini. It mentions that both teams achieved Gold medal performance in their respective competitions.

## content
RSS Feed: Simon Willison's Weblog
Source: https://simonwillison.net/atom/everything/
Link: https://simonwillison.net/2025/Sep/17/icpc/#atom-everything

ICPC medals for OpenAI and Gemini

In July it was the International Math Olympiad (OpenAI, Gemini), today it's the International Collegiate Programming Contest (ICPC). Once again, both OpenAI and Gemini competed with models that achieved Gold medal performance. OpenAI's Mostafa Rohaninejad: We received the problems in the exact same PDF form, and the reasoning system selected which answers to submit with no bespoke test-time harness whatsoever. For 11 of the 12 problems, the system’s first answer was correct. For the hardest problem, it succeeded on the 9th submission. Notably, the best human team achieved 11/12. We competed with an ensemble of general-purpose reasoning models; we did not train any model specifically for the ICPC. We had both GPT-5 and an experimental reasoning model generating solutions, and the experimental reasoning model selecting which solutions to submit. GPT-5 answered 11 correctly, and the last (and most difficult problem) was solved by the experimental reasoning model. And here's the blog post ...

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


## Scraped from https://simonwillison.net/2025/Sep/17/icpc/#atom-everything
ICPC medals for OpenAI and Gemini Simon Willison’s Weblog Subscribe In July it was the International Math Olympiad (OpenAI, Gemini), today it's the International Collegiate Programming Contest (ICPC). Once again, both OpenAI and Gemini competed with models that achieved Gold medal performance. OpenAI's Mostafa Rohaninejad: We received the problems in the exact same PDF form, and the reasoning system selected which answers to submit with no bespoke test-time harness whatsoever. For 11 of the 12 problems, the system’s first answer was correct. For the hardest problem, it succeeded on the 9th submission. Notably, the best human team achieved 11/12. We competed with an ensemble of general-purpose reasoning models; we did not train any model specifically for the ICPC. We had both GPT-5 and an experimental reasoning model generating solutions, and the experimental reasoning model selecting which solutions to submit. GPT-5 answered 11 correctly, and the last (and most difficult problem) was solved by the experimental reasoning model. And here's the blog post by Google DeepMind's Hanzhao (Maggie) Lin and Heng-Tze Cheng: An advanced version of Gemini 2.5 Deep Think competed live in a remote online environment following ICPC rules, under the guidance of the competition organizers. It started 10 minutes after the human contestants and correctly solved 10 out of 12 problems, achieving gold-medal level performance under the same five-hour time constraint. See our solutions here. I'm still trying to confirm if the models had access to tools in order to execute the code they were writing. The IMO results in July were both achieved without tools. Posted 17th September 2025 at 10:52 pm Recent articles My review of Claude&#x27;s new Code Interpreter, released under a very confusing name - 9th September 2025 Recreating the Apollo AI adoption rate chart with GPT-5, Python and Pyodide - 9th September 2025 GPT-5 Thinking in ChatGPT (aka Research Goblin) is shockingly good at search - 6th...


## connections
- processed from phone shortcut
