import pandas as pd
import numpy as np

class CandlestickEngulfing:
    """
    Candlestick Engulfing Pattern Detector

    Identifies bullish and bearish engulfing patterns where one candle
    completely engulfs the previous candle's body.
    """

    def __init__(self, min_body_pct_left=0, min_body_pct_right=0, filter_by_atr=False, atr_period=14):
        self.min_body_pct_left = min_body_pct_left
        self.min_body_pct_right = min_body_pct_right
        self.filter_by_atr = filter_by_atr
        self.atr_period = atr_period

    def calculate_body_range_ratio(self, open_price, close_price, high_price, low_price):
        """Calculate the ratio of body size to total price range."""
        body_range = abs(open_price - close_price)
        total_range = high_price - low_price
        if pd.isna(total_range) or total_range <= 0:
            return 0
        return (body_range / total_range * 100)

    def calculate_atr(self, df):
        """Calculate Average True Range"""
        high = df['high']
        low = df['low']
        close = df['close'].shift(1)

        tr1 = high - low
        tr2 = abs(high - close)
        tr3 = abs(low - close)

        true_range = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
        return true_range.rolling(window=self.atr_period).mean()

    def detect_engulfing(self, df):
        """
        Detect bullish and bearish engulfing patterns.

        Returns:
            tuple: (bullish_signals, bearish_signals) as boolean Series
        """
        # Get previous candle data
        prev_open = df['open'].shift(1)
        prev_high = df['high'].shift(1)
        prev_low = df['low'].shift(1)
        prev_close = df['close'].shift(1)

        # Calculate body ratios
        current_body_ratio = df.apply(
            lambda row: self.calculate_body_range_ratio(
                row['open'], row['close'], row['high'], row['low']
            ), axis=1
        )

        prev_body_ratio = pd.Series([
            self.calculate_body_range_ratio(o, c, h, l)
            for o, c, h, l in zip(prev_open, prev_close, prev_high, prev_low)
        ], index=df.index)

        # Bearish engulfing: current red candle engulfs previous green candle
        bearish_condition = (
            (df['open'] >= prev_high) &  # Current open >= previous high
            (df['close'] <= prev_low) &  # Current close <= previous low
            (df['open'] > df['close']) &  # Current candle is bearish
            (prev_open < prev_close) &    # Previous candle was bullish
            (prev_body_ratio >= self.min_body_pct_left) &
            (current_body_ratio >= self.min_body_pct_right)
        )

        # Bullish engulfing: current green candle engulfs previous red candle
        bullish_condition = (
            (df['open'] <= prev_low) &   # Current open <= previous low
            (df['close'] >= prev_high) &  # Current close >= previous high
            (df['open'] < df['close']) &  # Current candle is bullish
            (prev_open > prev_close) &    # Previous candle was bearish
            (prev_body_ratio >= self.min_body_pct_left) &
            (current_body_ratio >= self.min_body_pct_right)
        )

        # Apply ATR filter if enabled
        if self.filter_by_atr:
            atr = self.calculate_atr(df)
            body_size = abs(df['open'] - df['close'])
            atr_condition = body_size > atr

            bearish_condition = bearish_condition & atr_condition
            bullish_condition = bullish_condition & atr_condition

        return bullish_condition.fillna(False), bearish_condition.fillna(False)