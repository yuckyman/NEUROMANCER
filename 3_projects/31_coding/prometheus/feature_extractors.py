#!/usr/bin/env python3
"""
prometheus feature extractors
inspired by maven-rl's tcn feature extraction
"""

import numpy as np
import pandas as pd
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from abc import ABC, abstractmethod
import talib

@dataclass
class FeatureConfig:
    """feature extraction configuration"""
    lookback_period: int = 50
    technical_indicators: bool = True
    price_features: bool = True
    volume_features: bool = True
    volatility_features: bool = True
    momentum_features: bool = True

class BaseFeatureExtractor(ABC):
    """base feature extractor interface"""
    
    @abstractmethod
    def extract_features(self, data: pd.DataFrame) -> np.ndarray:
        """extract features from market data"""
        pass
    
    @abstractmethod
    def get_feature_names(self) -> List[str]:
        """get feature names"""
        pass

class TechnicalFeatureExtractor(BaseFeatureExtractor):
    """technical indicator feature extractor"""
    
    def __init__(self, config: FeatureConfig):
        self.config = config
        
    def extract_features(self, data: pd.DataFrame) -> np.ndarray:
        """extract technical indicators"""
        features = []
        
        if len(data) < self.config.lookback_period:
            # pad with zeros if not enough data
            return np.zeros(self._get_feature_dimension())
        
        # use last lookback_period rows
        recent_data = data.tail(self.config.lookback_period)
        
        # price features
        if self.config.price_features:
            price_features = self._extract_price_features(recent_data)
            features.extend(price_features)
            
        # volume features
        if self.config.volume_features:
            volume_features = self._extract_volume_features(recent_data)
            features.extend(volume_features)
            
        # technical indicators
        if self.config.technical_indicators:
            tech_features = self._extract_technical_indicators(recent_data)
            features.extend(tech_features)
            
        # volatility features
        if self.config.volatility_features:
            vol_features = self._extract_volatility_features(recent_data)
            features.extend(vol_features)
            
        # momentum features
        if self.config.momentum_features:
            mom_features = self._extract_momentum_features(recent_data)
            features.extend(mom_features)
            
        return np.array(features)
    
    def _extract_price_features(self, data: pd.DataFrame) -> List[float]:
        """extract price-based features"""
        features = []
        
        # basic price features
        close = data['close'].values
        high = data['high'].values
        low = data['low'].values
        open_price = data['open'].values
        
        # price ratios
        features.append(close[-1] / close[0] - 1)  # total return
        features.append(close[-1] / close[-2] - 1)  # 1-period return
        features.append(close[-1] / close[-5] - 1)  # 5-period return
        features.append(close[-1] / close[-10] - 1)  # 10-period return
        
        # high-low ratios
        features.append(high[-1] / low[-1] - 1)  # current hl ratio
        features.append(np.mean(high[-5:]) / np.mean(low[-5:]) - 1)  # 5-period hl ratio
        
        # price position in range
        recent_high = np.max(high[-20:])
        recent_low = np.min(low[-20:])
        if recent_high > recent_low:
            features.append((close[-1] - recent_low) / (recent_high - recent_low))
        else:
            features.append(0.5)
            
        return features
    
    def _extract_volume_features(self, data: pd.DataFrame) -> List[float]:
        """extract volume-based features"""
        features = []
        
        if 'volume' not in data.columns:
            return [0.0] * 5  # return zeros if no volume data
            
        volume = data['volume'].values
        
        # volume ratios
        features.append(volume[-1] / np.mean(volume[-5:]) - 1)  # current vs 5-period avg
        features.append(volume[-1] / np.mean(volume[-20:]) - 1)  # current vs 20-period avg
        
        # volume trend
        if len(volume) >= 5:
            volume_trend = np.polyfit(range(5), volume[-5:], 1)[0]
            features.append(volume_trend)
        else:
            features.append(0.0)
            
        # volume volatility
        features.append(np.std(volume[-10:]) / np.mean(volume[-10:]) if np.mean(volume[-10:]) > 0 else 0)
        
        # volume-price relationship
        if len(volume) >= 5:
            price_change = data['close'].iloc[-1] / data['close'].iloc[-5] - 1
            volume_change = volume[-1] / np.mean(volume[-5:]) - 1
            features.append(price_change * volume_change)  # price-volume correlation
        else:
            features.append(0.0)
            
        return features
    
    def _extract_technical_indicators(self, data: pd.DataFrame) -> List[float]:
        """extract technical indicators"""
        features = []
        
        close = data['close'].values
        high = data['high'].values
        low = data['low'].values
        volume = data['volume'].values if 'volume' in data.columns else None
        
        # moving averages
        ma_5 = talib.SMA(close, timeperiod=5)
        ma_10 = talib.SMA(close, timeperiod=10)
        ma_20 = talib.SMA(close, timeperiod=20)
        
        features.append(close[-1] / ma_5[-1] - 1 if not np.isnan(ma_5[-1]) else 0)
        features.append(close[-1] / ma_10[-1] - 1 if not np.isnan(ma_10[-1]) else 0)
        features.append(close[-1] / ma_20[-1] - 1 if not np.isnan(ma_20[-1]) else 0)
        features.append(ma_5[-1] / ma_10[-1] - 1 if not np.isnan(ma_5[-1]) and not np.isnan(ma_10[-1]) else 0)
        
        # rsi
        rsi = talib.RSI(close, timeperiod=14)
        features.append(rsi[-1] / 100 - 0.5 if not np.isnan(rsi[-1]) else 0.5)
        
        # bollinger bands
        bb_upper, bb_middle, bb_lower = talib.BBANDS(close, timeperiod=20)
        if not np.isnan(bb_upper[-1]):
            bb_position = (close[-1] - bb_lower[-1]) / (bb_upper[-1] - bb_lower[-1])
            features.append(bb_position)
        else:
            features.append(0.5)
            
        # macd
        macd, macd_signal, macd_hist = talib.MACD(close)
        features.append(macd[-1] if not np.isnan(macd[-1]) else 0)
        features.append(macd_hist[-1] if not np.isnan(macd_hist[-1]) else 0)
        
        # stochastic
        stoch_k, stoch_d = talib.STOCH(high, low, close)
        features.append(stoch_k[-1] / 100 - 0.5 if not np.isnan(stoch_k[-1]) else 0.5)
        
        return features
    
    def _extract_volatility_features(self, data: pd.DataFrame) -> List[float]:
        """extract volatility features"""
        features = []
        
        close = data['close'].values
        
        # returns
        returns = np.diff(np.log(close))
        
        # volatility measures
        features.append(np.std(returns[-5:]))  # 5-period volatility
        features.append(np.std(returns[-10:]))  # 10-period volatility
        features.append(np.std(returns[-20:]))  # 20-period volatility
        
        # volatility ratio
        short_vol = np.std(returns[-5:])
        long_vol = np.std(returns[-20:])
        features.append(short_vol / long_vol if long_vol > 0 else 1)
        
        # atr (average true range)
        atr = talib.ATR(data['high'].values, data['low'].values, close, timeperiod=14)
        features.append(atr[-1] / close[-1] if not np.isnan(atr[-1]) else 0)
        
        return features
    
    def _extract_momentum_features(self, data: pd.DataFrame) -> List[float]:
        """extract momentum features"""
        features = []
        
        close = data['close'].values
        
        # momentum indicators
        mom_5 = talib.MOM(close, timeperiod=5)
        mom_10 = talib.MOM(close, timeperiod=10)
        mom_20 = talib.MOM(close, timeperiod=20)
        
        features.append(mom_5[-1] / close[-1] if not np.isnan(mom_5[-1]) else 0)
        features.append(mom_10[-1] / close[-1] if not np.isnan(mom_10[-1]) else 0)
        features.append(mom_20[-1] / close[-1] if not np.isnan(mom_20[-1]) else 0)
        
        # rate of change
        roc_5 = talib.ROC(close, timeperiod=5)
        roc_10 = talib.ROC(close, timeperiod=10)
        
        features.append(roc_5[-1] / 100 if not np.isnan(roc_5[-1]) else 0)
        features.append(roc_10[-1] / 100 if not np.isnan(roc_10[-1]) else 0)
        
        return features
    
    def _get_feature_dimension(self) -> int:
        """calculate total feature dimension"""
        dim = 0
        
        if self.config.price_features:
            dim += 7  # price features
        if self.config.volume_features:
            dim += 5  # volume features
        if self.config.technical_indicators:
            dim += 9  # technical indicators
        if self.config.volatility_features:
            dim += 5  # volatility features
        if self.config.momentum_features:
            dim += 5  # momentum features
            
        return dim
    
    def get_feature_names(self) -> List[str]:
        """get feature names"""
        names = []
        
        if self.config.price_features:
            names.extend([
                'total_return', 'return_1', 'return_5', 'return_10',
                'hl_ratio', 'hl_ratio_5', 'price_position'
            ])
            
        if self.config.volume_features:
            names.extend([
                'volume_ratio_5', 'volume_ratio_20', 'volume_trend',
                'volume_volatility', 'price_volume_corr'
            ])
            
        if self.config.technical_indicators:
            names.extend([
                'ma_5_ratio', 'ma_10_ratio', 'ma_20_ratio', 'ma_cross',
                'rsi', 'bb_position', 'macd', 'macd_hist', 'stoch'
            ])
            
        if self.config.volatility_features:
            names.extend([
                'vol_5', 'vol_10', 'vol_20', 'vol_ratio', 'atr_ratio'
            ])
            
        if self.config.momentum_features:
            names.extend([
                'mom_5', 'mom_10', 'mom_20', 'roc_5', 'roc_10'
            ])
            
        return names

