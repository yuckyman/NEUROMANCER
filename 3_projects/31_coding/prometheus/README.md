# prometheus: autonomous market intelligence agent

*phase 0: free simulation mode for rl training*

## overview

prometheus is an autonomous ai agent that learns to predict financial markets through reinforcement learning. currently in phase 0 (free simulation), it tracks market data, makes predictions, and calculates rewards without spending real money.

## quick start

### 1. install dependencies
```bash
cd /Users/ian/NEUROMANCER/3_projects/31_coding/prometheus/
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

## deployment to yuckbox

### deploy to linux server
```bash
./deploy_to_yuckbox.sh
```

### monitor from neuromancer
```bash
python yuckbox_monitoring.py
```

## file structure

```
prometheus/
├── prometheus_monitoring_system.py  # main monitoring engine
├── prometheus_config.py            # configuration
├── run_prometheus.py               # launcher script
├── requirements_prometheus.txt     # dependencies
├── deploy_to_yuckbox.sh           # deployment script
├── yuckbox_monitoring.py          # monitoring dashboard
├── yuckbox_setup_guide.md         # deployment guide
├── prometheus_human_todo_checklist.md  # human setup tasks
├── prometheus_micro_capital_strategy.md # phase 1 strategy
└── README_prometheus.md           # detailed documentation
```

## phases

### phase 0: free simulation (current)
- tracks market data for SPY, QQQ, BTC, ETH
- makes predictions every 30 minutes
- calculates rewards for rl training
- **cost**: $0 (just api calls)

### phase 1: micro-capital deployment
- adds solana wallet integration
- implements real trading with $1-5 positions
- adds twitter bot for social proof
- **budget**: $100-200

### phase 2: rl training
- implements actual reinforcement learning
- fine-tunes predictions based on rewards
- optimizes for survival + profit

## key features

- **local inference**: no external api costs for decisions
- **transparent process**: every decision logged and analyzable
- **real market data**: not backtested historical data
- **continuous learning**: improves with every prediction
- **lightweight**: 30MB memory, 25MB disk after 3 months

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
