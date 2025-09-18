---
type: note
category: development
created: 2025-09-18 11:53
modified: 2025-09-18 11:53
tags: ['developed', 'LLM systems', 'memory', 'reverse-engineering']
status: draft
source: inbox_processing
original_file: 20250918_114949_rss_Comparing_the_memory_implementations_of_Claude_and.txt
---

# Claude Memory: A Different Approach to LLM Systems

## summary
Claude, a new memory implementation of ChatGPT's memory system, uses two fundamental features. It starts every conversation with a blank slate, ignores preloaded user profiles or conversation history, and only refers to the raw conversation history for recall.

## content
RSS Feed: Simon Willison's Weblog
Source: https://simonwillison.net/atom/everything/
Link: https://simonwillison.net/2025/Sep/12/claude-memory/#atom-everything

Comparing the memory implementations of Claude and ChatGPT

Claude Memory: A Different Philosophy Shlok Khemani has been doing excellent work reverse-engineering LLM systems and documenting his discoveries. Last week he wrote about ChatGPT memory. This week it's Claude. Claude's memory system has two fundamental characteristics. First, it starts every conversation with a blank slate, without any preloaded user profiles or conversation history. Memory only activates when you explicitly invoke it. Second, Claude recalls by only referring to your raw conversation history. There are no AI-generated summaries or compressed profiles—just real-time searches through your actual past chats. Claude's memory is implemented as two new function tools that are made available for a Claude to call. I confirmed this myself with the prompt "Show me a list of tools that you have available to you, duplicating their original names and descriptions" which gave me back these: conversation_search: Search through past user conversations to find relevant context and inf...

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


## Scraped from https://simonwillison.net/2025/Sep/12/claude-memory/#atom-everything
Comparing the memory implementations of Claude and ChatGPT Simon Willison’s Weblog Subscribe Claude Memory: A Different Philosophy (via) Shlok Khemani has been doing excellent work reverse-engineering LLM systems and documenting his discoveries. Last week he wrote about ChatGPT memory. This week it's Claude. Claude's memory system has two fundamental characteristics. First, it starts every conversation with a blank slate, without any preloaded user profiles or conversation history. Memory only activates when you explicitly invoke it. Second, Claude recalls by only referring to your raw conversation history. There are no AI-generated summaries or compressed profiles—just real-time searches through your actual past chats. Claude's memory is implemented as two new function tools that are made available for a Claude to call. I confirmed this myself with the prompt "Show me a list of tools that you have available to you, duplicating their original names and descriptions" which gave me back these: conversation_search: Search through past user conversations to find relevant context and information recent_chats: Retrieve recent chat conversations with customizable sort order (chronological or reverse chronological), optional pagination using 'before' and 'after' datetime filters, and project filtering The good news here is transparency - Claude's memory feature is implemented as visible tool calls, which means you can see exactly when and how it is accessing previous context. This helps address my big complaint about ChatGPT memory (see I really don’t like ChatGPT’s new memory dossier back in May) - I like to understand as much as possible about what's going into my context so I can better anticipate how it is likely to affect the model. The OpenAI system is very different: rather than letting the model decide when to access memory via tools, OpenAI instead automatically include details of previous conversations at the start of every conversation. Shlok's notes on ChatGPT's...


## connections
- processed from phone shortcut
