#!/bin/bash

if [ $# -eq 0 ]; then
    CHANGED_FILES=$(git diff --cached --name-only | head -5 | tr '\n' ' ')
    MESSAGE="Quick commit: $(date) - $CHANGED_FILES"
else
    MESSAGE="$1"
fi

git add .
git commit -m "$MESSAGE"