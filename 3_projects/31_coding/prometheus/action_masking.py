#!/usr/bin/env python3
"""
prometheus action masking system
prevents invalid trading actions inspired by maven-rl
"""

import numpy as np
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum

class ActionType(Enum):
    """trading action types"""
    HOLD = 0
    BUY = 1
    SELL = 2

@dataclass
class Position:
    """position information"""
    symbol: str
    quantity: float
    avg_price: float
    current_price: float
    unrealized_pnl: float

@dataclass
class AccountState:
    """account state for action validation"""
    cash: float
    total_value: float
    positions: Dict[str, Position]
    max_position_size: float = 0.1  # 10% max per position
    min_trade_size: float = 10.0    # minimum trade size

class ActionMasker:
    """action masking system to prevent invalid trades"""
    
    def __init__(self, account_state: AccountState):
        self.account_state = account_state
        
    def get_valid_actions(self, 
                         symbol: str, 
                         current_price: float,
                         market_hours: bool = True) -> List[ActionType]:
        """get valid actions for a given symbol"""
        valid_actions = [ActionType.HOLD]  # always valid
        
        if not market_hours:
            return valid_actions
            
        # check if we can buy
        if self._can_buy(symbol, current_price):
            valid_actions.append(ActionType.BUY)
            
        # check if we can sell
        if self._can_sell(symbol):
            valid_actions.append(ActionType.SELL)
            
        return valid_actions
    
    def _can_buy(self, symbol: str, current_price: float) -> bool:
        """check if we can buy the symbol"""
        # check if we have enough cash
        min_cost = current_price * (self.account_state.min_trade_size / current_price)
        if self.account_state.cash < min_cost:
            return False
            
        # check position size limits
        current_position_value = 0
        if symbol in self.account_state.positions:
            current_position_value = (
                self.account_state.positions[symbol].quantity * current_price
            )
            
        # check if adding position would exceed max size
        max_position_value = self.account_state.total_value * self.account_state.max_position_size
        if current_position_value >= max_position_value:
            return False
            
        return True
    
    def _can_sell(self, symbol: str) -> bool:
        """check if we can sell the symbol"""
        # check if we have position to sell
        if symbol not in self.account_state.positions:
            return False
            
        position = self.account_state.positions[symbol]
        
        # check if we have enough quantity to sell
        if position.quantity <= 0:
            return False
            
        return True
    
    def get_position_size_limit(self, symbol: str, current_price: float) -> float:
        """get maximum position size for a symbol"""
        max_position_value = self.account_state.total_value * self.account_state.max_position_size
        
        # check current position
        current_position_value = 0
        if symbol in self.account_state.positions:
            current_position_value = (
                self.account_state.positions[symbol].quantity * current_price
            )
            
        # calculate remaining capacity
        remaining_capacity = max_position_value - current_position_value
        
        # convert to quantity
        max_quantity = remaining_capacity / current_price if current_price > 0 else 0
        
        return max(0, max_quantity)
    
    def get_max_buy_quantity(self, symbol: str, current_price: float) -> float:
        """get maximum quantity we can buy"""
        if not self._can_buy(symbol, current_price):
            return 0.0
            
        # limited by cash
        max_by_cash = self.account_state.cash / current_price
        
        # limited by position size
        max_by_position = self.get_position_size_limit(symbol, current_price)
        
        return min(max_by_cash, max_by_position)
    
    def get_max_sell_quantity(self, symbol: str) -> float:
        """get maximum quantity we can sell"""
        if not self._can_sell(symbol):
            return 0.0
            
        return self.account_state.positions[symbol].quantity
    
    def validate_action(self, 
                       action: ActionType, 
                       symbol: str, 
                       quantity: float,
                       current_price: float) -> Tuple[bool, str]:
        """validate a trading action"""
        
        if action == ActionType.HOLD:
            return True, "valid"
            
        elif action == ActionType.BUY:
            if not self._can_buy(symbol, current_price):
                return False, "insufficient cash or position size limit"
                
            max_quantity = self.get_max_buy_quantity(symbol, current_price)
            if quantity > max_quantity:
                return False, f"quantity {quantity} exceeds max buyable {max_quantity:.2f}"
                
            if quantity < self.account_state.min_trade_size / current_price:
                return False, f"quantity {quantity} below minimum trade size"
                
        elif action == ActionType.SELL:
            if not self._can_sell(symbol):
                return False, "no position to sell"
                
            max_quantity = self.get_max_sell_quantity(symbol)
            if quantity > max_quantity:
                return False, f"quantity {quantity} exceeds position {max_quantity:.2f}"
                
        return True, "valid"
    
    def get_action_mask(self, 
                       symbols: List[str], 
                       current_prices: Dict[str, float],
                       market_hours: bool = True) -> Dict[str, List[bool]]:
        """get action mask for all symbols"""
        masks = {}
        
        for symbol in symbols:
            if symbol not in current_prices:
                masks[symbol] = [True, False, False]  # only hold allowed
                continue
                
            valid_actions = self.get_valid_actions(symbol, current_prices[symbol], market_hours)
            
            # create mask (hold, buy, sell)
            mask = [
                ActionType.HOLD in valid_actions,
                ActionType.BUY in valid_actions,
                ActionType.SELL in valid_actions
            ]
            
            masks[symbol] = mask
            
        return masks

# example usage
if __name__ == "__main__":
    # create test account state
    positions = {
        'SPY': Position('SPY', 10, 400, 410, 100),
        'QQQ': Position('QQQ', 5, 300, 305, 25)
    }
    
    account = AccountState(
        cash=1000,
        total_value=5000,
        positions=positions,
        max_position_size=0.2,  # 20% max per position
        min_trade_size=50
    )
    
    # create action masker
    masker = ActionMasker(account)
    
    # test action validation
    symbols = ['SPY', 'QQQ', 'BTC']
    current_prices = {'SPY': 410, 'QQQ': 305, 'BTC': 50000}
    
    # get action masks
    masks = masker.get_action_mask(symbols, current_prices)
    
    print("action masks:")
    for symbol, mask in masks.items():
        print(f"{symbol}: hold={mask[0]}, buy={mask[1]}, sell={mask[2]}")
    
    # test specific validations
    print("\nvalidation tests:")
    
    # valid buy
    valid, msg = masker.validate_action(ActionType.BUY, 'BTC', 0.01, 50000)
    print(f"buy 0.01 BTC: {valid} - {msg}")
    
    # invalid sell (no position)
    valid, msg = masker.validate_action(ActionType.SELL, 'BTC', 0.01, 50000)
    print(f"sell 0.01 BTC: {valid} - {msg}")
    
    # valid sell
    valid, msg = masker.validate_action(ActionType.SELL, 'SPY', 5, 410)
    print(f"sell 5 SPY: {valid} - {msg}")
