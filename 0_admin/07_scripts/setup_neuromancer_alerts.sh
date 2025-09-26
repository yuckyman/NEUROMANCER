#!/bin/bash
# Complete setup for NEUROMANCER Social Intelligence System

echo "🧠 Setting up NEUROMANCER Social Intelligence System..."

# Check if we're in the right directory
if [ ! -f "NEUROMANCER.md" ]; then
    echo "❌ Please run this from the NEUROMANCER root directory"
    exit 1
fi

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip3 install requests feedparser ollama pyyaml

# Make scripts executable
chmod +x /Users/ian/NEUROMANCER/0_admin/07_scripts/social_monitor.py
chmod +x /Users/ian/NEUROMANCER/0_admin/07_scripts/neuromancer_learning_agent.py

# Check for Discord webhook
echo "🔗 Checking Discord webhook configuration..."
if [ -z "$DISCORD_WEBHOOK_URL" ]; then
    echo "⚠️  DISCORD_WEBHOOK_URL environment variable not set"
    echo ""
    echo "To set up Discord notifications:"
    echo "1. Go to your Discord server settings"
    echo "2. Navigate to Integrations > Webhooks"
    echo "3. Create a new webhook"
    echo "4. Copy the webhook URL"
    echo "5. Run: export DISCORD_WEBHOOK_URL='your_webhook_url_here'"
    echo "6. Add to your shell profile for persistence"
    echo ""
    echo "Continuing setup without Discord notifications..."
else
    echo "✅ Discord webhook URL found"
fi

# Create cron jobs
echo "⏰ Setting up cron jobs..."

# Social monitor (every 10 minutes)
CRON_SOCIAL="*/10 * * * * /usr/bin/python3 /Users/ian/NEUROMANCER/0_admin/07_scripts/social_monitor.py >> /Users/ian/NEUROMANCER/0_admin/07_scripts/social_monitor.log 2>&1"

# Learning agent (every 6 hours)
CRON_LEARNING="0 */6 * * * /usr/bin/python3 /Users/ian/NEUROMANCER/0_admin/07_scripts/neuromancer_learning_agent.py >> /Users/ian/NEUROMANCER/0_admin/07_scripts/neuromancer_learning.log 2>&1"

# Check if cron jobs already exist
if ! crontab -l 2>/dev/null | grep -q "social_monitor.py"; then
    (crontab -l 2>/dev/null; echo "$CRON_SOCIAL") | crontab -
    echo "✅ Social monitor cron job added: runs every 10 minutes"
else
    echo "ℹ️  Social monitor cron job already exists"
fi

if ! crontab -l 2>/dev/null | grep -q "neuromancer_learning_agent.py"; then
    (crontab -l 2>/dev/null; echo "$CRON_LEARNING") | crontab -
    echo "✅ Learning agent cron job added: runs every 6 hours"
else
    echo "ℹ️  Learning agent cron job already exists"
fi

# Test the system
echo "🧪 Testing NEUROMANCER intelligence system..."

# Test social monitor
echo "Testing social monitor..."
python3 /Users/ian/NEUROMANCER/0_admin/07_scripts/social_monitor.py

# Test learning agent
echo "Testing learning agent..."
python3 /Users/ian/NEUROMANCER/0_admin/07_scripts/neuromancer_learning_agent.py

echo ""
echo "🎉 NEUROMANCER Social Intelligence System setup complete!"
echo ""
echo "What NEUROMANCER will do:"
echo "• Monitor Hacker News, Reddit, and GitHub for relevant content"
echo "• Learn from your vault activity and preferences"
echo "• Send intelligent Discord alerts when it finds something interesting"
echo "• Adapt its relevance scoring based on your behavior"
echo "• Maintain unbiased, factual reporting"
echo ""
echo "Configuration files:"
echo "• Social monitor: /Users/ian/NEUROMANCER/0_admin/07_scripts/social_monitor_config.yaml"
echo "• Learning agent: /Users/ian/NEUROMANCER/0_admin/07_scripts/neuromancer_learning_config.yaml"
echo ""
echo "Logs:"
echo "• Social monitor: /Users/ian/NEUROMANCER/0_admin/07_scripts/social_monitor.log"
echo "• Learning agent: /Users/ian/NEUROMANCER/0_admin/07_scripts/neuromancer_learning.log"
echo ""
echo "To customize:"
echo "1. Edit the config files to adjust monitoring sources and thresholds"
echo "2. Set DISCORD_WEBHOOK_URL for notifications"
echo "3. Monitor logs to see what NEUROMANCER is learning"
echo ""
echo "🧠 NEUROMANCER is now your intelligent research assistant!"

