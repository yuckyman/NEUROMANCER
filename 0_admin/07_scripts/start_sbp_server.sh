#!/bin/bash

# SBP Server Startup Script
# Starts the SBP MCP server for NEUROMANCER knowledge amplification

cd /Users/ian/NEUROMANCER/3_projects/30_repos/sbp-mcp-server

# Activate virtual environment
source venv/bin/activate

# Start the server
uvicorn app:app --reload --host 0.0.0.0 --port 8001



