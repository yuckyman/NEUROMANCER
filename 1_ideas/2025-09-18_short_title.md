---
type: note
category: ideas
created: 2025-09-18 11:51
modified: 2025-09-18 11:51
tags: ['programming', 'Lexical structure', 'lexical keywords', 'cursed programming language', 'French slang']
status: draft
source: inbox_processing
original_file: 20250918_114949_rss_Geoffrey_Huntley_is_cursed.txt
---

# short title

## summary
Geoffrey Huntley is cursed: Claude's programming language, 'cursed', has a completely different syntax and lexical structures compared to its intended purposes.

## content
RSS Feed: Simon Willison's Weblog
Source: https://simonwillison.net/atom/everything/
Link: https://simonwillison.net/2025/Sep/9/cursed/#atom-everything

Geoffrey Huntley is cursed

I ran Claude in a loop for three months, and it created a genz programming language called cursed Geoffrey Huntley vibe-coded an entirely new programming language using Claude: The programming language is called "cursed". It's cursed in its lexical structure, it's cursed in how it was built, it's cursed that this is possible, it's cursed in how cheap this was, and it's cursed through how many times I've sworn at Claude. Geoffrey's initial prompt: Hey, can you make me a programming language like Golang but all the lexical keywords are swapped so they're Gen Z slang? Then he pushed it to keep on iterating over a three month period. Here's Hello World: vibe main yeet "vibez" slay main() { vibez.spill("Hello, World!") } And here's binary search, part of 17+ LeetCode problems that run as part of the test suite: slay binary_search(nums normie[], target normie) normie { sus left normie = 0 sus right normie = len(nums) - 1 bestie (left &lt;= right) { sus mid normie = left + (right - left) / 2 ...

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


## Scraped from https://simonwillison.net/2025/Sep/9/cursed/#atom-everything
Geoffrey Huntley is cursed Simon Willison’s Weblog Subscribe I ran Claude in a loop for three months, and it created a genz programming language called cursed (via) Geoffrey Huntley vibe-coded an entirely new programming language using Claude: The programming language is called "cursed". It's cursed in its lexical structure, it's cursed in how it was built, it's cursed that this is possible, it's cursed in how cheap this was, and it's cursed through how many times I've sworn at Claude. Geoffrey's initial prompt: Hey, can you make me a programming language like Golang but all the lexical keywords are swapped so they're Gen Z slang? Then he pushed it to keep on iterating over a three month period. Here's Hello World: vibe main yeet "vibez" slay main() { vibez.spill("Hello, World!") } And here's binary search, part of 17+ LeetCode problems that run as part of the test suite: slay binary_search(nums normie[], target normie) normie { sus left normie = 0 sus right normie = len(nums) - 1 bestie (left &lt;= right) { sus mid normie = left + (right - left) / 2 ready (nums[mid] == target) { damn mid } ready (nums[mid] &lt; target) { left = mid + 1 } otherwise { right = mid - 1 } } damn -1 } This is a substantial project. The repository currently has 1,198 commits. It has both an interpreter mode and a compiler mode, and can compile programs to native binaries (via LLVM) for macOS, Linux and Windows. It looks like it was mostly built using Claude running via Sourcegraph's Amp, which produces detailed commit messages. The commits include links to archived Amp sessions but sadly those don't appear to be publicly visible. The first version was written in C, then Geoffrey had Claude port it to Rust and then Zig. His cost estimate: Technically it costs about 5k usd to build your own compiler now because cursed was implemented first in c, then rust, now zig. So yeah, it’s not one compiler it’s three editions of it. For a total of $14k USD. Posted 9th September 2025 at 9:31 am Recent ...


## connections
- processed from phone shortcut
