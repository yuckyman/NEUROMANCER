---
type: note
category: 24-computing
created: 2025-09-22 10:28
modified: 2025-09-22 10:28
tags:
- dev-log
- project
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 20250922_102659_rss_Obsidian_2025.08.22__Public_.txt
content_hash: bad4f17c07dd1c3b2567d13f617713d804c2788b751a996b5d6ce684d531407c
---


# Obsidian 2025.08.22 (Public) Obsidian Sync upgrade - new security features

## summary
Obsidian 2025.08.22 (Public) has received a security upgrade to ensure better file encryption and path integrity.

## content
RSS Feed: Obsidian Changelog
Source: https://obsidian.md/changelog.xml
Link: https://obsidian.md/changelog/2025-08-22-sync/

Obsidian 2025.08.22 (Public)

Obsidian Sync has received a minor security upgrade. File names have always been end-to-end encrypted, but they're now protected using an even stronger method. All new vaults automatically use this stronger encryption. Existing vaults can be upgraded with the new migration assistant in Obsidian 1.9.11. The old method of encrypting file paths and hashes derived the initialization vector (IV) from a hash of the string. In rare cases, this could create a pattern that an attacker might try to take advantage of if they were able to get access to your encrypted data. Now, file paths and hashes are encrypted with AES-SIV so those patterns can no longer exist. The way file contents are encrypted hasn't changed, they've always been secured with AES-GCM.

## Scraped from https://obsidian.md/changelog.xml
<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom" xml:base="en">
	<title>Obsidian Changelog</title>
	<subtitle>Follow new releases of Obsidian for mobile and desktop.</subtitle>
	<link href="https://obsidian.md/changelog.xml" rel="self"/>
	<link href="https://obsidian.md/"/>
	<updated>2025-09-19T00:00:00Z</updated>
	<id>https://obsidian.md/</id>
	<author>
		<name>Obsidian</name>
	</author>
	
	<entry>
		<title>Obsidian 1.9.13 Mobile (Early access)</title>
		<link href="https://obsidian.md/changelog/2025-09-19-mobile-v1.9.13/"/>
		<updated>2025-09-19T00:00:00Z</updated>
		<id>https://obsidian.md/changelog/2025-09-19-mobile-v1.9.13/</id>
		<content type="html">&lt;ul&gt;
&lt;li&gt;Includes all new functionality and bug fixes up to Obsidian Desktop v1.9.13.&lt;/li&gt;
&lt;/ul&gt;
&lt;h2&gt;No longer broken&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;iPadOS 26: Fixed screen shrinking after switching apps.&lt;/li&gt;
&lt;li&gt;iPadOS 26: Fixed toolbar getting incorrectly positioned.&lt;/li&gt;
&lt;li&gt;Android: Fixed toolbar and navigation bar being incorrectly positioned on Android 10 and below.&lt;/li&gt;
&lt;/ul&gt;
&lt;h2&gt;Developers&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;Fixed default layout of &lt;code&gt;Modal&lt;/code&gt; on phone sizes. Modals are now always pinned to the bottom of the screen by default.&lt;/li&gt;
&lt;li&gt;Fixed close button not working on &lt;code&gt;Modal&lt;/code&gt; instances.&lt;/li&gt;
&lt;/ul&gt;
</content>
	</entry>
	
	<entry>
		<title>Obsidian 1.9.13 Desktop (Early access)</title>
		<link href="https://obsidian.md/changelog/2025-09-19-desktop-v1.9.13/"/>
		<updated>2025-09-19T00:00:00Z</updated>
		<id>https://obsidian.md/changelog/2025-09-19-desktop-v1.9.13/</id>
		<content type="html">&lt;h2&gt;No longer broken&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;Improved performance when opening quick switcher and command palette when using the latest Obsidian 1.9 installer (Electron v35+).&lt;/li&gt;
&lt;li&gt;Fix...


## Scraped from https://obsidian.md/changelog/2025-08-22-sync/
Obsidian 2025.08.22 (Public) - Obsidian Download Pricing Sync Publish Enterprise Community Account Download Account Sync Publish Pricing Plugins Enterprise Web Clipper Learn more Help About Blog Discord Changelog Community Roadmap Security Merch store Privacy Changelog Follow Obsidian updates and improvements. RSS Discord Twitter Bluesky Mastodon August 22, 2025 2025.08.22 Sync public Obsidian Sync has received a minor security upgrade. File names have always been end-to-end encrypted, but they're now protected using an even stronger method. All new vaults automatically use this stronger encryption. Existing vaults can be upgraded with the new migration assistant in Obsidian 1.9.11. The old method of encrypting file paths and hashes derived the initialization vector (IV) from a hash of the string. In rare cases, this could create a pattern that an attacker might try to take advantage of if they were able to get access to your encrypted data. Now, file paths and hashes are encrypted with AES-SIV so those patterns can no longer exist. The way file contents are encrypted hasn't changed, they've always been secured with AES-GCM. Previous release August 22, 2025 1.9.11 Mobile catalyst Next release August 25, 2025 1.9.12 Desktop catalyst Get started Download Pricing Enterprise Account Obsidian Overview Sync Publish Canvas Mobile Web Clipper Plugins Learn Help Developers Changelog About Roadmap Blog Resources System status License overview Terms of service Privacy policy Security Community Join the community Discord Forum / 中文论坛 Merch store Brand guidelines Follow us Discord Twitter Bluesky Threads Mastodon YouTube GitHub © 2025 Obsidian


## connections
- processed from phone shortcut
