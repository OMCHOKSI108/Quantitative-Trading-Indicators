import pandas as pd

class MACDV:
    """
    Volume-Weighted MACD (Moving Average Convergence Divergence)

    Enhanced MACD oscillator that incorporates volume weighting for improved signal reliability.
    """

    def __init__(self, fast_period=12, slow_period=26, signal_period=9):
        self.fast_period = fast_period
        self.slow_period = slow_period
        self.signal_period = signal_period

    def calculate(self, df):
        """
        Calculate MACDV components.

        Args:
            df (pandas.DataFrame): DataFrame with 'close' and 'volume' columns

        Returns:
            tuple: (macd_line, signal_line, histogram, volume_weighted_histogram)
        """
        # Calculate EMAs
        fast_ema = df['close'].ewm(span=self.fast_period).mean()
        slow_ema = df['close'].ewm(span=self.slow_period).mean()

        # MACD line
        macd_line = fast_ema - slow_ema

        # Signal line
        signal_line = macd_line.ewm(span=self.signal_period).mean()

        # Histogram
        histogram = macd_line - signal_line

        # Volume-weighted histogram
        volume_weighted_histogram = histogram * df['volume']

        return macd_line, signal_line, histogram, volume_weighted_histogram