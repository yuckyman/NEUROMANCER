# reMarkable Notes Processing

This directory contains reMarkable tablet notes and an automated GitHub Actions workflow for processing them.

## 📁 Directory Structure

```
3_projects/32_remarkable/
├── README.md                    # This file
├── *.svg                        # Original reMarkable SVG files
└── *.md                         # Processed markdown files with frontmatter
```

## 🔄 Automated Workflow

The GitHub Actions workflow (`.github/workflows/remarkable-processor.yml`) automatically processes reMarkable notes when you add SVG files to this directory.

### Workflow Features

1. **SVG to Markdown Conversion**: Converts SVG drawings to markdown files
2. **YAML Frontmatter**: Adds structured metadata to each note
3. **UUIDv5 Generation**: Creates unique identifiers for each note
4. **Auto-commit**: Automatically commits processed files back to the repository

### What Gets Generated

For each SVG file (e.g., `my-note.svg`), the workflow creates a corresponding markdown file (`my-note.md`) with:

```yaml
---
id: <UUIDv5>
title: My Note
created: <ISO 8601 timestamp>
modified: <ISO 8601 timestamp>
type: remarkable-note
source: reMarkable
tags:
  - remarkable
  - handwriting
  - notes
svg_file: my-note.svg
---

# My Note

**UUID:** `<generated-uuid>`

## Original Note

![My Note](my-note.svg)

## Transcription

_Add transcription or notes here_

## Metadata

- **Source File:** `my-note.svg`
- **Processed:** <timestamp>
- **UUID:** <uuid>
```

## 🚀 Usage

### Adding New Notes

1. Export SVG files from your reMarkable tablet
2. Add the SVG files to this directory
3. Commit and push to GitHub:
   ```bash
   git add 3_projects/32_remarkable/*.svg
   git commit -m "Add reMarkable notes"
   git push
   ```
4. The workflow will automatically:
   - Detect the new SVG files
   - Generate markdown files with frontmatter
   - Create UUIDs for each note
   - Commit the processed files

### Manual Trigger

You can also manually trigger the workflow from the GitHub Actions tab:
1. Go to **Actions** → **reMarkable Notes Processor**
2. Click **Run workflow**
3. Select the branch and run

## 📝 Post-Processing

After the workflow runs, you can:

1. Edit the generated markdown files to add transcriptions
2. Update tags and metadata as needed
3. Link notes to other content in your vault
4. Add additional context or annotations

## 🔧 Workflow Configuration

The workflow is configured to:
- Trigger on pushes to `3_projects/32_remarkable/**`
- Run on the `main` branch
- Use Python 3.11 for processing
- Auto-commit with GitHub Actions bot credentials

## 📊 Monitoring

Check the workflow status:
- **Actions Tab**: View workflow runs and logs
- **Commit History**: See automated commits from the bot
- **Step Summary**: Review processing results after each run

## 🛠️ Dependencies

The workflow uses:
- Python 3.11
- PyYAML (for frontmatter)
- UUID (for ID generation)
- Pillow & CairoSVG (for image processing)

## 🔗 Related Files

- Workflow: [.github/workflows/remarkable-processor.yml](../../.github/workflows/remarkable-processor.yml)
- Project Overview: [32.00_remarkable_sync.md](./32.00_remarkable_sync.md)

---

**Last Updated:** 2025-10-20  
**Maintained By:** GitHub Actions Bot