class MultiTimeframeFeatureExtractor(BaseFeatureExtractor):
    """multi-timeframe feature extractor"""
    
    def __init__(self, timeframes: List[str], config: FeatureConfig):
        self.timeframes = timeframes
        self.config = config
        self.extractors = {
            tf: TechnicalFeatureExtractor(config) 
            for tf in timeframes
        }
    
    def extract_features(self, data: Dict[str, pd.DataFrame]) -> np.ndarray:
        """extract features from multiple timeframes"""
        all_features = []
        
        for timeframe in self.timeframes:
            if timeframe in data:
                features = self.extractors[timeframe].extract_features(data[timeframe])
                all_features.extend(features)
            else:
                # pad with zeros if timeframe not available
                dim = self.extractors[timeframe]._get_feature_dimension()
                all_features.extend([0.0] * dim)
                
        return np.array(all_features)
    
    def get_feature_names(self) -> List[str]:
        """get feature names for all timeframes"""
        names = []
        
        for timeframe in self.timeframes:
            tf_names = self.extractors[timeframe].get_feature_names()
            names.extend([f"{tf}_{timeframe}" for tf in tf_names])
            
        return names

# example usage
if __name__ == "__main__":
    # create sample data
    dates = pd.date_range('2023-01-01', periods=100, freq='1H')
    data = pd.DataFrame({
        'open': 100 + np.random.randn(100).cumsum(),
        'high': 100 + np.random.randn(100).cumsum() + 2,
        'low': 100 + np.random.randn(100).cumsum() - 2,
        'close': 100 + np.random.randn(100).cumsum(),
        'volume': np.random.randint(1000, 10000, 100)
    }, index=dates)
    
    # create feature extractor
    config = FeatureConfig(lookback_period=50)
    extractor = TechnicalFeatureExtractor(config)
    
    # extract features
    features = extractor.extract_features(data)
    feature_names = extractor.get_feature_names()
    
    print(f"extracted {len(features)} features")
    print("feature names:", feature_names[:10])  # show first 10
    print("sample features:", features[:10])
