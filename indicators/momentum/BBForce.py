import pandas as pd

class BBForce:
    """
    Bollinger Bands Force Indicator

    Measures the force or intensity of price movements relative to Bollinger Bands.
    The force is calculated as the standardized deviation from the moving average.
    """

    def __init__(self, period=20, std_dev=2):
        self.period = period
        self.std_dev = std_dev

    def calculate(self, df):
        """
        Calculate BBForce values.

        Args:
            df (pandas.DataFrame): DataFrame with 'close' column

        Returns:
            pandas.Series: BBForce values
        """
        # Calculate simple moving average
        sma = df['close'].rolling(window=self.period).mean()

        # Calculate rolling standard deviation
        std = df['close'].rolling(window=self.period).std()

        # Calculate Bollinger Bands
        upper_band = sma + self.std_dev * std
        lower_band = sma - self.std_dev * std

        # Calculate force as standardized deviation from mean
        force = (df['close'] - sma) / (self.std_dev * std)

        return force