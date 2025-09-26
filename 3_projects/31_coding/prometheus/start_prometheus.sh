#!/bin/bash
# start prometheus with docker compose

echo "🚀 starting prometheus with docker compose..."

# check if .env file exists
if [ ! -f .env ]; then
    echo "⚠️  .env file not found. creating from example..."
    echo "WEB_PORT=7778" > .env
    echo "ALPHA_VANTAGE_API_KEY=your_key_here" >> .env
    echo "COINGECKO_API_KEY=" >> .env
    echo "DASHBOARD_PORT=8080" >> .env
    echo "📝 please edit .env file with your actual api keys"
fi

# build and start services
echo "🔨 building and starting services..."
docker compose up --build -d

echo "✅ prometheus is running!"
echo "📊 dashboard available at: http://localhost:7778"
echo "🔍 check logs with: docker compose logs -f"
echo "🛑 stop with: docker compose down"
