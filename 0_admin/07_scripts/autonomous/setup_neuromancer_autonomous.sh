#!/bin/bash
# Setup script for NEUROMANCER Autonomous Intelligence System

echo "🧠 Setting up NEUROMANCER Autonomous Intelligence System..."

# Check if Python dependencies are installed
echo "📦 Checking Python dependencies..."
python3 -c "import asyncio, aiohttp, aiofiles, requests, feedparser, ollama, yaml, bs4" 2>/dev/null || {
    echo "Installing required Python packages..."
    pip3 install aiohttp aiofiles requests feedparser pyyaml beautifulsoup4
}

# Check if Ollama is available
echo "🤖 Checking Ollama models..."
python3 -c "
import ollama
try:
    models = ollama.list()
    model_names = [m['name'] for m in models['models']]
    required = ['qwen2.5:1.5b-instruct', 'qwen3:4b']
    for model in required:
        if not any(model in name for name in model_names):
            print(f'⚠️  Model {model} not found. Install with: ollama pull {model}')
except Exception as e:
    print(f'❌ Ollama not available: {e}')
"

# Create Discord webhook configuration
echo "🔗 Discord webhook setup..."
if [ -z "$DISCORD_WEBHOOK_URL" ]; then
    echo "⚠️  DISCORD_WEBHOOK_URL environment variable not set"
    echo "Please set it with: export DISCORD_WEBHOOK_URL='your_webhook_url_here'"
    echo "You can get a webhook URL from your Discord server settings"
else
    echo "✅ Discord webhook URL found"
fi

# Make scripts executable (Linux server paths)
chmod +x /home/ian/NEUROMANCER/0_admin/07_scripts/autonomous/neuromancer_autonomous.py

# Create cron job for autonomous monitoring (Linux server paths)
echo "⏰ Setting up cron job..."
CRON_JOB="*/30 * * * * /usr/bin/python3 /home/ian/NEUROMANCER/0_admin/07_scripts/autonomous/neuromancer_autonomous.py >> /home/ian/NEUROMANCER/0_admin/07_scripts/neuromancer_autonomous.log 2>&1"

# Check if cron job already exists
if ! crontab -l 2>/dev/null | grep -q "neuromancer_autonomous.py"; then
    (crontab -l 2>/dev/null; echo "$CRON_JOB") | crontab -
    echo "✅ Cron job added: runs every 30 minutes"
else
    echo "ℹ️  Cron job already exists"
fi

# Test the autonomous system (Linux server paths)
echo "🧪 Testing autonomous system..."
timeout 30 python3 /home/ian/NEUROMANCER/0_admin/07_scripts/autonomous/neuromancer_autonomous.py &
TEST_PID=$!

# Wait a moment for startup
sleep 5

# Check if process is still running
if kill -0 $TEST_PID 2>/dev/null; then
    echo "✅ Autonomous system started successfully"
    kill $TEST_PID 2>/dev/null
else
    echo "⚠️  Autonomous system may need manual testing"
fi

echo ""
echo "🎉 NEUROMANCER Autonomous Intelligence System setup complete!"
echo ""
echo "System Features:"
echo "• Semi-stochastic scheduling with learning-based timing"
echo "• Multi-source intelligence synthesis"
echo "• Autonomous RSS feed discovery"
echo "• Casual, friendly Discord messaging (like a buddy sharing cool finds!)"
echo "• Rich embeds with personality and personal commentary"
echo "• Local knowledge base integration"
echo "• Self-healing error recovery"
echo ""
echo "Next steps:"
echo "1. Set DISCORD_WEBHOOK_URL environment variable"
echo "2. Customize neuromancer_autonomous_config.yaml for your preferences"
echo "3. System will run every 30 minutes via cron"
echo "4. Check logs at: /home/ian/NEUROMANCER/0_admin/07_scripts/neuromancer_autonomous.log"
echo "5. Monitor synthesis files in: /home/ian/NEUROMANCER/1_ideas/"
echo ""
echo "Configuration files:"
echo "• Config: 0_admin/07_scripts/autonomous/neuromancer_autonomous_config.yaml"
echo "• RSS feeds: 0_admin/07_scripts/rss_feeds.json"
echo "• State: 0_admin/07_scripts/autonomous/autonomous_state.json"
echo ""
echo "🧠 NEUROMANCER is now autonomous!"
