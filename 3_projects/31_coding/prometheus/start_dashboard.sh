#!/bin/bash
# start prometheus dashboard locally for testing

echo "🚀 starting prometheus dashboard..."

# activate virtual environment
source venv/bin/activate

# start dashboard server
python dashboard_server.py
