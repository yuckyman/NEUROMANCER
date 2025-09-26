#!/bin/bash
# Setup Discord webhook for NEUROMANCER alerts

echo "🔗 Setting up Discord webhook for NEUROMANCER..."

# Check if webhook URL is already set
if [ ! -z "$DISCORD_WEBHOOK_URL" ]; then
    echo "✅ DISCORD_WEBHOOK_URL is already set"
    echo "Current webhook: ${DISCORD_WEBHOOK_URL:0:20}..."
else
    echo "❌ DISCORD_WEBHOOK_URL not set"
    echo ""
    echo "To set up Discord notifications:"
    echo "1. Go to your Discord server settings"
    echo "2. Navigate to Integrations > Webhooks"
    echo "3. Create a new webhook"
    echo "4. Copy the webhook URL"
    echo "5. Run: export DISCORD_WEBHOOK_URL='your_webhook_url_here'"
    echo ""
    echo "To make it permanent, add to your shell profile:"
    echo "echo 'export DISCORD_WEBHOOK_URL=\"your_webhook_url_here\"' >> ~/.zshrc"
    echo "source ~/.zshrc"
fi

echo ""
echo "🧪 Testing webhook..."
if [ ! -z "$DISCORD_WEBHOOK_URL" ]; then
    # Test the webhook with a simple message
    curl -X POST "$DISCORD_WEBHOOK_URL" \
        -H "Content-Type: application/json" \
        -d '{
            "content": "🧠 NEUROMANCER webhook test - if you see this, the setup is working!",
            "embeds": [{
                "title": "NEUROMANCER Test Alert",
                "description": "This is a test message to verify the webhook is working correctly.",
                "color": 0x00ff00,
                "footer": {
                    "text": "NEUROMANCER • Test Message"
                }
            }]
        }'
    
    if [ $? -eq 0 ]; then
        echo "✅ Webhook test successful! Check your Discord channel."
    else
        echo "❌ Webhook test failed. Check your URL and try again."
    fi
else
    echo "⚠️  Cannot test webhook - DISCORD_WEBHOOK_URL not set"
fi

echo ""
echo "🎯 Once the webhook is set up, NEUROMANCER will send you alerts like:"
echo "   • High relevance items from Hacker News, Reddit, and GitHub"
echo "   • Casual, down-to-earth explanations of why they matter"
echo "   • Unbiased, factual reporting with source quality adjustments"
echo "   • Learning-based confidence scores that improve over time"

