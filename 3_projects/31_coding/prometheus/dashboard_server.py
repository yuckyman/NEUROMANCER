#!/usr/bin/env python3
"""
prometheus dashboard server
serves a static html page with real-time market data visualization
"""

import os
import sqlite3
import json
import time
from datetime import datetime, timedelta
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
import threading

class DashboardHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.serve_dashboard()
        elif self.path == '/api/data':
            self.serve_api_data()
        else:
            self.send_error(404)

    def serve_dashboard(self):
        """serve the main dashboard html"""
        html_content = self.generate_dashboard_html()
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html_content.encode())

    def serve_api_data(self):
        """serve market data as json"""
        try:
            data = self.get_market_data()
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())
        except Exception as e:
            self.send_error(500, str(e))

    def get_market_data(self):
        """get latest market data from database"""
        conn = sqlite3.connect('prometheus.db')
        cursor = conn.cursor()
        
        # get latest data for each symbol
        cursor.execute("""
            SELECT symbol, price, change_24h, timestamp 
            FROM market_data 
            WHERE timestamp > datetime('now', '-1 day')
            ORDER BY timestamp DESC
        """)
        
        data = {}
        for row in cursor.fetchall():
            symbol, price, change_24h, timestamp = row
            if symbol not in data:
                data[symbol] = {
                    'price': price,
                    'change_24h': change_24h,
                    'timestamp': timestamp,
                    'trend': 'up' if change_24h > 0 else 'down' if change_24h < 0 else 'sideways'
                }
        
        # get recent predictions
        cursor.execute("""
            SELECT symbol, direction, confidence, timestamp
            FROM predictions 
            WHERE timestamp > datetime('now', '-1 hour')
            ORDER BY timestamp DESC
        """)
        
        predictions = {}
        for row in cursor.fetchall():
            symbol, direction, confidence, timestamp = row
            if symbol not in predictions:
                predictions[symbol] = {
                    'direction': direction,
                    'confidence': confidence,
                    'timestamp': timestamp
                }
        
        conn.close()
        
        return {
            'market_data': data,
            'predictions': predictions,
            'last_updated': datetime.now().isoformat()
        }

    def generate_dashboard_html(self):
        """generate the dashboard html"""
        return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Prometheus Market Intelligence</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            min-height: 100vh;
        }
        .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
        .header { text-align: center; margin-bottom: 30px; }
        .header h1 { font-size: 2.5em; margin-bottom: 10px; }
        .header p { opacity: 0.8; font-size: 1.1em; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; }
        .card { 
            background: rgba(255,255,255,0.1); 
            backdrop-filter: blur(10px);
            border-radius: 15px; 
            padding: 20px; 
            border: 1px solid rgba(255,255,255,0.2);
        }
        .symbol { font-size: 1.5em; font-weight: bold; margin-bottom: 10px; }
        .price { font-size: 2em; margin-bottom: 5px; }
        .change { font-size: 1.2em; }
        .change.positive { color: #4ade80; }
        .change.negative { color: #f87171; }
        .change.neutral { color: #94a3b8; }
        .prediction { margin-top: 15px; padding-top: 15px; border-top: 1px solid rgba(255,255,255,0.2); }
        .confidence { font-size: 0.9em; opacity: 0.8; }
        .loading { text-align: center; padding: 20px; }
        .status { text-align: center; margin-top: 20px; opacity: 0.7; }
        .trend-indicator {
            display: inline-block;
            width: 0;
            height: 0;
            margin-left: 10px;
        }
        .trend-up { border-left: 5px solid transparent; border-right: 5px solid transparent; border-bottom: 10px solid #4ade80; }
        .trend-down { border-left: 5px solid transparent; border-right: 5px solid transparent; border-top: 10px solid #f87171; }
        .trend-sideways { width: 10px; height: 3px; background: #94a3b8; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🤖 Prometheus Market Intelligence</h1>
            <p>Autonomous AI Learning to Predict Markets</p>
        </div>
        
        <div id="loading" class="loading">
            <p>Loading market data...</p>
        </div>
        
        <div id="dashboard" class="grid" style="display: none;">
            <!-- Market data cards will be populated here -->
        </div>
        
        <div class="status">
            <p>Last updated: <span id="last-updated">-</span></p>
            <p>Phase 0: Free Simulation Mode | Dry Run Active</p>
        </div>
    </div>

    <script>
        async function loadData() {
            try {
                const response = await fetch('/api/data');
                const data = await response.json();
                updateDashboard(data);
            } catch (error) {
                console.error('Error loading data:', error);
                document.getElementById('loading').innerHTML = '<p>Error loading data. Retrying...</p>';
            }
        }

        function updateDashboard(data) {
            const dashboard = document.getElementById('dashboard');
            const loading = document.getElementById('loading');
            
            loading.style.display = 'none';
            dashboard.style.display = 'grid';
            
            let html = '';
            
            for (const [symbol, marketData] of Object.entries(data.market_data)) {
                const changeClass = marketData.change_24h > 0 ? 'positive' : 
                                  marketData.change_24h < 0 ? 'negative' : 'neutral';
                const trendClass = marketData.trend === 'up' ? 'trend-up' : 
                                 marketData.trend === 'down' ? 'trend-down' : 'trend-sideways';
                
                const prediction = data.predictions[symbol] || { direction: 'unknown', confidence: 0 };
                
                html += `
                    <div class="card">
                        <div class="symbol">${symbol}</div>
                        <div class="price">
                            $${marketData.price.toFixed(2)}
                            <span class="trend-indicator ${trendClass}"></span>
                        </div>
                        <div class="change ${changeClass}">
                            ${marketData.change_24h > 0 ? '+' : ''}${(marketData.change_24h * 100).toFixed(2)}%
                        </div>
                        <div class="prediction">
                            <strong>Prediction:</strong> ${prediction.direction}
                            <div class="confidence">Confidence: ${(prediction.confidence * 100).toFixed(1)}%</div>
                        </div>
                    </div>
                `;
            }
            
            dashboard.innerHTML = html;
            document.getElementById('last-updated').textContent = new Date(data.last_updated).toLocaleString();
        }

        // load data immediately and then every 30 seconds
        loadData();
        setInterval(loadData, 30000);
    </script>
</body>
</html>
        """

def run_dashboard(port=None):
    """run the dashboard server"""
    if port is None:
        port = int(os.getenv('DASHBOARD_PORT', '8080'))
    
    server = HTTPServer(('0.0.0.0', port), DashboardHandler)
    print(f"🚀 Prometheus Dashboard running on http://localhost:{port}")
    print("📊 Real-time market data visualization active")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Dashboard stopped")

if __name__ == "__main__":
    run_dashboard()
