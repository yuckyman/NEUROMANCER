#!/usr/bin/env python3
"""
prometheus monitoring system - phase 0 (free simulation)
tracks market data, makes predictions, calculates rewards for rl training
"""

import asyncio
import json
import logging
import sqlite3
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import requests
import numpy as np
from dataclasses import dataclass
from pathlib import Path

# configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('prometheus.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

@dataclass
class MarketData:
    """market data point"""
    timestamp: datetime
    symbol: str
    price: float
    volume: float
    change_1h: float
    change_4h: float
    change_24h: float

@dataclass
class Prediction:
    """prometheus prediction"""
    timestamp: datetime
    symbol: str
    direction: str  # "up", "down", "sideways"
    confidence: float  # 0.0 - 1.0
    magnitude: float  # expected % change
    timeframe: str  # "1h", "4h", "1d"
    reasoning: str
    actual_outcome: Optional[Dict] = None

@dataclass
class Reward:
    """calculated reward for rl training"""
    prediction_id: int
    accuracy_reward: float
    portfolio_reward: float
    total_reward: float
    timestamp: datetime

class MarketDataFetcher:
    """fetches market data from free apis"""
    
    def __init__(self):
        self.alpha_vantage_key = "YOUR_ALPHA_VANTAGE_KEY"  # replace with actual key
        self.coingecko_base = "https://api.coingecko.com/api/v3"
        self.alpha_vantage_base = "https://www.alphavantage.co/query"
        
    async def fetch_stock_data(self, symbol: str) -> Optional[MarketData]:
        """fetch stock data from alpha vantage"""
        try:
            url = f"{self.alpha_vantage_base}"
            params = {
                "function": "TIME_SERIES_INTRADAY",
                "symbol": symbol,
                "interval": "60min",
                "apikey": self.alpha_vantage_key,
                "outputsize": "compact"
            }
            
            response = requests.get(url, params=params, timeout=10)
            data = response.json()
            
            if "Error Message" in data:
                logger.error(f"alpha vantage error for {symbol}: {data['Error Message']}")
                return None
                
            time_series = data.get("Time Series (60min)", {})
            if not time_series:
                logger.warning(f"no time series data for {symbol}")
                return None
                
            # get latest data point
            latest_time = max(time_series.keys())
            latest_data = time_series[latest_time]
            
            # calculate changes (simplified)
            current_price = float(latest_data["4. close"])
            
            # get previous data points for change calculation
            times = sorted(time_series.keys(), reverse=True)
            if len(times) < 25:  # need 24h of data
                logger.warning(f"insufficient data for {symbol}")
                return None
                
            price_1h_ago = float(time_series[times[1]]["4. close"])
            price_4h_ago = float(time_series[times[4]]["4. close"])
            price_24h_ago = float(time_series[times[24]]["4. close"])
            
            return MarketData(
                timestamp=datetime.now(),
                symbol=symbol,
                price=current_price,
                volume=float(latest_data["5. volume"]),
                change_1h=(current_price - price_1h_ago) / price_1h_ago,
                change_4h=(current_price - price_4h_ago) / price_4h_ago,
                change_24h=(current_price - price_24h_ago) / price_24h_ago
            )
            
        except Exception as e:
            logger.error(f"error fetching stock data for {symbol}: {e}")
            return None
    
    async def fetch_crypto_data(self, symbol: str) -> Optional[MarketData]:
        """fetch crypto data from coingecko"""
        try:
            # map symbols to coingecko ids
            symbol_map = {
                "BTC": "bitcoin",
                "ETH": "ethereum", 
                "SOL": "solana"
            }
            
            coin_id = symbol_map.get(symbol)
            if not coin_id:
                logger.error(f"unsupported crypto symbol: {symbol}")
                return None
                
            url = f"{self.coingecko_base}/simple/price"
            params = {
                "ids": coin_id,
                "vs_currencies": "usd",
                "include_24hr_change": "true",
                "include_1h_change": "true"
            }
            
            response = requests.get(url, params=params, timeout=10)
            data = response.json()
            
            if coin_id not in data:
                logger.error(f"coin not found: {coin_id}")
                return None
                
            coin_data = data[coin_id]
            
            return MarketData(
                timestamp=datetime.now(),
                symbol=symbol,
                price=coin_data["usd"],
                volume=0,  # coingecko free tier doesn't include volume
                change_1h=coin_data.get("usd_1h_change", 0) / 100,
                change_4h=0,  # not available in free tier
                change_24h=coin_data.get("usd_24h_change", 0) / 100
            )
            
        except Exception as e:
            logger.error(f"error fetching crypto data for {symbol}: {e}")
            return None

