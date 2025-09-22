---
type: note
category: 24-computing
created: 2025-09-22 10:28
modified: 2025-09-22 10:28
tags:
- tag1
- tag2
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 1758514286.txt
content_hash: 674b9ff42080b34ef02254a8ef76324aa1c0cbd6d934b188cd69ec8ffd1351b9
---


# Unique Filenames for Logging

## summary
Create a unique filename per capture with a timestamp and UUID for easy filtering.

## content
ok, got it — you’re basically building a capture → sync → process → rotate pipeline, with apple shortcuts as the mobile front-end and your server (yuckbox) doing the heavy lifting. let’s break it down piece by piece:

⸻

1. unique filenames for logging

instead of appending to one big file (messy to parse), have the shortcut create a new file per capture with a unique name.

filename convention:

quadlog-<timestamp>-<uuid>.md

example:

quadlog-20250921-233015-84f2.md

inside:

buy protein powder #quad/dd @someday +fitness

this makes it trivial to filter later (just ls quadlog-*).

⸻

2. sending over ssh

in shortcuts you can use the Run Script Over SSH action. setup:
	•	server: ian@yuckbox
	•	path: /home/ian/NEUROMANCER/0_admin/01_inbox/

shortcut flow:
	1.	Ask for Input (task description).
	2.	Choose from Menu (quadrant tag).
	3.	Choose from Menu (priority tag).
	4.	Combine Text → build file body.
	5.	Run Script Over SSH → cat > /home/ian/NEUROMANCER/0_admin/01_inbox/quadlog-$(date +%s).md and pipe in the body.

⸻

3. cron-powered processing on server

you can have a cron job (say every 15m) run a script like:

#!/bin/bash
inbox="/home/ian/NEUROMANCER/0_admin/01_inbox"
archive="/home/ian/NEUROMANCER/0_admin/01_inbox/archive"
csv="/home/ian/NEUROMANCER/0_admin/quadrant_log.csv"

mkdir -p "$archive"

for f in $inbox/quadlog-*.md; do
    [ -e "$f" ] || continue
    entry=$(cat "$f")
    ts=$(basename "$f" | cut -d'-' -f2)  # timestamp from filename
    echo "$ts,\"$entry\"" >> "$csv"
    mv "$f" "$archive/"
done

now you have a running CSV with timestamp,entry.

⸻

4. centralized storage → dashboard

later, the CSV can feed:
	•	a TUI dashboard (python curses app)
	•	discord bot/habit tracker (parse daily slice)
	•	generate dynamic eisenhower matrix (filter #quad/... into quadrants).

⸻

5. workout logger (shortcut twin)

make another shortcut, same flow but:
	•	ask for “type of workout” (pushups, run, etc.)
	•	ask for “quantity” (e.g. reps/mins)
	•	auto-tag as #quad/dd +fitness
	•	send over ssh same way.

entry example:

pushups 40 reps #quad/dd +fitness


⸻

6. automation: random daily rotation

trickiest part on iOS, since Shortcuts doesn’t have great random selection from files. two options:
	•	Option A (server-side):
have your cron script also generate a daily.md each morning by randomly sampling 1 from each quadrant in the CSV. then sync that file back to your phone (icloud / git / even email).
	•	Option B (pure shortcut):
	1.	“Get File Contents” of the central CSV (or inbox).
	2.	“Filter Lines” by #quad/od, etc.
	3.	“Get Random Item” (there’s a built-in action).
	4.	Assemble them into a markdown block.

(but i’d lean toward server-side for sanity — your phone won’t choke on big lists later.)

⸻

7. keeping up through the day
	•	run the “rotation” shortcut in the morning → creates a daily note.
	•	check it via apple notes, obsidian, or even cat the file over ssh.
	•	optional: add a “mark done” shortcut that ssh’s to append ✓ to the line in today’s file.

⸻

so the flow becomes:
	•	capture quickly on phone (shortcuts → ssh → yuckbox inbox).
	•	cron consolidates into CSV + rotates tasks.
	•	daily note is generated server-side (or pulled random by shortcut).
	•	you track progress either from your phone or TUI/discord later.

⸻

want me to write out the actual shortcut steps (like menu structure + exact actions) so you can literally build it click-by-click in the Shortcuts app?

## connections
- processed from phone shortcut
