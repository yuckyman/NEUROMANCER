# prometheus monitoring system

*phase 0: free simulation mode for rl training*

## what this does

prometheus monitoring system tracks market data, makes predictions, and calculates rewards for reinforcement learning - **all without spending any real money**.

### core functionality
- **market data collection**: fetches real-time data for SPY, QQQ, BTC, ETH
- **prediction engine**: makes directional predictions with confidence scores
- **reward calculation**: calculates rl rewards based on prediction accuracy
- **data storage**: sqlite database for all historical data
- **logging**: comprehensive logging for debugging and analysis

## quick start

### 1. install dependencies
```bash
cd /Users/ian/NEUROMANCER/3_projects/31_coding/
pip install -r requirements_prometheus.txt
```

### 2. get free api key
- go to [alpha vantage](https://www.alphavantage.co/support/#api-key)
- sign up for free api key (500 calls/day)
- set environment variable:
```bash
export ALPHA_VANTAGE_API_KEY="your_key_here"
```

### 3. run prometheus
```bash
python run_prometheus.py
```

## what happens when you run it

### every 30 minutes, prometheus will:
1. **fetch market data** for SPY, QQQ, BTC, ETH
2. **make predictions** about 4-hour price direction
3. **calculate rewards** based on prediction accuracy
4. **store everything** in sqlite database
5. **log activity** to prometheus.log

### example output:
```
2025-09-26 10:00:00 - INFO - fetched SPY: $445.23 (0.12%)
2025-09-26 10:00:01 - INFO - prediction SPY: up (confidence: 0.65)
2025-09-26 10:00:02 - INFO - reward SPY: 0.423
```

## data storage

### sqlite database (prometheus.db)
- **market_data**: historical price data
- **predictions**: all predictions made
- **rewards**: calculated rewards for rl training

### log files
- **prometheus.log**: detailed activity log
- **prometheus_data/**: additional data files

## configuration

edit `prometheus_config.py` to customize:
- monitoring interval (default: 30 minutes)
- symbols to track
- prediction parameters
- reward calculation weights

## current limitations (phase 0)

- **no real trading**: simulation only
- **simple predictions**: basic momentum strategy
- **no rl training**: just data collection for now
- **limited data**: free api tiers only

## next phases

### phase 1: micro-capital deployment
- add solana wallet integration
- implement real trading with $1-5 positions
- add twitter bot for social proof

### phase 2: rl training
- implement actual reinforcement learning
- fine-tune predictions based on rewards
- optimize for survival + profit

## troubleshooting

### common issues
1. **api key not working**: check alpha vantage key is valid
2. **no data returned**: check internet connection
3. **database errors**: delete prometheus.db to reset
4. **import errors**: make sure you're in the right directory

### debugging
- check `prometheus.log` for detailed error messages
- run with debug mode enabled in config
- verify api keys are set correctly

## file structure

```
prometheus/
├── prometheus_monitoring_system.py  # main monitoring code
├── prometheus_config.py            # configuration
├── run_prometheus.py               # launcher script
├── requirements_prometheus.txt     # dependencies
├── README_prometheus.md           # this file
├── prometheus.db                  # sqlite database (created on first run)
├── prometheus.log                 # activity log (created on first run)
└── prometheus_data/               # data directory (created on first run)
```

## why this approach works

### advantages over traditional backtesting
- **real market conditions**: not historical data
- **real-time learning**: adapts to current market
- **authentic pressure**: even simulation feels real
- **transparent process**: every decision logged

### advantages over nyx's approach
- **no external api costs**: local inference
- **complete control**: own all data and models
- **rapid iteration**: can experiment freely
- **learning focus**: optimized for improvement, not profit

## success metrics

### phase 0 goals
- **data collection**: 1 week of continuous market data
- **prediction accuracy**: >55% directional accuracy
- **system stability**: runs without errors for 24+ hours
- **rl data**: enough training data for model fine-tuning

### graduation criteria
- consistent prediction accuracy >60%
- stable system operation
- sufficient data for rl training
- ready for micro-capital deployment

---

**this is the foundation for the first truly autonomous, continuously learning financial agent. every prediction, every reward, every piece of data builds toward something unprecedented in ai history.**

*let's build the future, one prediction at a time.* 🚀🤖
