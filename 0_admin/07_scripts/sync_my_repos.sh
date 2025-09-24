#!/bin/bash

# Script to sync GitHub user repos to JSON and Markdown files.
# Idempotent: Overwrites files with timestamp if changed.
# For cron: Run daily, logs to file.

set -e  # Exit on error

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
DATA_DIR="${PROJECT_ROOT}/3_projects/github"
mkdir -p "$DATA_DIR"

JSON_FILE="${DATA_DIR}/my_repos.json"
MD_FILE="${DATA_DIR}/my_repos.md"
LOG_FILE="${DATA_DIR}/sync_my_repos.log"
TIMESTAMP_FILE="${DATA_DIR}/last_my_repos_sync.txt"

# Log function
log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" | tee -a "$LOG_FILE"
}

log "Starting sync of my repositories."

# Fetch user repos (paginated to get ALL results)
if ! gh api user/repos --paginate > "${DATA_DIR}/temp_my_repos.json"; then
    log "Error: Failed to fetch user repos. Ensure 'gh' is authenticated."
    exit 1
fi

# Check if changed (simple: compare line count or use md5)
if [ -f "$JSON_FILE" ]; then
    OLD_COUNT=$(wc -l < "$JSON_FILE" 2>/dev/null || echo 0)
    NEW_COUNT=$(wc -l < "${DATA_DIR}/temp_my_repos.json" 2>/dev/null || echo 0)
    if [ "$OLD_COUNT" = "$NEW_COUNT" ]; then
        log "No changes detected. Skipping update."
        rm "${DATA_DIR}/temp_my_repos.json"
        echo "$(date '+%Y-%m-%d %H:%M:%S')" > "$TIMESTAMP_FILE"
        exit 0
    fi
fi

# Pretty-print JSON (requires jq; install if needed: brew install jq)
if command -v jq >/dev/null 2>&1; then
    jq . "${DATA_DIR}/temp_my_repos.json" > "$JSON_FILE"
else
    mv "${DATA_DIR}/temp_my_repos.json" "$JSON_FILE"
    log "Warning: jq not found. JSON not pretty-printed."
fi

# Generate Markdown summary
echo "# My GitHub Repositories (Last Sync: $(date))" > "$MD_FILE"
echo "" >> "$MD_FILE"
if command -v jq >/dev/null 2>&1; then
    # Sort by updated_at (most recent first) and format nicely
    jq -r 'sort_by(.updated_at) | reverse | .[] | "- **[\(.name)](\(.html_url))** (\(.stargazers_count) stars, \(.language // "No language")) - \(.description // "No description") - Updated: \(.updated_at | split("T")[0])"' "$JSON_FILE" >> "$MD_FILE"
    echo "" >> "$MD_FILE"
    # Add summary stats
    echo "## Repository Statistics" >> "$MD_FILE"
    echo "" >> "$MD_FILE"
    echo "- **Total repositories:** $(jq length "$JSON_FILE")" >> "$MD_FILE"
    echo "- **Total stars:** $(jq 'map(.stargazers_count) | add' "$JSON_FILE")" >> "$MD_FILE"
    echo "- **Total forks:** $(jq 'map(.forks_count) | add' "$JSON_FILE")" >> "$MD_FILE"
    echo "- **Most starred:** $(jq -r 'max_by(.stargazers_count) | "\(.name) (\(.stargazers_count) stars)"' "$JSON_FILE")" >> "$MD_FILE"
    echo "- **Languages used:** $(jq -r '[.[] | .language // "Unknown"] | unique | join(", ")' "$JSON_FILE")" >> "$MD_FILE"
else
    log "Warning: Cannot generate MD without jq. Install jq for full functionality."
    echo "Install jq to generate Markdown summary." >> "$MD_FILE"
fi

rm -f "${DATA_DIR}/temp_my_repos.json"

echo "$(date '+%Y-%m-%d %H:%M:%S')" > "$TIMESTAMP_FILE"

log "Sync completed. JSON: $JSON_FILE, MD: $MD_FILE"
