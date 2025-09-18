---
type: note
category: 24-computing
created: 2025-09-18 11:54
modified: 2025-09-18 11:54
tags:
- python
- deep-copy
- shallow-copy
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 20250918_114949_rss_Deep_vs_Shallow_Copies_in_Python.txt
---


# Real Python – Understanding Deep vs Shallow Copies

## summary
In this blog post, we'll discuss the difference between shallow and deep copies in Python. We'll also learn how to safely duplicate objects using the copy module.

## content
RSS Feed: Real Python
Source: https://realpython.com/atom.xml
Link: https://realpython.com/courses/deep-vs-shallow-copies/

Deep vs Shallow Copies in Python

Understand the difference between shallow and deep copies in Python. Learn how to duplicate objects safely using the copy module and other techniques.

## Scraped from https://realpython.com/atom.xml
<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">

  <title>Real Python</title>
  <link href="https://realpython.com/atom.xml" rel="self"/>
  <link href="https://realpython.com/"/>
  <updated>2025-09-17T14:00:00+00:00</updated>
  <id>https://realpython.com/</id>
  <author>
    <name>Real Python</name>
  </author>

  
    <entry>
      <title>Python 3.14 Preview: REPL Autocompletion and Highlighting</title>
      <id>https://realpython.com/python-repl-autocompletion-highlighting/</id>
      <link href="https://realpython.com/python-repl-autocompletion-highlighting/"/>
      <updated>2025-09-17T14:00:00+00:00</updated>
      <summary>Explore Python 3.14 REPL updates: import autocompletion, syntax coloring, and theme customization to help you code faster and read with ease.</summary>
      <content type="html">
        &lt;div&gt;&lt;p&gt;Python 3.14 introduces improvements to its interactive shell (REPL), bringing a more modern, colorful, and user-friendly environment. The new features make the Python 3.14 REPL a powerful tool for experimentation. Whether you’re testing a quick idea, exploring a new library, or debugging a tricky snippet, the REPL gives you instant feedback—no files, no setup, just type and run.&lt;/p&gt;
&lt;p&gt;The default CPython REPL intentionally kept things minimal. It was fast, reliable, and available everywhere, but it lacked the richer, more ergonomic features found in tools like &lt;a href=&quot;https://realpython.com/ipython-interactive-python-shell/&quot;&gt;IPython&lt;/a&gt; or &lt;a href=&quot;https://realpython.com/ptpython-shell/&quot;&gt;ptpython&lt;/a&gt;. That began to change in &lt;strong&gt;Python 3.13&lt;/strong&gt;, when CPython adopted a modern PyREPL-based shell by default, adding multiline editing, better history navigation, and smarter &lt;span class=&quot;keys&quot;&gt;&lt;kbd class=&quot;key-tab&quot;&gt;Tab&lt;/kbd&gt;&lt;/span&gt; completion.&lt;/p&gt;
&lt;p&gt;&lt;strong&gt;By the end of...


## Scraped from https://realpython.com/courses/deep-vs-shallow-copies/
Deep vs Shallow Copies in Python – Real Python Start&nbsp;Here Learn Python Python Tutorials&nbsp;→In-depth articles and video courses Learning Paths&nbsp;→Guided study plans for accelerated learning Quizzes & Exercises&nbsp;→Check your learning progress Browse Topics&nbsp;→Focus on a specific area or skill level Community Chat&nbsp;→Learn with other Pythonistas Office Hours&nbsp;→Live Q&A calls with Python experts Podcast&nbsp;→Hear what’s new in the world of Python Books&nbsp;→Round out your knowledge and learn offline Reference&nbsp;→Concise definitions for common Python terms Code Mentor&nbsp;→BetaPersonalized code assistance &amp; learning tools Unlock All Content&nbsp;→ More Learner Stories Python Newsletter Python Job Board Meet the Team Become a Tutorial Writer Become a Video Instructor Search / Join Sign&#8209;In Deep vs Shallow Copies in Python Joseph Peart 9&nbsp;Lessons 40m advanced python Start Now Add Bookmark Rate and Review Share When working with Python objects, you&rsquo;ll often need to make copies rather than modify the originals. In this video course, you&rsquo;ll explore various ways to copy objects in Python, including using the built-in copy module. You&rsquo;ll also learn the key differences between shallow and deep copies, with practical examples so you can safely duplicate objects in your own code. By the end of this video course, you&rsquo;ll understand that: Shallow copying creates a new object but references the same nested objects, leading to shared changes. Deep copying recursively duplicates all objects, ensuring full independence from the original. Python&rsquo;s copy module provides the copy() function for shallow copies and deepcopy() for deep copies. Custom classes can implement .__copy__() and .__deepcopy__() for specific copying behavior. Assignment in Python binds variable names to objects without copying, unlike some lower-level languages. What’s Included: 9 Lessons Video Subtitles and Full Transcripts 2 Downloadable Resource...


## connections
- processed from phone shortcut
