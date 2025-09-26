#!/usr/bin/env python3
"""
prometheus reward functions
inspired by maven-rl's comprehensive reward system
"""

import numpy as np
from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class TradingMetrics:
    """trading performance metrics"""
    total_return: float
    sharpe_ratio: float
    sortino_ratio: float
    max_drawdown: float
    win_rate: float
    profit_factor: float
    volatility: float
    calmar_ratio: float

class RewardCalculator:
    """advanced reward calculation system"""
    
    def __init__(self, risk_free_rate: float = 0.02):
        self.risk_free_rate = risk_free_rate
        self.portfolio_history = []
        self.returns_history = []
        
    def calculate_equity_delta_reward(self, 
                                    current_portfolio_value: float,
                                    previous_portfolio_value: float,
                                    transaction_cost: float = 0.001) -> float:
        """calculate reward based on portfolio value change"""
        if previous_portfolio_value == 0:
            return 0.0
            
        # raw return
        raw_return = (current_portfolio_value - previous_portfolio_value) / previous_portfolio_value
        
        # subtract transaction costs
        net_return = raw_return - transaction_cost
        
        # scale reward (log scale for better learning)
        reward = np.log(1 + net_return) if net_return > -0.99 else -10.0
        
        return reward
    
    def calculate_risk_adjusted_reward(self, 
                                     returns: List[float],
                                     lookback_period: int = 30) -> float:
        """calculate risk-adjusted reward using sharpe ratio"""
        if len(returns) < 2:
            return 0.0
            
        recent_returns = returns[-lookback_period:]
        mean_return = np.mean(recent_returns)
        std_return = np.std(recent_returns)
        
        if std_return == 0:
            return 0.0
            
        sharpe_ratio = (mean_return - self.risk_free_rate/252) / std_return
        
        # convert sharpe to reward (positive = good, negative = bad)
        reward = np.tanh(sharpe_ratio)  # bound between -1 and 1
        
        return reward
    
    def calculate_drawdown_penalty(self, 
                                 portfolio_values: List[float],
                                 max_drawdown_threshold: float = 0.1) -> float:
        """penalize large drawdowns"""
        if len(portfolio_values) < 2:
            return 0.0
            
        # calculate running maximum
        running_max = np.maximum.accumulate(portfolio_values)
        
        # calculate drawdown
        drawdown = (portfolio_values - running_max) / running_max
        
        # get maximum drawdown
        max_dd = np.min(drawdown)
        
        # penalty if drawdown exceeds threshold
        if max_dd < -max_drawdown_threshold:
            penalty = max_dd * 10  # amplify penalty
        else:
            penalty = 0.0
            
        return penalty
    
    def calculate_consistency_reward(self, 
                                   returns: List[float],
                                   target_consistency: float = 0.6) -> float:
        """reward consistent positive returns"""
        if len(returns) < 5:
            return 0.0
            
        # calculate win rate
        positive_returns = [r for r in returns if r > 0]
        win_rate = len(positive_returns) / len(returns)
        
        # reward consistency
        consistency_reward = (win_rate - target_consistency) * 2
        
        return np.clip(consistency_reward, -1, 1)
    
    def calculate_volatility_penalty(self, 
                                   returns: List[float],
                                   target_volatility: float = 0.02) -> float:
        """penalize excessive volatility"""
        if len(returns) < 2:
            return 0.0
            
        volatility = np.std(returns)
        
        # penalty for excessive volatility
        if volatility > target_volatility:
            penalty = -(volatility - target_volatility) * 5
        else:
            penalty = 0.0
            
        return penalty
    
    def calculate_comprehensive_reward(self,
                                     current_portfolio_value: float,
                                     previous_portfolio_value: float,
                                     returns: List[float],
                                     portfolio_values: List[float],
                                     weights: Optional[Dict[str, float]] = None) -> Dict[str, float]:
        """calculate comprehensive reward with multiple components"""
        
        if weights is None:
            weights = {
                'equity_delta': 0.4,
                'risk_adjusted': 0.3,
                'drawdown_penalty': 0.2,
                'consistency': 0.1
            }
        
        # calculate individual components
        equity_reward = self.calculate_equity_delta_reward(
            current_portfolio_value, previous_portfolio_value
        )
        
        risk_reward = self.calculate_risk_adjusted_reward(returns)
        
        drawdown_penalty = self.calculate_drawdown_penalty(portfolio_values)
        
        consistency_reward = self.calculate_consistency_reward(returns)
        
        # calculate weighted total reward
        total_reward = (
            weights['equity_delta'] * equity_reward +
            weights['risk_adjusted'] * risk_reward +
            weights['drawdown_penalty'] * drawdown_penalty +
            weights['consistency'] * consistency_reward
        )
        
        return {
            'total_reward': total_reward,
            'equity_delta': equity_reward,
            'risk_adjusted': risk_reward,
            'drawdown_penalty': drawdown_penalty,
            'consistency': consistency_reward
        }
    
    def calculate_metrics(self, returns: List[float]) -> TradingMetrics:
        """calculate comprehensive trading metrics"""
        if len(returns) < 2:
            return TradingMetrics(0, 0, 0, 0, 0, 0, 0, 0)
        
        returns_array = np.array(returns)
        
        # basic metrics
        total_return = np.sum(returns_array)
        volatility = np.std(returns_array)
        
        # risk-adjusted metrics
        sharpe_ratio = (np.mean(returns_array) - self.risk_free_rate/252) / volatility if volatility > 0 else 0
        
        # sortino ratio (downside deviation)
        downside_returns = returns_array[returns_array < 0]
        downside_std = np.std(downside_returns) if len(downside_returns) > 0 else 0
        sortino_ratio = (np.mean(returns_array) - self.risk_free_rate/252) / downside_std if downside_std > 0 else 0
        
        # drawdown
        cumulative_returns = np.cumprod(1 + returns_array)
        running_max = np.maximum.accumulate(cumulative_returns)
        drawdown = (cumulative_returns - running_max) / running_max
        max_drawdown = np.min(drawdown)
        
        # win rate
        win_rate = np.mean(returns_array > 0)
        
        # profit factor
        gross_profit = np.sum(returns_array[returns_array > 0])
        gross_loss = abs(np.sum(returns_array[returns_array < 0]))
        profit_factor = gross_profit / gross_loss if gross_loss > 0 else float('inf')
        
        # calmar ratio
        calmar_ratio = total_return / abs(max_drawdown) if max_drawdown != 0 else 0
        
        return TradingMetrics(
            total_return=total_return,
            sharpe_ratio=sharpe_ratio,
            sortino_ratio=sortino_ratio,
            max_drawdown=max_drawdown,
            win_rate=win_rate,
            profit_factor=profit_factor,
            volatility=volatility,
            calmar_ratio=calmar_ratio
        )

# example usage
if __name__ == "__main__":
    # test reward calculator
    calculator = RewardCalculator()
    
    # simulate some returns
    returns = [0.01, -0.005, 0.02, -0.01, 0.015, 0.008, -0.003, 0.012]
    portfolio_values = [1000, 1010, 1005, 1025, 1015, 1030, 1038, 1035, 1047]
    
    # calculate comprehensive reward
    reward_components = calculator.calculate_comprehensive_reward(
        current_portfolio_value=1047,
        previous_portfolio_value=1035,
        returns=returns,
        portfolio_values=portfolio_values
    )
    
    print("reward components:", reward_components)
    
    # calculate metrics
    metrics = calculator.calculate_metrics(returns)
    print("trading metrics:", metrics)
