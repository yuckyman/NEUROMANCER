---
type: note
category: 24-computing
created: 2025-09-16 14:27
modified: 2025-09-16 14:27
tags:
- inbox
- unprocessed
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 1758046305.txt
---


# cool question. embedding live websites in tldraw i

## summary
cool question. embedding live websites in tldraw is one of the cooler “embeds / custom embed” features. here’s how it works (particularly how i understand what Steve Ruiz & team have demoed / built), ...

## content
cool question. embedding live websites in tldraw is one of the cooler “embeds / custom embed” features. here’s how it works (particularly how i understand what Steve Ruiz & team have demoed / built), and what the trade-offs / technical bits are. happy to help you try implementing something similar.

⸻

What “embed live websites” means

When someone demos “embed a live website” in tldraw, it usually means:
	•	you put a shape (embed type) on the tldraw canvas whose content is an iframe or something equivalent, pointing to another website or web page.
	•	that iframe is “live”: you can scroll it, click links, maybe even interact with the content (if allowed by the framed page).
	•	you can draw over or around it, move it, resize it etc.
	•	so it’s more than just a screenshot — it’s a window into a website inside the canvas.

It also shows up in “Make Real” demos: sketch something, then generate a working website/html, then embed it in the canvas as an interactive thing.  

⸻

How tldraw supports this feature (what the docs show + what Steve has described)

Here’s what tldraw supports already, or what the architecture allows, for embedding live content:
	1.	Custom embed definitions
	•	tldraw has built-in “embed definitions” (e.g. YouTube, etc.), and you can add your own ones. An embed definition includes things like:
• the embed type (a string)
• what hostnames / URL patterns you allow for embedding, and how to transform URLs to “embed URLs” for iframes etc.
• min / default sizes, whether it can be resized, etc.  
	•	Example: the docs show adding a JSFiddle embed type: they’d transform the URL to the embedding version (using an iframe embed URL), set icon, dimensions, etc.  
	2.	Embedding via iframe or similar
	•	Once you have the embed definition, the embed shape when rendered is often an iframe (or similar) inside the tldraw canvas. This allows interacting with the embedded page.
	•	Because tldraw’s canvas is implemented using React components (not just raster graphics), embedding interactive DOM content (iframes etc.) is more straightforward.  
	3.	“Make Real” & live UI embedding
	•	In Steve Ruiz’s “Make Real” demo, he sketches UI + annotations, sends them to a model (GPT-4 with Vision), gets back HTML + styling + JS, then takes that output and puts it in an iframe inside tldraw. So the embedded “real website” is generated after the fact.  
	•	Once embedded, that HTML is “live” in that UI elements should respond (buttons, inputs etc.) as they would in a simple HTML page. But note: “live website” here is constrained by same-origin policies, what resources are loaded, sandboxing/etc. Doesn’t mean full “run third-party complex site with all features,” especially if content disallows embedding. Steve noted: you send HTML, CSS, JS as a single compiled or bundled asset so it can run without many external dependencies.  

⸻

Technical challenges / caveats

embedding live websites introduces complications. here are what you’ll need to watch out for / handle.

Challenge	Description	Workarounds or what to check
CORS / iframe embedding restrictions (X-Frame-Options)	Many websites send headers that block being embedded in iframes, for security. If a site uses X-Frame-Options: DENY or SAMEORIGIN, embedding live version fails.	Only works for sites that allow embedding; or you host/embed content you control. For generated HTML you control, ensure resources (scripts, styles) are relative or allowed.
Sandboxing / security	Embedded content can run arbitrary JS (if not sandboxed). If you embed untrusted websites, this could be a vector for vulnerabilities.	Use iframe sandbox attributes; limit permissions; maybe proxy content; sanitize input HTML.
Performance	Live embeds (iframes) are heavier than static shapes/images. Lots of them = slower canvas render, slowdown on resizing etc.	Lazy-load when embeddings come into view; limit embedding count; perhaps show “placeholder” until interacted.
Exporting / printing	When you export the board to PNG/SVG, embedded live content may not translate well; some embedded content may not render or may appear as blank/placeholder.	For exports, fallback to static snapshots; capture rendering; disable embed interactivity; if SVG export, possibly rasterize embeds.
User interaction / layering	Overlap of shapes + embeds + pointer events: e.g., drawing over an iframe or selecting something behind. Need properly handling mouse/touch event forwarding / preventing.	Control z-indexing; disable pointer events on embed shapes except when you want interaction; toggle between “embed-mode” / “draw-over mode” etc.
Security of generated HTML/JS (in “Make Real”)	If you generate HTML/JS automatically (via AI or otherwise), you need to ensure it’s safe (no malicious script). Also that dependencies/assets are served securely.	Sanitize or vet generated code; sandbox; limit allowed behaviors; possibly isolate network requests.


