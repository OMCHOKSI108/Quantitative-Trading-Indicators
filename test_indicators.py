import pandas as pd
import numpy as np
from indicators import CandlestickEngulfing, BBForce, MACDV, ADX

# Sample test data
np.random.seed(42)
dates = pd.date_range('2023-01-01', periods=100, freq='D')
df = pd.DataFrame({
    'open': np.random.uniform(100, 200, 100),
    'high': np.random.uniform(150, 250, 100),
    'low': np.random.uniform(50, 150, 100),
    'close': np.random.uniform(100, 200, 100),
    'volume': np.random.randint(1000, 10000, 100)
}, index=dates)

# Ensure high >= max(open, close), low <= min(open, close)
df['high'] = df[['open', 'close', 'high']].max(axis=1)
df['low'] = df[['open', 'close', 'low']].min(axis=1)

def test_engulfing():
    detector = CandlestickEngulfing()
    bullish, bearish = detector.detect_engulfing(df)
    assert isinstance(bullish, pd.Series)
    assert isinstance(bearish, pd.Series)
    print("Engulfing test passed")

def test_bbforce():
    bbforce = BBForce()
    force = bbforce.calculate(df)
    assert isinstance(force, pd.Series)
    print("BBForce test passed")

def test_macdv():
    macdv = MACDV()
    macd, signal, hist, vol_hist = macdv.calculate(df)
    assert all(isinstance(x, pd.Series) for x in [macd, signal, hist, vol_hist])
    print("MACDV test passed")

def test_adx():
    adx_calc = ADX()
    adx, di_plus, di_minus = adx_calc.calculate(df)
    assert all(isinstance(x, pd.Series) for x in [adx, di_plus, di_minus])
    print("ADX test passed")

if __name__ == "__main__":
    test_engulfing()
    test_bbforce()
    test_macdv()
    test_adx()
    print("All tests passed!")