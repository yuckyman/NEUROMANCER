#!/bin/bash
# Setup script for NEUROMANCER Social Media Monitor

echo "🧠 Setting up NEUROMANCER Social Media Monitor..."

# Check if Python dependencies are installed
echo "📦 Checking Python dependencies..."
python3 -c "import requests, feedparser, ollama, yaml" 2>/dev/null || {
    echo "Installing required Python packages..."
    pip3 install requests feedparser ollama pyyaml
}

# Create Discord webhook configuration
echo "🔗 Discord webhook setup..."
if [ -z "$DISCORD_WEBHOOK_URL" ]; then
    echo "⚠️  DISCORD_WEBHOOK_URL environment variable not set"
    echo "Please set it with: export DISCORD_WEBHOOK_URL='your_webhook_url_here'"
    echo "You can get a webhook URL from your Discord server settings"
else
    echo "✅ Discord webhook URL found"
fi

# Make scripts executable
chmod +x /Users/ian/NEUROMANCER/0_admin/07_scripts/social_monitor.py

# Create cron job for social monitoring
echo "⏰ Setting up cron job..."
CRON_JOB="*/10 * * * * /usr/bin/python3 /Users/ian/NEUROMANCER/0_admin/07_scripts/social_monitor.py >> /Users/ian/NEUROMANCER/0_admin/07_scripts/social_monitor.log 2>&1"

# Check if cron job already exists
if ! crontab -l 2>/dev/null | grep -q "social_monitor.py"; then
    (crontab -l 2>/dev/null; echo "$CRON_JOB") | crontab -
    echo "✅ Cron job added: runs every 10 minutes"
else
    echo "ℹ️  Cron job already exists"
fi

# Test the monitor
echo "🧪 Testing social monitor..."
python3 /Users/ian/NEUROMANCER/0_admin/07_scripts/social_monitor.py

echo "🎉 NEUROMANCER Social Media Monitor setup complete!"
echo ""
echo "Next steps:"
echo "1. Set DISCORD_WEBHOOK_URL environment variable"
echo "2. Customize social_monitor_config.yaml for your preferences"
echo "3. Monitor will run every 10 minutes via cron"
echo "4. Check logs at: /Users/ian/NEUROMANCER/0_admin/07_scripts/social_monitor.log"