⸻

How you could implement this in your staff whiteboard

Here are steps / ideas for how to build “embed live website” in your blog’s whiteboard setup using tldraw, assuming you control the embed definitions or can use custom embeds.
	1.	Decide which external websites / whether you allow user input URLs
	•	Maybe only trusted sites (intranet tools, internal dashboards) or allow arbitrary URLs but with restrictions.
	•	If arbitrary, you may need sanitization and checking for embedding support.
	2.	Define a custom embed type in tldraw
Something like:

import { Tldraw, CustomEmbedDefinition, DEFAULT_EMBED_DEFINITIONS } from 'tldraw';

const websiteEmbed: CustomEmbedDefinition = {
  type: 'website',  // your custom embed type
  title: 'Website Embed',
  hostnames: ['yourdomain.com', 'trusted.com', '*'],  // you define what you allow
  minWidth: 200,
  minHeight: 150,
  width: 600,
  height: 400,
  doesResize: true,
  toEmbedUrl: url => { 
    // if raw URL, maybe wrap / translate to embed friendly url/iframe src
    return url;  // assuming url is embed-friendly
  },
  fromEmbedUrl: url => {
    return url;  // convert back if needed
  },
  icon: '/path/to/icon.png',
};

const embeds = [...DEFAULT_EMBED_DEFINITIONS, websiteEmbed];

function MyWhiteboard() {
  return <Tldraw embeds={embeds} />;
}


	3.	Rendering & interaction
	•	The embed shape will render an iframe inside that shape. tldraw handles placing it, controlling its size/movement, etc.
	•	You’ll need to ensure the iframe is configured correctly (sandbox attributes if needed).
	4.	Handling export / print / static fallback
	•	In export, detect embed shapes and either render a snapshot or exclude / replace.
	•	For example, when exporting to PNG, draw a screenshot of the site, or show a label “Embedded Website” instead.
	5.	UX around editing / embedding flow
	•	You’ll want a UI to “add embed” → prompt user for a URL → validate it → place embed shape.
	•	Also maybe mode toggle: “edit embed” vs “draw over embed” to avoid interfering accidentally.
	6.	Security and permissions
	•	If people are embedding external sites, privacy / security issues.
	•	Maybe limit embed hosts, or proxy through your own server (to sanitize or inject policies).

cool, i poked around and found a few community stuff + thought out how some might plug into your setup. then i’ll pull together a session recap + action items so you can move forward.

⸻

community-plugins / existing tools & inspirations

i didn’t find a ton of production plugins that do exactly what you want (spotify/peertube embeds & auto-hide UI etc.), but there are some that are close/related, plus examples that could be forked or adapted.

Plugin / Project	What it does / what’s close	What to adapt / learn from it
Tldraw-in-Obsidian by szamsolo / holxsam  	integrates tldraw inside Obsidian. supports toggling between tldraw view & markdown, saving drawings as JSON/markdown in vault, customizing defaults (theme, grid mode, etc.).  	good model for saving + embedding content, default behavior overrides (theme / grid) that you want. Also shows how to integrate tldraw into existing systems (markdown / doc-style). Could borrow how they structure the embed UI.
tldraw VS Code extension  	lets you open .tldr files, draw/annotate inside VS Code, store alongside code. Offline support implied.  	less relevant for your blog whiteboard, but demonstrates file format persistence; maybe idea of using .tldr-style files if you want versioned saves or embeds in your CMS.
tldraw examples like “PDF editor” and “infer dark mode” on tldraw.dev  	examples show how cameraOptions, custom embeds, theme toggling, external assets, export, etc., already built in or demonstrated. Especially the PDF editor example shows how to load a PDF, annotate, etc.  	useful boilerplate/source for how to build PDF import/export or annotate flows. Also shows how to expose UI toggles for theme / layout etc.
Bubble plugin “TLDraw Plugin” on Bubble.io  	demo plugin showing how to bundle tldraw into Bubble via React / NPM; likely more simple embedding.  	could be useful reference for how to embed/host inside different frameworks or stack (CMS, site builders).