class PrometheusPredictor:
    """simple prediction engine (placeholder for rl model)"""
    
    def __init__(self):
        self.symbols = ["SPY", "QQQ", "BTC", "ETH"]
        self.prediction_history = []
        
    def make_prediction(self, market_data: MarketData) -> Prediction:
        """make a prediction based on market data"""
        
        # simple heuristic-based prediction (replace with rl model later)
        price_change_1h = market_data.change_1h
        price_change_24h = market_data.change_24h
        
        # basic momentum strategy
        if price_change_1h > 0.01:  # 1% up in last hour
            direction = "up"
            confidence = min(0.8, abs(price_change_1h) * 10)
        elif price_change_1h < -0.01:  # 1% down in last hour
            direction = "down" 
            confidence = min(0.8, abs(price_change_1h) * 10)
        else:
            direction = "sideways"
            confidence = 0.3
            
        # adjust confidence based on 24h trend
        if (direction == "up" and price_change_24h > 0) or (direction == "down" and price_change_24h < 0):
            confidence *= 1.2  # trend continuation
        else:
            confidence *= 0.8  # trend reversal
            
        confidence = min(1.0, max(0.1, confidence))
        
        # expected magnitude based on recent volatility
        magnitude = abs(price_change_1h) * 2  # expect 2x recent movement
        magnitude = min(0.1, max(0.001, magnitude))  # clamp between 0.1% and 10%
        
        # reasoning
        reasoning = f"1h change: {price_change_1h:.2%}, 24h change: {price_change_24h:.2%}, momentum: {direction}"
        
        prediction = Prediction(
            timestamp=datetime.now(),
            symbol=market_data.symbol,
            direction=direction,
            confidence=confidence,
            magnitude=magnitude,
            timeframe="4h",  # predict 4 hours ahead
            reasoning=reasoning
        )
        
        self.prediction_history.append(prediction)
        return prediction

class RewardCalculator:
    """calculates rewards for rl training"""
    
    def calculate_reward(self, prediction: Prediction, actual_outcome: MarketData) -> Reward:
        """calculate reward based on prediction accuracy"""
        
        # determine actual direction
        actual_change = actual_outcome.change_4h  # use 4h change to match prediction timeframe
        if actual_change > 0.005:  # 0.5% threshold
            actual_direction = "up"
        elif actual_change < -0.005:
            actual_direction = "down"
        else:
            actual_direction = "sideways"
            
        # accuracy reward
        direction_correct = (prediction.direction == actual_direction)
        if direction_correct:
            accuracy_reward = prediction.confidence
        else:
            accuracy_reward = -prediction.confidence
            
        # portfolio simulation reward
        position_size = prediction.confidence * 0.1  # max 10% allocation
        portfolio_return = position_size * actual_change
        portfolio_reward = portfolio_return * 100  # scale for visibility
        
        # total reward
        total_reward = 0.7 * accuracy_reward + 0.3 * portfolio_reward
        
        return Reward(
            prediction_id=len(prediction.prediction_history) if hasattr(prediction, 'prediction_history') else 0,
            accuracy_reward=accuracy_reward,
            portfolio_reward=portfolio_reward,
            total_reward=total_reward,
            timestamp=datetime.now()
        )

