---
type: rss
category: 24-computing
created: 2025-09-19 17:55
modified: 2025-09-19 17:55
tags:
- news
- RSS
- feeds
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 1758227090.txt
content_hash: 927b282781b3f6d4ecd746009301cf6018a1006ca59b84e97ac1945dc1910e8f
---


# Hacker News RSS Feeds

## summary
Provide custom, realtime RSS feeds for Hacker News.

## content
<!doctype html>

<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes" />
<title>Hacker News RSS</title>
<link rel="stylesheet" type="text/css" href="style.css?ver=2020.11.14-02">
<link rel="alternate" type="application/rss+xml" title="hnrss.org updates" href="https://hnrss.github.io/updates.xml">

<header>
<h1 class="title">Hacker News RSS</h1>
</header>

<h2 id="overview">Overview</h2>
<p>hnrss.org provides custom, realtime RSS feeds for <a href="https://news.ycombinator.com/">Hacker News</a>.</p>
<p>The following feed types are available:</p>

<table>
<tbody>
<tr >
<td ><a href="#firehose-feeds"><strong>Firehose</strong></a></td>
<td>New <a href="https://hnrss.org/newest">posts</a> and <a href="https://hnrss.org/newcomments">comments</a> as they arrive.</td>
</tr>

<tr >
<td ><a href="#search-feeds"><strong>Searches</strong></a></td>
<td>New <a href="https://hnrss.org/newest?q=redis">posts</a> and <a href="https://hnrss.org/newcomments?q=linux">comments</a> matching a given search term.</td>
</tr>
<tr >
<td ><a href="#reply-feeds"><strong>Replies</strong></a></td>
<td>New comments in reply to a particular <a href="https://hnrss.org/replies?id=jerf">user</a> or <a href="https://hnrss.org/replies?id=17752464">comment</a>.</td>
</tr>

<tr>
<td><a href="#bestcomments"><strong>Best Comments</strong></a></td>
<td>The <a href="https://hnrss.org/bestcomments">best comments</a> from across Hacker News.</td>
</tr>

<tr >
<td ><a href="#activity-parameters"><strong>Points</strong></a></td>
<td>New <a href="https://hnrss.org/newest?points=300">posts</a> with more than N points.</td>
</tr>
<tr >
<td ><a href="#activity-parameters"><strong>Activity</strong></a></td>
<td>New <a href="https://hnrss.org/newest?comments=250">posts</a> with more than N comments.</td>
</tr>

<tr >
<td ><a href="#firehose-feeds"><strong>Front Page</strong></a></td>
<td>New <a href="https://hnrss.org/frontpage">posts</a> as they appear on the front page.</td>
</tr>

<tr >
<td ><a href="#self-post-feeds"><strong>Self-posts</strong></a></td>
<td>New “<a href="https://hnrss.org/ask">Ask HN</a>” and “<a href="https://hnrss.org/show">Show HN</a>” posts, along with <a href="https://hnrss.org/polls">polls</a>.</td>
</tr>

<tr>
<td><a href="#alternative-feeds"><strong>Alternative</strong></a></td>
<td>Follow Hacker News through some alternative homepages.</td>
</tr>

<tr >
<td ><a href="#job-feeds"><strong>Jobs</strong></a></td>
<td>New <a href="https://hnrss.org/jobs">hiring posts</a> made by YC startups along with comments from the monthly <a href="https://hnrss.org/whoishiring/jobs">“Who is hiring?”</a> threads.</td>
</tr>
<tr >
<td ><a href="#user-feeds"><strong>Users</strong></a></td>
<td>New <a href="https://hnrss.org/submitted?id=jacquesm">posts</a> and <a href="https://hnrss.org/threads?id=tptacek">comments</a> made by a given user.</td>
</tr>

<tr >
<td ><a href="#favorite-feeds"><strong>Favorites</strong></a></td>
<td>New posts that have been <a href="https://hnrss.org/favorites?id=edavis">favorited</a> by a particular user</td>
</tr>

<tr >
<td ><a href="#thread-feeds"><strong>Threads</strong></a></td>
<td>New comments made <a href="https://hnrss.org/item?id=23778510">in a given thread</a>, optionally <a href="https://hnrss.org/item?id=23778510&author=edavis">filtered by username</a>.</td>
</tr>
<tr >
<td ><a href="#feed-formats"><strong>Formats</strong></a></td>
<td>In addition to RSS, all of the above are also available in <a href="https://hnrss.org/newest.atom">Atom</a> and <a href="https://hnrss.org/newest.jsonfeed">JSON Feed</a> formats.</td>
</tr>
</tbody>
</table>

