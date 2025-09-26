#!/usr/bin/env python3
"""
enhanced prometheus dashboard with interactive charts
serves a dynamic html page with real-time market data visualization
"""

import os
import sqlite3
import json
import time
from datetime import datetime, timedelta
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
import threading

class EnhancedDashboardHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.serve_dashboard()
        elif self.path == '/api/data':
            self.serve_api_data()
        elif self.path == '/api/history':
            self.serve_history_data()
        else:
            self.send_error(404)

    def serve_dashboard(self):
        """serve the enhanced dashboard html"""
        html_content = self.generate_enhanced_dashboard_html()
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html_content.encode())

    def serve_api_data(self):
        """serve current market data as json"""
        try:
            data = self.get_market_data()
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())
        except Exception as e:
            self.send_error(500, str(e))

    def serve_history_data(self):
        """serve historical data for charts"""
        try:
            data = self.get_historical_data()
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
            SELECT symbol, price, change_24h, volume, timestamp 
            FROM market_data 
            WHERE timestamp > datetime('now', '-1 day')
            ORDER BY timestamp DESC
        """)
        
        data = {}
        for row in cursor.fetchall():
            symbol, price, change_24h, volume, timestamp = row
            if symbol not in data:
                data[symbol] = {
                    'price': price,
                    'change_24h': change_24h,
                    'volume': volume,
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

    def get_historical_data(self):
        """get historical data for charts"""
        conn = sqlite3.connect('prometheus.db')
        cursor = conn.cursor()
        
        # get last 24 hours of data for top symbols
        cursor.execute("""
            SELECT symbol, price, change_24h, volume, timestamp 
            FROM market_data 
            WHERE timestamp > datetime('now', '-24 hours')
            ORDER BY timestamp ASC
        """)
        
        # group by symbol
        data = {}
        for row in cursor.fetchall():
            symbol, price, change_24h, volume, timestamp = row
            if symbol not in data:
                data[symbol] = []
            data[symbol].append({
                'timestamp': timestamp,
                'price': price,
                'change_24h': change_24h,
                'volume': volume
            })
        
        conn.close()
        return data

    def generate_enhanced_dashboard_html(self):
        """generate the enhanced dashboard html with charts"""
        return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Prometheus Market Intelligence - Enhanced</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chartjs-adapter-date-fns/dist/chartjs-adapter-date-fns.bundle.min.js"></script>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            min-height: 100vh;
        }
        .container { max-width: 1400px; margin: 0 auto; padding: 20px; }
        .header { text-align: center; margin-bottom: 30px; }
        .header h1 { font-size: 2.5em; margin-bottom: 10px; }
        .header p { opacity: 0.8; font-size: 1.1em; }
        
        .dashboard-grid { 
            display: grid; 
            grid-template-columns: 1fr 1fr; 
            gap: 20px; 
            margin-bottom: 20px;
        }
        
        .chart-container {
            background: rgba(255,255,255,0.1);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            padding: 20px;
            border: 1px solid rgba(255,255,255,0.2);
            height: 400px;
        }
        
        .chart-title {
            font-size: 1.2em;
            font-weight: bold;
            margin-bottom: 15px;
            text-align: center;
        }
        
        .market-grid { 
            display: grid; 
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); 
            gap: 15px; 
        }
        
        .card { 
            background: rgba(255,255,255,0.1); 
            backdrop-filter: blur(10px);
            border-radius: 15px; 
            padding: 15px; 
            border: 1px solid rgba(255,255,255,0.2);
            transition: transform 0.2s;
        }
        .card:hover { transform: translateY(-2px); }
        
        .symbol { font-size: 1.2em; font-weight: bold; margin-bottom: 8px; }
        .price { font-size: 1.5em; margin-bottom: 5px; }
        .change { font-size: 1em; }
        .change.positive { color: #4ade80; }
        .change.negative { color: #f87171; }
        .change.neutral { color: #94a3b8; }
        
        .prediction { 
            margin-top: 10px; 
            padding-top: 10px; 
            border-top: 1px solid rgba(255,255,255,0.2); 
            font-size: 0.9em;
        }
        .confidence { font-size: 0.8em; opacity: 0.8; }
        
        .loading { text-align: center; padding: 20px; }
        .status { text-align: center; margin-top: 20px; opacity: 0.7; }
        
        .trend-indicator {
            display: inline-block;
            width: 0;
            height: 0;
            margin-left: 8px;
        }
        .trend-up { border-left: 4px solid transparent; border-right: 4px solid transparent; border-bottom: 8px solid #4ade80; }
        .trend-down { border-left: 4px solid transparent; border-right: 4px solid transparent; border-top: 8px solid #f87171; }
        .trend-sideways { width: 8px; height: 2px; background: #94a3b8; }
        
        .controls {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin-bottom: 20px;
        }
        
        .btn {
            background: rgba(255,255,255,0.2);
            border: 1px solid rgba(255,255,255,0.3);
            color: white;
            padding: 8px 16px;
            border-radius: 8px;
            cursor: pointer;
            transition: background 0.2s;
        }
        .btn:hover { background: rgba(255,255,255,0.3); }
        .btn.active { background: rgba(255,255,255,0.4); }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🤖 Prometheus Market Intelligence</h1>
            <p>Enhanced Dashboard with Interactive Charts</p>
        </div>
        
        <div class="controls">
            <button class="btn active" onclick="switchView('overview')">Overview</button>
            <button class="btn" onclick="switchView('charts')">Charts</button>
            <button class="btn" onclick="switchView('predictions')">Predictions</button>
        </div>
        
        <div id="loading" class="loading">
            <p>Loading market data...</p>
        </div>
        
        <div id="overview" class="view">
            <div class="dashboard-grid">
                <div class="chart-container">
                    <div class="chart-title">Price Trends (Last 24h)</div>
                    <canvas id="priceChart"></canvas>
                </div>
                <div class="chart-container">
                    <div class="chart-title">Volume Analysis</div>
                    <canvas id="volumeChart"></canvas>
                </div>
            </div>
            <div class="market-grid" id="market-cards">
                <!-- Market data cards will be populated here -->
            </div>
        </div>
        
        <div id="charts" class="view" style="display: none;">
            <div class="chart-container" style="height: 500px;">
                <div class="chart-title">Interactive Price Chart</div>
                <canvas id="interactiveChart"></canvas>
            </div>
        </div>
        
        <div id="predictions" class="view" style="display: none;">
            <div class="market-grid" id="prediction-cards">
                <!-- Prediction cards will be populated here -->
            </div>
        </div>
        
        <div class="status">
            <p>Last updated: <span id="last-updated">-</span></p>
            <p>Phase 0: Free Simulation Mode | Dry Run Active</p>
        </div>
    </div>

    <script>
        let charts = {};
        let currentView = 'overview';
        
        // chart configurations
        const chartConfigs = {
            price: {
                type: 'line',
                data: { labels: [], datasets: [] },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        x: { type: 'time', time: { unit: 'hour' } },
                        y: { beginAtZero: false }
                    },
                    plugins: {
                        legend: { labels: { color: 'white' } }
                    }
                }
            },
            volume: {
                type: 'bar',
                data: { labels: [], datasets: [] },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        x: { ticks: { color: 'white' } },
                        y: { beginAtZero: true, ticks: { color: 'white' } }
                    },
                    plugins: {
                        legend: { labels: { color: 'white' } }
                    }
                }
            },
            interactive: {
                type: 'line',
                data: { labels: [], datasets: [] },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    interaction: {
                        intersect: false,
                        mode: 'index'
                    },
                    scales: {
                        x: { type: 'time', time: { unit: 'hour' } },
                        y: { beginAtZero: false }
                    },
                    plugins: {
                        legend: { labels: { color: 'white' } },
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    return context.dataset.label + ': $' + context.parsed.y.toFixed(2);
                                }
                            }
                        }
                    }
                }
            }
        };
        
        function switchView(view) {
            // hide all views
            document.querySelectorAll('.view').forEach(v => v.style.display = 'none');
            document.querySelectorAll('.btn').forEach(b => b.classList.remove('active'));
            
            // show selected view
            document.getElementById(view).style.display = 'block';
            document.querySelector(`[onclick="switchView('${view}')"]`).classList.add('active');
            
            currentView = view;
            
            // resize charts if needed
            if (view === 'charts' && charts.interactive) {
                charts.interactive.resize();
            }
        }
        
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
        
        async function loadHistory() {
            try {
                const response = await fetch('/api/history');
                const data = await response.json();
                updateCharts(data);
            } catch (error) {
                console.error('Error loading history:', error);
            }
        }
        
        function updateDashboard(data) {
            const loading = document.getElementById('loading');
            const overview = document.getElementById('overview');
            
            loading.style.display = 'none';
            overview.style.display = 'block';
            
            updateMarketCards(data);
            document.getElementById('last-updated').textContent = new Date(data.last_updated).toLocaleString();
        }
        
        function updateMarketCards(data) {
            const container = document.getElementById('market-cards');
            let html = '';
            
            // sort by market cap/importance
            const priority = ['SPY', 'QQQ', 'BTC', 'ETH', 'TSLA', 'NVDA', 'AAPL', 'MSFT'];
            const sortedSymbols = Object.keys(data.market_data).sort((a, b) => {
                const aIndex = priority.indexOf(a);
                const bIndex = priority.indexOf(b);
                if (aIndex === -1 && bIndex === -1) return a.localeCompare(b);
                if (aIndex === -1) return 1;
                if (bIndex === -1) return -1;
                return aIndex - bIndex;
            });
            
            for (const symbol of sortedSymbols) {
                const marketData = data.market_data[symbol];
                const prediction = data.predictions[symbol] || { direction: 'unknown', confidence: 0 };
                
                const changeClass = marketData.change_24h > 0 ? 'positive' : 
                                  marketData.change_24h < 0 ? 'negative' : 'neutral';
                const trendClass = marketData.trend === 'up' ? 'trend-up' : 
                                 marketData.trend === 'down' ? 'trend-down' : 'trend-sideways';
                
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
            
            container.innerHTML = html;
        }
        
        function updateCharts(historyData) {
            // update price chart
            updatePriceChart(historyData);
            updateVolumeChart(historyData);
            updateInteractiveChart(historyData);
        }
        
        function updatePriceChart(data) {
            const ctx = document.getElementById('priceChart').getContext('2d');
            
            if (charts.price) {
                charts.price.destroy();
            }
            
            const datasets = [];
            const colors = ['#4ade80', '#f87171', '#60a5fa', '#fbbf24', '#a78bfa'];
            let colorIndex = 0;
            
            // show top 5 symbols by volume
            const sortedSymbols = Object.keys(data).sort((a, b) => {
                const aVol = data[a].reduce((sum, d) => sum + d.volume, 0);
                const bVol = data[b].reduce((sum, d) => sum + d.volume, 0);
                return bVol - aVol;
            }).slice(0, 5);
            
            for (const symbol of sortedSymbols) {
                const symbolData = data[symbol];
                if (symbolData.length > 0) {
                    datasets.push({
                        label: symbol,
                        data: symbolData.map(d => ({
                            x: new Date(d.timestamp),
                            y: d.price
                        })),
                        borderColor: colors[colorIndex % colors.length],
                        backgroundColor: colors[colorIndex % colors.length] + '20',
                        tension: 0.4,
                        fill: false
                    });
                    colorIndex++;
                }
            }
            
            charts.price = new Chart(ctx, {
                ...chartConfigs.price,
                data: { datasets }
            });
        }
        
        function updateVolumeChart(data) {
            const ctx = document.getElementById('volumeChart').getContext('2d');
            
            if (charts.volume) {
                charts.volume.destroy();
            }
            
            const labels = [];
            const volumes = [];
            
            // aggregate volume by hour
            const hourlyVolume = {};
            for (const symbol of Object.keys(data)) {
                for (const point of data[symbol]) {
                    const hour = new Date(point.timestamp).getHours();
                    if (!hourlyVolume[hour]) hourlyVolume[hour] = 0;
                    hourlyVolume[hour] += point.volume || 0;
                }
            }
            
            for (let hour = 0; hour < 24; hour++) {
                labels.push(`${hour}:00`);
                volumes.push(hourlyVolume[hour] || 0);
            }
            
            charts.volume = new Chart(ctx, {
                ...chartConfigs.volume,
                data: {
                    labels,
                    datasets: [{
                        label: 'Total Volume',
                        data: volumes,
                        backgroundColor: 'rgba(96, 165, 250, 0.6)',
                        borderColor: 'rgba(96, 165, 250, 1)',
                        borderWidth: 1
                    }]
                }
            });
        }
        
        function updateInteractiveChart(data) {
            const ctx = document.getElementById('interactiveChart').getContext('2d');
            
            if (charts.interactive) {
                charts.interactive.destroy();
            }
            
            const datasets = [];
            const colors = ['#4ade80', '#f87171', '#60a5fa', '#fbbf24', '#a78bfa', '#fb7185', '#34d399', '#fbbf24'];
            let colorIndex = 0;
            
            // show all symbols
            for (const symbol of Object.keys(data)) {
                const symbolData = data[symbol];
                if (symbolData.length > 0) {
                    datasets.push({
                        label: symbol,
                        data: symbolData.map(d => ({
                            x: new Date(d.timestamp),
                            y: d.price
                        })),
                        borderColor: colors[colorIndex % colors.length],
                        backgroundColor: colors[colorIndex % colors.length] + '20',
                        tension: 0.4,
                        fill: false,
                        pointRadius: 2,
                        pointHoverRadius: 5
                    });
                    colorIndex++;
                }
            }
            
            charts.interactive = new Chart(ctx, {
                ...chartConfigs.interactive,
                data: { datasets }
            });
        }
        
        // load data immediately and then every 30 seconds
        loadData();
        loadHistory();
        setInterval(() => {
            loadData();
            if (currentView === 'charts') {
                loadHistory();
            }
        }, 30000);
    </script>
</body>
</html>
        """

def run_enhanced_dashboard(port=None):
    """run the enhanced dashboard server"""
    if port is None:
        port = int(os.getenv('DASHBOARD_PORT', '8080'))
    
    server = HTTPServer(('0.0.0.0', port), EnhancedDashboardHandler)
    print(f"🚀 Enhanced Prometheus Dashboard running on http://localhost:{port}")
    print("📊 Interactive charts and real-time data visualization active")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Enhanced Dashboard stopped")

if __name__ == "__main__":
    run_enhanced_dashboard()
