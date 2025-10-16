import pandas as pd

class ADX:
    """
    Average Directional Index (ADX) with Histogram

    Measures trend strength and direction using directional movement indicators.
    """

    def __init__(self, period=14):
        self.period = period

    def calculate(self, df):
        """
        Calculate ADX and directional indicators.

        Args:
            df (pandas.DataFrame): DataFrame with 'high', 'low', 'close' columns

        Returns:
            tuple: (adx, di_plus, di_minus)
        """
        # Calculate True Range
        high = df['high']
        low = df['low']
        close = df['close']

        tr1 = high - low
        tr2 = abs(high - close.shift(1))
        tr3 = abs(low - close.shift(1))
        tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
        atr = tr.rolling(window=self.period).mean()

        # Directional Movement
        dm_plus = high - high.shift(1)
        dm_minus = low.shift(1) - low
        dm_plus = dm_plus.where((dm_plus > dm_minus) & (dm_plus > 0), 0)
        dm_minus = dm_minus.where((dm_minus > dm_plus) & (dm_minus > 0), 0)

        # Directional Indicators
        di_plus = 100 * (dm_plus.rolling(window=self.period).mean() / atr)
        di_minus = 100 * (dm_minus.rolling(window=self.period).mean() / atr)

        # ADX
        dx = 100 * abs(di_plus - di_minus) / (di_plus + di_minus)
        adx = dx.rolling(window=self.period).mean()

        return adx, di_plus, di_minus