<h2 id="details">Feeds</h2>
<p>Each feed is <a href="https://validator.w3.org/feed/check.cgi?url=https%3A%2F%2Fhnrss.org%2Fnewest">valid RSS</a> served over <a href="https://www.ssllabs.com/ssltest/analyze.html?d=hnrss.org">HTTPS</a>.</p>

<h3 id="firehose-feeds">Firehose Feeds</h3>
<p>The “firehose” feeds contain all new posts and comments as they appear on Hacker News:</p>
<pre>
https://hnrss.org/newest
https://hnrss.org/newcomments
</pre>
<p>For just the posts that have appeared on the front page:</p>
<pre>
https://hnrss.org/frontpage
</pre>
<p>If the firehose feeds are a bit too noisy for you, <a href="#activity-parameters">read below</a> on filtering them with the <code>points</code> and/or <code>comments</code> parameters.</p>

<h3 id="search-feeds">Search Feeds</h3>
<p>You can get a feed of new posts and/or comments containing keywords by using the <code>q=KEYWORD</code> parameter. For example:</p>
<pre>
https://hnrss.org/newest?q=Django
https://hnrss.org/newcomments?q=WordPress
</pre>
<p>If you want a single search feed but multiple keywords, separate the keywords with &quot; OR &quot;:</p>
<pre>
https://hnrss.org/newest?q=git+OR+linux
</pre>
<p>If your query contains <a href="https://en.wikipedia.org/wiki/Percent-encoding#Percent-encoding_reserved_characters">reserved characters</a> (especially the plus sign), you'll need to percent-encode those characters:</p>
<pre>
# This is the percent-encoded form of C++
https://hnrss.org/newest?q=C%2B%2B
</pre>

<h3 id="reply-feeds">Reply Feeds</h3>
<p>Keep an eye on replies to your comments:</p>
<pre>
https://hnrss.org/replies?id=jerf
</pre>
<p>Use a comment ID to follow replies to a particular comment:</p>
<pre>
https://hnrss.org/replies?id=17752464
</pre>

<h3 id="bestcomments">Best Comments</h3>
<p>Recent, highly voted comments from across Hacker News:</p>
<pre>
https://hnrss.org/bestcomments
</pre>
<p>Some great stuff in here in threads you may not normally have opened. Definitely recommended.</p>

<h3 id="self-post-feeds">Self Post Feeds</h3>
<p>Ask HN, Show HN, and polls are available:</p>
<pre>
https://hnrss.org/ask
https://hnrss.org/show
https://hnrss.org/polls
</pre>

<h3 id="alternative-feeds">Alternative Feeds</h3>
<p>Hacker News <a href="https://news.ycombinator.com/classic">Classic</a> only counts votes from "early users" (accounts created before February 13, 2008):</p>
<pre>
https://hnrss.org/classic
</pre>
<p>Hacker News <a href="https://news.ycombinator.com/best">Best</a> for top vote getters from the past few days:</p>
<pre>
https://hnrss.org/best
</pre>
<p>Hacker News <a href="https://news.ycombinator.com/invited">Invited</a> and <a href="https://news.ycombinator.com/pool">Pool</a> for reposted stories invited back by the mods and given a <a href="https://news.ycombinator.com/item?id=26998308">second chance</a>:</p>
<pre>
https://hnrss.org/invited
https://hnrss.org/pool
</pre>
<p>Hacker News <a href="https://news.ycombinator.com/active">Active</a> for posts with the most active, ongoing discussions:</p>
<pre>
https://hnrss.org/active
</pre>
<p>Hacker News <a href="https://news.ycombinator.com/launches">Launches</a> for "Launch HN" posts from YC affiliated startups:</p>
<pre>
https://hnrss.org/launches
</pre>


<h3 id="job-feeds">Job Feeds</h3>
<p>Job opportunities from YC funded startups:</p>
<pre>
https://hnrss.org/jobs
</pre>
<p>Top level comments in threads created by the whoishiring bot:</p>
<pre>
# Comments from "Who is hiring?" threads
https://hnrss.org/whoishiring/jobs

# Comments from "Who wants to be hired?" threads
https://hnrss.org/whoishiring/hired

# Comments from "Freelancer? Seeking freelancer?" threads
https://hnrss.org/whoishiring/freelance

