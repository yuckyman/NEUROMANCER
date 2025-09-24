#!/bin/bash

# Script to sync GitHub starred repos to JSON and Markdown files.
# Idempotent: Overwrites files with timestamp if changed.
# For cron: Run daily, logs to file.

set -e  # Exit on error

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
DATA_DIR="${PROJECT_ROOT}/3_projects/github"
mkdir -p "$DATA_DIR"

JSON_FILE="${DATA_DIR}/starred_repos.json"
MD_FILE="${DATA_DIR}/starred_repos.md"
LOG_FILE="${DATA_DIR}/sync.log"
TIMESTAMP_FILE="${DATA_DIR}/last_sync.txt"

# Log function
log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" | tee -a "$LOG_FILE"
}

log "Starting sync of starred repos."

# Fetch starred repos (paginated to get ALL results)
if ! gh api user/starred --paginate > "${DATA_DIR}/temp.json"; then
    log "Error: Failed to fetch starred repos. Ensure 'gh' is authenticated."
    exit 1
fi

# Check if changed (simple: compare line count or use md5)
if [ -f "$JSON_FILE" ]; then
    OLD_COUNT=$(wc -l < "$JSON_FILE" 2>/dev/null || echo 0)
    NEW_COUNT=$(wc -l < "${DATA_DIR}/temp.json" 2>/dev/null || echo 0)
    if [ "$OLD_COUNT" = "$NEW_COUNT" ]; then
        log "No changes detected. Skipping update."
        rm "${DATA_DIR}/temp.json"
        echo "$(date '+%Y-%m-%d %H:%M:%S')" > "$TIMESTAMP_FILE"
        exit 0
    fi
fi

# Pretty-print JSON (requires jq; install if needed: brew install jq)
if command -v jq >/dev/null 2>&1; then
    jq . "${DATA_DIR}/temp.json" > "$JSON_FILE"
else
    mv "${DATA_DIR}/temp.json" "$JSON_FILE"
    log "Warning: jq not found. JSON not pretty-printed."
fi

# Generate Markdown summary
echo "# GitHub Starred Repos (Last Sync: $(date))" > "$MD_FILE"
echo "" >> "$MD_FILE"
if command -v jq >/dev/null 2>&1; then
    jq -r '.[] | "- **[\(.full_name)](\(.html_url))** (\(.stargazers_count) stars) - \(.description)"' "$JSON_FILE" >> "$MD_FILE"
else
    log "Warning: Cannot generate MD without jq. Install jq for full functionality."
    echo "Install jq to generate Markdown summary." >> "$MD_FILE"
fi
echo "" >> "$MD_FILE"
echo "Total: $(jq length "$JSON_FILE" 2>/dev/null || wc -l < "$JSON_FILE") repos" >> "$MD_FILE"

rm -f "${DATA_DIR}/temp.json"

echo "$(date '+%Y-%m-%d %H:%M:%S')" > "$TIMESTAMP_FILE"

log "Sync completed. JSON: $JSON_FILE, MD: $MD_FILE"