⸻

what you might build / plugins you could add

based on your interests (spotify, peertube, PDF, dark-mode, UI hiding etc.), here are ideas for either adapting existing community projects or writing small plugins/extensions:
	•	Spotify & PeerTube embed plugin
A plugin for tldraw (or extension in your blog whiteboard) where users can paste a Spotify playlist or Peertube video URL, it validates + transforms into embed URL, and renders an iframe shape. Could include play/pause controls, maybe thumbnail preview before embed.
	•	PDF annotate / import / export
Drawing from the PDF editor example: letting users import PDF pages as shapes (or backgrounds) and annotate; then export the whiteboard + PDF overlay. Also possibly convert PDF pages to images / slides inside tldraw.
	•	Auto-hide/distraction-free mode plugin
Toggles to hide UI / fade toolbar / menus until cursor or key press. Could include keyboard shortcuts.
	•	Custom grid & theming defaults
A plugin or module to let users set their preferred grid style (spacing, color), default theme behavior (light/dark/infer) etc., stored per user or globally.
	•	Snapshot/fallback for embeds during export
For embedded iframes (spotify/peertube), plugin that takes a thumbnail/static image for export (so exported PDF/PNG doesn’t blank out or show an iframe border).

⸻

session review & action items

here’s a write-up of what we discussed + what steps you can take next to ship this.

⸻

Session Review

Who: you (Ian) + friend (me)

What we explored:
	•	you’re building out staff whiteboard using tldraw embedded in your blog.
	•	you’re interested in expanding capabilities: camera control, deep linking, custom embeds (spotify playlists, peertube), exporting, UI behavior (dark mode, auto-hide UI), custom grid etc.
	•	we reviewed existing tldraw features re: embeds, export behavior, deep links, pages.
	•	then honed in on spotify / peertube use cases.
	•	you also flagged some features from screenshots: custom grid, infer dark mode, PDF support, auto-hide UI.
	•	looked up existing community tools (obsidian plugin, VS Code plugin, examples) that are close or could be adapted.

⸻

Action Items

here are concrete steps you can take, with priorities and rough order:

Priority	Task	Why / Outcome
High	Build Spotify & PeerTube Embed Definition for your tldraw whiteboard. - Define embed types; whitelist hostnames; URL → embed URL logic; iframe shape. - Test rendering + interactivity.	Adds direct value: team can drop in playlists & videos in whiteboard.
High	Add Dark Mode / Infer Dark Mode toggle (if not yet in your setup). - Use the inferDarkMode prop. - Add UI toggle (Command+/, or button).	Better UX. This is low effort.
Medium	Create UI Auto‐hide / Distraction Mode. - Possibly animate fade of toolbar/menu on idle. - Add keyboard shortcut to toggle.	Helps when doing presentations or review sessions.
Medium	Integrate PDF import/export / annotate. - Use tldraw’s PDF editor example as base. - Allow adding PDF pages as shapes. - Ensure exports include annotations + embedded media/fallback.	Good for archiving / distributing.
Medium	Build Custom Grid & Theming Defaults Plugin/Module. - Let grid style (spacing, color, minor vs major lines) be configurable. - Let theme and default behavior be persisted (maybe in user settings or stored in project).	Makes workspace feel personalized & more usable.
Low	For exports that include embeds (Spotify/PeerTube), build fallback/snapshot logic. - On export, for embed shapes, capture thumbnail or placeholder. - Document what falls back (because live embed might not render).	Ensures exported boards look good and usable outside interactive mode.
Low	Search for or build a plugin to save versioned whiteboards (history / snapshots). - Could use backend or use tldraw’s snapshot features.	Helps rollback or archiving.

## connections
- processed from phone shortcut