# All of the above
https://hnrss.org/whoishiring
</pre>
<p>If you’re interested in something in particular, you can apply a <code>q=KEYWORD</code> parameter to only return relevant comments. For example, filter the top-level “Who is hiring?” comments to only those containing “React Native”:</p>
<pre>
https://hnrss.org/whoishiring/jobs?q=React+Native
</pre>

<h3 id="user-feeds">User Feeds</h3>
<p>If you don’t want to miss a post or comment by a given user, you can subscribe to that user’s feed:</p>
<pre>
https://hnrss.org/submitted?id=USERNAME # posts
https://hnrss.org/threads?id=USERNAME   # comments
https://hnrss.org/user?id=USERNAME      # everything
</pre>

<h3 id="favorite-feeds">Favorite Feeds</h3>
<p>Supply a username and get a feed of posts that have been "favorited" by that user:</p>
<pre>
https://hnrss.org/favorites?id=edavis
</pre>
<p>At the moment this only returns posts, not comments.</p>
<p>Note: This scrapes Hacker News first and then fetches from Algolia. For this reason, please be extra conservative with your refresh schedule. Thanks in advance.</p>

<h3 id="thread-feeds">Thread Feeds</h3>
<p>A chronological feed of new comments on a particular post can be found at:</p>
<pre>
https://hnrss.org/item?id=THREAD_ID
</pre>
<p>You can filter this feed by author by providing the <code>author</code> parameter:</p>
<pre>
https://hnrss.org/item?id=THREAD_ID&author=USERNAME
</pre>
<p>With <code>THREAD_ID</code> the numerical ID found in the URL when viewing the comments page and <code>USERNAME</code> being the author's username.</p>

<h2 id="feed-options">Feed Options</h2>
<p>You can modify any feed’s output using URL parameters. Multiple parameters can be applied at the same time by joining them with an ampersand.</p>

<h3 id="activity-parameters">Activity Parameters</h3>
<p>You can apply a <code>points=N</code> or <code>comments=N</code> parameter to any feed to filter the results so only entries with more than N points or comments are shown:</p>
<pre>
https://hnrss.org/newest?points=100
https://hnrss.org/ask?comments=25
</pre>
<p>You can also combine both parameters:</p>
<pre>
https://hnrss.org/show?points=100&comments=25
</pre>
<p>Unfortunately, <code>/newcomments</code> <a href="https://github.com/algolia/hn-search/issues/55#issuecomment-73599729">does not work</a> with a <code>points=N</code> parameter.</p>

<h3 id="search-parameter">Search Parameter</h3>
<p>By default, searches on posts only look at titles. If you want to search against the submitted URLs themselves, use the <code>search_attrs</code> parameter.</p>
<p>Here are some examples:</p>
<pre>
# Search for posts with "WordPress" in the title only
https://hnrss.org/newest?q=WordPress

# Search for posts with 'WordPress' in the URL only
https://hnrss.org/newest?q=WordPress&search_attrs=url

# Search for posts with 'WordPress' in the title or URL
https://hnrss.org/newest?q=WordPress&search_attrs=title,url

# Don't restrict search attributes at all. This searches for posts
# containing 'WordPress' in all attributes indexed by Algolia. This was
# the behavior of searches prior to June 3, 2015
https://hnrss.org/newest?q=WordPress&search_attrs=default
</pre>

<h3 id="link-parameter">Link Parameter</h3>
<p>By default, the RSS <code>&lt;link&gt;</code> element points to the submitted article’s URL. The <code>&lt;link&gt;</code> element can be changed to point to the Hacker News comment page by appending <code>link=comments</code> to the end of the URL. For example:</p>
<pre>https://hnrss.org/newest?link=comments</pre>

<h3 id="description-parameter">Description Parameter</h3>
<p>You can disable the <code>&lt;description&gt;</code> element entirely by passing the <code>description=0</code> parameter:</p>
<pre>https://hnrss.org/newest?description=0</pre>

<h3 id="count-parameter">Count Parameter</h3>
<p>By default, feeds return 20 RSS items. This can be increased via the <code>count=N</code> parameter:</p>
<pre>https://hnrss.org/newest?count=50</pre>
<p>There is a hardcoded limit of 100 entries, so keep that in mind.</p>

<h3 id="feed-formats">Feed Formats</h3>
<p>By default, feeds come back as RSS. But if you add “.atom” or “.jsonfeed” to any endpoint you’ll receive the contents in <a href="https://validator.w3.org/feed/docs/atom.html">Atom</a> or <a href="https://jsonfeed.org/">JSON Feed</a>, respectively.</p>
<pre>
# The front page as Atom
https://hnrss.org/frontpage.atom