class DatabaseManager:
    """manages sqlite database for storing data"""
    
    def __init__(self, db_path: str = "prometheus.db"):
        self.db_path = db_path
        self.init_database()
        
    def init_database(self):
        """initialize database tables"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # market data table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS market_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                symbol TEXT,
                price REAL,
                volume REAL,
                change_1h REAL,
                change_4h REAL,
                change_24h REAL
            )
        """)
        
        # predictions table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS predictions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                symbol TEXT,
                direction TEXT,
                confidence REAL,
                magnitude REAL,
                timeframe TEXT,
                reasoning TEXT,
                actual_outcome TEXT
            )
        """)
        
        # rewards table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS rewards (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                prediction_id INTEGER,
                accuracy_reward REAL,
                portfolio_reward REAL,
                total_reward REAL,
                timestamp TEXT,
                FOREIGN KEY (prediction_id) REFERENCES predictions (id)
            )
        """)
        
        conn.commit()
        conn.close()
        
    def store_market_data(self, data: MarketData):
        """store market data"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO market_data (timestamp, symbol, price, volume, change_1h, change_4h, change_24h)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            data.timestamp.isoformat(),
            data.symbol,
            data.price,
            data.volume,
            data.change_1h,
            data.change_4h,
            data.change_24h
        ))
        
        conn.commit()
        conn.close()
        
    def store_prediction(self, prediction: Prediction):
        """store prediction"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO predictions (timestamp, symbol, direction, confidence, magnitude, timeframe, reasoning)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            prediction.timestamp.isoformat(),
            prediction.symbol,
            prediction.direction,
            prediction.confidence,
            prediction.magnitude,
            prediction.timeframe,
            prediction.reasoning
        ))
        
        conn.commit()
        conn.close()
        
    def store_reward(self, reward: Reward):
        """store reward"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO rewards (prediction_id, accuracy_reward, portfolio_reward, total_reward, timestamp)
            VALUES (?, ?, ?, ?, ?)
        """, (
            reward.prediction_id,
            reward.accuracy_reward,
            reward.portfolio_reward,
            reward.total_reward,
            reward.timestamp.isoformat()
        ))
        
        conn.commit()
        conn.close()

class PrometheusMonitor:
    """main monitoring system"""
    
    def __init__(self):
        self.data_fetcher = MarketDataFetcher()
        self.predictor = PrometheusPredictor()
        self.reward_calc = RewardCalculator()
        self.db = DatabaseManager()
        self.running = False
        
    async def run_cycle(self):
        """run one monitoring cycle"""
        logger.info("starting monitoring cycle")
        
        # fetch market data for all symbols
        market_data = {}
        for symbol in self.predictor.symbols:
            if symbol in ["SPY", "QQQ"]:
                data = await self.data_fetcher.fetch_stock_data(symbol)
            else:
                data = await self.data_fetcher.fetch_crypto_data(symbol)
                
            if data:
                market_data[symbol] = data
                self.db.store_market_data(data)
                logger.info(f"fetched {symbol}: ${data.price:.2f} ({data.change_1h:.2%})")
        
        # make predictions
        predictions = {}
        for symbol, data in market_data.items():
            prediction = self.predictor.make_prediction(data)
            predictions[symbol] = prediction
            self.db.store_prediction(prediction)
            logger.info(f"prediction {symbol}: {prediction.direction} (confidence: {prediction.confidence:.2f})")
        
        # calculate rewards for previous predictions (if we have enough data)
        if len(self.predictor.prediction_history) > 4:  # need some history
            # this is simplified - in real implementation, we'd wait for actual outcomes
            # for now, we'll use current market data as "outcome"
            for prediction in self.predictor.prediction_history[-4:]:  # last 4 predictions
                if prediction.symbol in market_data:
                    actual_outcome = market_data[prediction.symbol]
                    reward = self.reward_calc.calculate_reward(prediction, actual_outcome)
                    self.db.store_reward(reward)
                    logger.info(f"reward {prediction.symbol}: {reward.total_reward:.3f}")
        
        logger.info("monitoring cycle complete")
        
    async def run(self, interval_minutes: int = 30):
        """run monitoring system continuously"""
        self.running = True
        logger.info(f"starting prometheus monitoring (interval: {interval_minutes}min)")
        
        while self.running:
            try:
                await self.run_cycle()
                await asyncio.sleep(interval_minutes * 60)
            except KeyboardInterrupt:
                logger.info("shutting down prometheus monitoring")
                self.running = False
            except Exception as e:
                logger.error(f"error in monitoring cycle: {e}")
                await asyncio.sleep(60)  # wait 1 minute before retrying

def main():
    """main entry point"""
    monitor = PrometheusMonitor()
    
    # run for 24 hours as test
    async def test_run():
        for i in range(48):  # 48 cycles of 30 minutes = 24 hours
            await monitor.run_cycle()
            await asyncio.sleep(30 * 60)  # 30 minutes
    
    asyncio.run(test_run())

if __name__ == "__main__":
    main()
