#!/bin/bash

# SBP Daemon Startup Script
# Ensures the SBP FastAPI server is running for MCP integration

SBP_DIR="/Users/ian/NEUROMANCER/3_projects/30_repos/sbp-mcp-server"
PID_FILE="/tmp/sbp_server.pid"
LOG_FILE="/tmp/sbp_server.log"

# Function to check if server is running
check_server() {
    # Check if port 8001 is in use
    if lsof -Pi :8001 -sTCP:LISTEN -t >/dev/null 2>&1; then
        return 0  # Server is running
    fi
    
    # Also check PID file
    if [ -f "$PID_FILE" ]; then
        PID=$(cat "$PID_FILE")
        if ps -p "$PID" > /dev/null 2>&1; then
            return 0  # Server is running
        else
            rm -f "$PID_FILE"  # Clean up stale PID file
        fi
    fi
    return 1  # Server is not running
}

# Function to start server
start_server() {
    echo "Starting SBP server..."
    cd "$SBP_DIR"
    source venv/bin/activate
    
    # Start server in background and save PID
    nohup uvicorn app:app --host 0.0.0.0 --port 8001 > "$LOG_FILE" 2>&1 &
    echo $! > "$PID_FILE"
    
    # Wait a moment and check if it started successfully
    sleep 2
    if check_server; then
        echo "SBP server started successfully (PID: $(cat $PID_FILE))"
        return 0
    else
        echo "Failed to start SBP server"
        return 1
    fi
}

# Main logic
if check_server; then
    # Get the actual PID of the process using port 8001
    ACTUAL_PID=$(lsof -Pi :8001 -sTCP:LISTEN -t 2>/dev/null | head -1)
    if [ -n "$ACTUAL_PID" ]; then
        echo "SBP server is already running (PID: $ACTUAL_PID)"
        echo "$ACTUAL_PID" > "$PID_FILE"  # Update PID file
    else
        echo "SBP server is already running"
    fi
else
    start_server
fi
