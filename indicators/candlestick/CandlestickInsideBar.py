import pandas as pd

class CandlestickInsideBar:
    """
    Candlestick Inside Bar Pattern Detector

    Identifies inside bar patterns where the current candle's range
    is completely within the previous candle's range.
    """

    def __init__(self):
        pass

    def detect_inside_bar(self, df):
        """
        Detect inside bar patterns.

        Returns:
            pandas.Series: Boolean series indicating inside bar patterns
        """
        # Get previous candle data
        prev_high = df['high'].shift(1)
        prev_low = df['low'].shift(1)

        # Inside bar condition: current high < prev high and current low > prev low
        inside_bar = (df['high'] < prev_high) & (df['low'] > prev_low)

        return inside_bar