# "Ask HN" with 10 or more comments as JSON Feed
https://hnrss.org/ask.jsonfeed?comments=10
</pre>
<p>Note: These formats are a lot less battle-tested than the RSS format. If you see any wonkiness or they don’t play nicely with your feed reader, please <a href="https://github.com/hnrss/hnrss/issues/new">open an issue</a> with as much information as possible. Thanks!</p>

<h2 id="credits">Credits</h2>
<p>Thanks to <a href="https://www.algolia.com/">Algolia</a> for providing their <a href="https://hn.algolia.com/api">REST API</a>. Without it, hnrss.org simply would not exist.</p>
<p>Thanks to <a href="https://github.com/jaredandrews">Jared Andrews</a> for the <a href="https://github.com/hnrss/hnrss/pull/23">PR</a> that created the /whoishiring/ endpoints.</p>
<p>Thanks to <a href="https://github.com/zmwangx">Zhiming Wang</a> for adding Python 3 support.</p>
<p>Thanks to <a href="https://github.com/grantjenks">Grant Jenks</a> for the idea of adding the Article URL and Points to the description.</p>
<p>Thanks to <a href="https://github.com/cagrimmett">Chuck Grimmett</a> for being a sounding board when it comes to adding new features to hnrss.org as well as suggesting the /jobs endpoint.</p>
<p>And many, many thanks to all those who have donated in support of the project over the years. You all mean the world to me.</p>

<h2 id="colophon">Colophon</h2>
<p>hnrss.org is powered by the Gin web framework, served by nginx, and hosted on DigitalOcean. HTTPS is provided by Let’s Encrypt. DNS is provided by Namecheap.</p>

<p class="updated">This documentation was last updated on December 14, 2022.</p>

