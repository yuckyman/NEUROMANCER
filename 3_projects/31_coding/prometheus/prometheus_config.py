#!/usr/bin/env python3
"""
prometheus configuration file
set your api keys and parameters here
"""

import os
from pathlib import Path

# api keys (get these from the human todo checklist)
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY", "YOUR_ALPHA_VANTAGE_KEY_HERE")
COINGECKO_API_KEY = os.getenv("COINGECKO_API_KEY", None)  # optional, free tier works without key

# monitoring configuration
MONITORING_INTERVAL_MINUTES = 30  # how often to check markets
SYMBOLS_TO_TRACK = [
    "SPY", "QQQ", "BTC", "ETH",  # original set
    "TSLA", "NVDA", "AAPL", "MSFT",  # tech giants
    "GOOGL", "AMZN", "META", "NFLX",  # big tech
    "SOL", "ADA", "DOT", "MATIC",  # more crypto
    "VIX", "GLD", "SLV", "TLT"  # volatility & commodities
]  # what to monitor

# prediction configuration
PREDICTION_TIMEFRAME = "4h"  # how far ahead to predict
CONFIDENCE_THRESHOLD = 0.6  # minimum confidence to make prediction
MAX_POSITION_SIZE = 0.1  # max 10% allocation per trade

# reward calculation weights
ACCURACY_WEIGHT = 0.7  # how much to weight prediction accuracy
PORTFOLIO_WEIGHT = 0.3  # how much to weight simulated returns

# database configuration
DATABASE_PATH = "prometheus.db"
LOG_FILE = "prometheus.log"

# risk management
MAX_DAILY_PREDICTIONS = 10  # don't spam predictions
MIN_CONFIDENCE_FOR_ACTION = 0.5  # only act on high-confidence predictions

# social media (for later phases)
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY", None)
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET", None)
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN", None)
TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET", None)

# solana configuration (for later phases)
SOLANA_RPC_URL = "https://api.mainnet-beta.solana.com"
WALLET_PRIVATE_KEY = os.getenv("WALLET_PRIVATE_KEY", None)  # keep this secret!

# logging configuration
LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# development flags
DEBUG_MODE = True  # set to False in production
DRY_RUN = True  # set to False when ready for real trading
SIMULATION_MODE = True  # set to False when ready for live trading

# file paths
DATA_DIR = Path("prometheus_data")
LOGS_DIR = Path("prometheus_logs")
MODELS_DIR = Path("prometheus_models")

# create directories if they don't exist
DATA_DIR.mkdir(exist_ok=True)
LOGS_DIR.mkdir(exist_ok=True)
MODELS_DIR.mkdir(exist_ok=True)
