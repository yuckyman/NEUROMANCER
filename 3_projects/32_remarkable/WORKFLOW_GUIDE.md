# reMarkable Notes Workflow Quick Guide

## 🎯 Quick Start

### 1. Export Notes from reMarkable
- Connect your reMarkable tablet to your computer
- Export notes as SVG files
- Save them locally

### 2. Add to Repository
```bash
# Navigate to your local NEUROMANCER repository
cd /path/to/NEUROMANCER

# Copy SVG files to the remarkable directory
cp /path/to/exported/*.svg 3_projects/32_remarkable/

# Add to git
git add 3_projects/32_remarkable/*.svg

# Commit with a descriptive message
git commit -m "Add reMarkable notes from [date/topic]"

# Push to GitHub
git push origin main
```

### 3. Workflow Runs Automatically
The GitHub Actions workflow will:
- ✅ Detect new SVG files
- ✅ Generate markdown files with YAML frontmatter
- ✅ Create UUIDv5 identifiers
- ✅ Commit processed files automatically
- ✅ Notify you of completion

### 4. Pull Changes
```bash
# Pull the processed markdown files
git pull origin main

# Your markdown files are now ready!
```

## 📋 What You Get

For each `note.svg`, you'll get `note.md` with:

```markdown
---
id: <uuid-v5>
title: Note
created: 2025-10-20T03:54:22Z
modified: 2025-10-20T03:54:22Z
type: remarkable-note
source: reMarkable
tags:
  - remarkable
  - handwriting
  - notes
svg_file: note.svg
---

# Note

**UUID:** `12345678-abcd-...`

## Original Note
![Note](note.svg)

## Transcription
_Add transcription or notes here_

## Metadata
- **Source File:** `note.svg`
- **Processed:** 2025-10-20T03:54:22Z
- **UUID:** 12345678-abcd-...
```

## 🔧 Customization

### Edit Generated Markdown
After processing, you can:

1. **Add Transcription**: Replace placeholder text
2. **Update Tags**: Modify the tags array in frontmatter
3. **Add Links**: Link to other notes or pages
4. **Enhance Metadata**: Add custom fields

Example:
```yaml
---
id: 12345678-abcd-...
title: Meeting Notes - Project Alpha
created: 2025-10-20T03:54:22Z
modified: 2025-10-20T04:30:00Z
type: remarkable-note
source: reMarkable
tags:
  - remarkable
  - meeting
  - project-alpha
  - 2025-q4
svg_file: meeting-2025-10-20.svg
project: "[[Project Alpha]]"
attendees:
  - Alice
  - Bob
---
```

### Batch Processing

Process multiple notes at once:
```bash
# Add all SVGs in a folder
cp /path/to/notes/*.svg 3_projects/32_remarkable/

# Commit all at once
git add 3_projects/32_remarkable/
git commit -m "Batch import: Week 42 notes"
git push
```

## 🔍 Troubleshooting

### Workflow Not Running
1. Check GitHub Actions tab for errors
2. Verify files are in `3_projects/32_remarkable/`
3. Ensure SVG files have `.svg` extension
4. Check workflow permissions in repository settings

### Duplicate Files
- The workflow processes ALL `.svg` files each run
- Already-processed files get updated timestamps
- Use meaningful filenames to avoid confusion

### Manual Trigger
If automatic trigger fails:
1. Go to **Actions** tab on GitHub
2. Select **reMarkable Notes Processor**
3. Click **Run workflow**
4. Choose `main` branch
5. Click **Run workflow** button

## 💡 Tips & Best Practices

### File Naming
Use descriptive names for your SVG files:
- ✅ `meeting-notes-2025-10-20.svg`
- ✅ `sketch-app-wireframe.svg`
- ✅ `idea-new-feature.svg`
- ❌ `note1.svg`
- ❌ `untitled.svg`

### Organization
Consider subdirectories for different types:
```
32_remarkable/
├── meetings/
├── sketches/
├── ideas/
└── journal/
```

### Version Control
- Commit notes regularly
- Use descriptive commit messages
- Tag important versions
- Create branches for experiments

### Integration with Obsidian
If using Obsidian:
1. Processed markdown files work seamlessly
2. SVG images display inline
3. UUIDs enable reliable linking
4. Tags integrate with Obsidian tags

## 🚀 Advanced Usage

### Workflow Customization
Edit `.github/workflows/remarkable-processor.yml` to:
- Change processing logic
- Add OCR integration
- Enable PNG conversion
- Custom frontmatter fields

### UUID Namespacing
UUIDs use the filename as input to `uuid5()`:
- Consistent across runs
- Reproducible identifiers
- Based on DNS namespace

### API Integration
Future possibilities:
- Direct sync with reMarkable cloud
- Automatic backup scheduling
- OCR with handwriting recognition
- Export to multiple formats

## 📚 Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [reMarkable Export Guide](https://remarkablewiki.com/)
- [YAML Frontmatter Spec](https://jekyllrb.com/docs/front-matter/)
- [UUID RFC 4122](https://tools.ietf.org/html/rfc4122)

---

**Need Help?** Check the [main README](./README.md) or review workflow logs in the Actions tab.