## Scraped from https://hnrss.github.io/updates.xml
<?xml version="1.0" encoding="utf-8"?>
<rss version="2.0">
  <channel>
    <title>hnrss.org updates</title>
    <link>https://hnrss.org/</link>
    <description>A feed announcing updates related to hnrss.org</description>
    <item>
      <title><![CDATA[Development RSS feed location has moved]]></title>
      <description><![CDATA[<p>Please point your feed reader to https://github.com/hnrss/hnrss/releases.atom to continue receiving hnrss development updates. Thanks!</p>]]></description>
      <link>https://github.com/hnrss/hnrss/releases.atom</link>
      <pubDate>Wed, 14 Dec 2022 22:19:53 +0000</pubDate>
      <guid isPermaLink="false">08e7b58c-ca3f-4d1e-9f41-1b2ec33506d3</guid>
    </item>
    <item>
      <title><![CDATA[hnrss.org now supports the Second-Chance Pool]]></title>
      <description><![CDATA[<p>The URL is https://hnrss.org/pool and more information is available <a href="https://news.ycombinator.com/item?id=26998308">here</a></p>]]></description>
      <link>https://hnrss.github.io/#alternative-feeds</link>
      <pubDate>Sat, 1 May 2021 23:37:38 +0000</pubDate>
      <guid isPermaLink="false">6e40216a-20b0-4aae-aa04-8df78a021234</guid>
    </item>
    <item>
      <title><![CDATA[hnrss.org now supports filtering thread comments by user]]></title>
      <description><![CDATA[<p>Attach <code>&author=USERNAME</code> to a thread feed to only see comments from that user.</p>
<p>Like so: <a href="https://hnrss.org/item?id=23778510&author=edavis">https://hnrss.org/item?id=23778510&author=edavis</a></p>]]></description>
      <link>https://hnrss.github.io/#thread-feeds</link>
      <pubDate>Mon, 16 Nov 2020 00:05:13 +0000</pubDate>
      <guid isPermaLink="false">1bdd700d-2b3a-4c23-8347-62577d9fb7da</guid>
    </item>
    <item>
      <title><![CDATA[New endpoints for Best, Invited, Active, and Launches]]></title>
      <description><![CDATA[<ul>
<li><a href="https://hnrss.org/best">https://hnrss.org/best</a> for the top recent vote getters</li>
<li><a href...


## Scraped from https://news.ycombinator.com/
Hacker NewsHacker Newsnew | past | comments | ask | show | jobs | submitlogin1.Ask HN: Has anyone else been unemployed for over two years?97 points by ncarlson 53 minutes ago | hide | 47&nbsp;comments2.Feedmaker: URL + CSS selectors = RSS feed (feedmaker.fly.dev)9 points by mustaphah 40 minutes ago | hide | discuss3.An untidy history of AI across four books (hedgehogreview.com)59 points by ewf 3 hours ago | hide | 23&nbsp;comments4.Ants that seem to defy biology – They lay eggs that hatch into another species (smithsonianmag.com)266 points by sampo 9 hours ago | hide | 85&nbsp;comments5.R MCP Server (github.com/finite-sample)42 points by neehao 3 hours ago | hide | 2&nbsp;comments6.Three-Minute Take-Home Test May Identify Symptoms Linked to Alzheimer&#x27;s Disease (smithsonianmag.com)27 points by pseudolus 2 hours ago | hide | 1&nbsp;comment7.Your very own humane interface: Try Jef Raskin&#x27;s ideas at home (arstechnica.com)38 points by zdw 4 hours ago | hide | discuss8.The Economic Impacts of AI: A Multidisciplinary, Multibook Review [pdf] (kevinbryanecon.com)25 points by cjbarber 2 hours ago | hide | 9&nbsp;comments9.Time Spent on Hardening (third-bit.com)26 points by mooreds 1 hour ago | hide | 10&nbsp;comments10.Internet Archive&#x27;s big battle with music publishers ends in settlement (arstechnica.com)233 points by coloneltcb 10 hours ago | hide | 96&nbsp;comments11.Show HN: WeUseElixir - Elixir project directory (weuseelixir.com)27 points by taddgiles 1 hour ago | hide | 2&nbsp;comments12.Ruby Central&#x27;s Attack on RubyGems [pdf] (pup-e.com)553 points by jolux 13 hours ago | hide | 168&nbsp;comments13.Safepoints and Fil-C (fil-c.org)49 points by matt_d 5 hours ago | hide | 19&nbsp;comments14.Show the Physics (tudelft.nl)125 points by pillars 9 hours ago | hide | 7&nbsp;comments15.Kernel: Introduce Multikernel Architecture Support (lwn.net)67 points by ahlCVA 6 hours ago | hide | 10&nbsp;comments16.Revamping an Old TV as a Gift (2019) (davidv.dev)47 poin...


## Scraped from https://hnrss.org/newest
<rss version="2.0" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:atom="http://www.w3.org/2005/Atom"><channel><title>Hacker News: Newest</title><link>https://news.ycombinator.com/newest</link><description>Hacker News RSS</description><docs>https://hnrss.org/</docs><generator>hnrss v2.1.1</generator><lastBuildDate>Fri, 19 Sep 2025 21:49:37 +0000</lastBuildDate><atom:link href="https://hnrss.org/newest" rel="self" type="application/rss+xml"></atom:link><item><title><![CDATA[Trump to announce $100K fee for H-1B specialty visas]]></title><description><![CDATA[
<p>Article URL: <a href="https://www.politico.com/news/2025/09/19/trump-to-announce-100k-fee-for-h-1b-specialty-visas-00573709">https://www.politico.com/news/2025/09/19/trump-to-announce-100k-fee-for-h-1b-specialty-visas-00573709</a></p>
<p>Comments URL: <a href="https://news.ycombinator.com/item?id=45307052">https://news.ycombinator.com/item?id=45307052</a></p>
<p>Points: 1</p>
<p># Comments: 0</p>
]]></description><pubDate>Fri, 19 Sep 2025 21:45:46 +0000</pubDate><link>https://www.politico.com/news/2025/09/19/trump-to-announce-100k-fee-for-h-1b-specialty-visas-00573709</link><dc:creator>raw_anon_1111</dc:creator><comments>https://news.ycombinator.com/item?id=45307052</comments><guid isPermaLink="false">https://news.ycombinator.com/item?id=45307052</guid></item><item><title><![CDATA[Wait Smart Glasses Are Suddenly Good? [video]]]></title><description><![CDATA[
<p>Article URL: <a href="https://www.youtube.com/watch?v=7gtc1DW2Tgo">https://www.youtube.com/watch?v=7gtc1DW2Tgo</a></p>
<p>Comments URL: <a href="https://news.ycombinator.com/item?id=45307044">https://news.ycombinator.com/item?id=45307044</a></p>
<p>Points: 2</p>
<p># Comments: 0</p>
]]></description><pubDate>Fri, 19 Sep 2025 21:44:52 +0000</pubDate><link>https://www.youtube.com/watch?v=7gtc1DW2Tgo</link><dc:creator>doener</dc:creator><comments>https://news.ycombinator.com/item?id=45307044</comments><guid isPermaLink="false">https://news.ycombinator.co...


## connections
- processed from phone shortcut
