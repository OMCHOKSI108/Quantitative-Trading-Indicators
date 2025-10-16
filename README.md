![Trading Indicators Overview](https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80)

# TradingView Proprietary Indicators

**Author: OM CHOKSI**

This repository contains a comprehensive suite of proprietary technical indicators and trading strategies implemented in Pine Script for TradingView, complemented by Python implementations for quantitative analysis and backtesting. The collection is organized by category, including candlestick patterns, momentum indicators, trend analysis tools, and strategic frameworks designed for systematic trading approaches.

## Python Implementation

The repository includes Python-based implementations of the proprietary indicators, facilitating algorithmic trading, historical backtesting, and automated signal generation. These implementations leverage pandas for data manipulation, numpy for numerical computations, and matplotlib for visualization.

### Quick Start (Python)

To utilize the Python components:

1. Establish a virtual environment:
   ```bash
   python -m venv trade
   ```

2. Activate the environment:
   - Windows: `trade\Scripts\activate`
   - Linux/Mac: `source trade/bin/activate`

3. Install required dependencies:
   ```bash
   pip install pandas numpy matplotlib yfinance
   ```

4. Execute validation tests:
   ```bash
   python test_indicators.py
   ```

5. Conduct interactive analysis:
   ```bash
   jupyter lab indicators.ipynb
   ```

### Available Python Indicators

- **CandlestickEngulfing**: Identifies bullish and bearish engulfing patterns with configurable body percentage thresholds and optional ATR filtering for volatility-based signal validation.
- **CandlestickInsideBar**: Detects inside bar consolidation patterns, useful for identifying potential breakout scenarios.
- **BBForce**: Computes Bollinger Bands force measurements, quantifying the intensity of price deviations from mean levels.
- **MACDV**: Implements an enhanced MACD oscillator incorporating volume weighting for improved signal reliability.

### Usage Example

```python
import pandas as pd
import yfinance as yf
from indicators import CandlestickEngulfing, BBForce

# Acquire historical price data
df = yf.download('AAPL', start='2023-01-01', end='2024-01-01')

# Instantiate indicator objects
engulfing_detector = CandlestickEngulfing(min_body_pct_left=50, min_body_pct_right=60)
bbforce_indicator = BBForce(period=20, std_dev=2)

# Generate signals
bullish_signals, bearish_signals = engulfing_detector.detect_engulfing(df)
bbforce_values = bbforce_indicator.calculate(df)
```

## Pine Script Indicators

The Pine Script implementations provide real-time analysis within the TradingView platform. Indicators are categorized as follows:

### Candlestick Patterns
- CandlestickEngulfing.pine: Engulfing pattern detection
- CandlestickInsideBar.pine: Inside bar identification
- CandlestickKicker.pine: Kicker pattern recognition
- CandlestickPatterns.pine: Comprehensive pattern library
- CandlestickPatterns-HOLP-LOHP.pine: Higher/Lower Open/Close patterns

### Momentum Indicators
- BBForce.pine: Bollinger Bands force analysis
- BodyMassIndicator.pine: Body mass index for momentum
- CommitmentGauge.pine: Commitment measurement
- Flip Flop.pine: Directional change detection
- MACD-V.pine: Volume-weighted MACD
- QuantityQualityCommitment.pine: Commitment quality assessment
- Swoosh Indicator.pine: Momentum oscillation
- WickPowerShift.pine: Wick-based power shifts

### Trend Analysis
- ADX-Hist.pine: Average Directional Index with histogram
- Cloud.pine: Ichimoku cloud implementation

## Trading Strategies

Strategic implementations for automated execution:

- STRG One Bar Pursuit.pine: Single-bar pursuit strategy
- STRG-BBForce.pine: Bollinger Bands force strategy
- STRG-HOLP.pine: Higher/Lower Open/Close strategy
- STRG-KijunArrow.pine: Kijun-based arrow signals
- STRG-KijunArrow-variant-1: Variant implementation
- STRG-KijunArrow-variant-2: Alternative variant

## Data Analysis Notebooks

Jupyter notebooks for empirical analysis and visualization:

- aapl_data.ipynb: Apple Inc. price data analysis
- indicators_strategies.ipynb: Indicator and strategy evaluation

## Documentation

- CONTRIBUTING.md: Contribution guidelines
- LICENSE: Licensing terms
- docs/: Additional documentation in Markdown format
- mkdocs.yml: Documentation configuration

## Dependencies

Core Python dependencies:
- pandas: Data manipulation and analysis
- numpy: Numerical computing
- matplotlib: Plotting and visualization
- yfinance: Yahoo Finance data retrieval
- jupyter: Interactive computing environment

## Testing

Execute the test suite to validate indicator implementations:
```bash
python test_indicators.py
```

## License

This project is licensed under the terms specified in the LICENSE file.

# Calculate signals
bullish, bearish = engulfing.detect_engulfing(df)
force, sma, upper, lower = bbforce.calculate_bbforce(df)
```

## Categories

### Candlestick Patterns
Scripts for detecting and signaling candlestick formations like engulfing, kicker, inside bar, etc.
- CandlestickEngulfing.pine
- CandlestickInsideBar.pine
- CandlestickKicker.pine
- CandlestickPatterns-HOLP-LOHP.pine
- CandlestickPatterns.pine
- Candle Count with labels

### Momentum Indicators
Scripts for analyzing price momentum, including MACD variants, body mass, and commitment gauges.
- BBForce.pine
- BodyMassIndicator.pine
- CommitmentGauge.pine
- Flip Flop.pine
- MACD-V.pine
- QuantityQualityCommitment.pine
- Swoosh Indicator.pine
- WickPowerShift.pine

### Trend Indicators
Scripts for assessing trend strength and direction, such as ADX and Ichimoku Cloud.
- ADX-Hist.pine
- Cloud.pine

### Strategies
Automated trading strategies based on various indicators.
- STRG One Bar Pursuit.pine
- STRG-BBForce.pine
- STRG-HOLP.pine
- STRG-KijunArrow-variant-1
- STRG-KijunArrow-variant-2
- STRG-KijunArrow.pine

## Indicator Descriptions
### TK Crosses Period ###
* The Tenkan-sen (conversion line) and Kijun-sen (base line) indicate price momentum and potential trend changes. A Tenkan-sen crossover above Kijun-sen within the cloud suggests a medium-strength upward signal. Above the cloud, the signal strengthens, and below it, weakens.
* The TKx value in the top right panel shows the number of periods since the Tenkan-sen and Kijun-sen last crossed, which can provide an indication of the trend's strength and potential continuation.
* The top right panel shows the timeframe of the most recent crossovers for reference. Additionally, the current daily range compared to the Average True Range (ATR) can provide insights into momentum strength. An unusually large daily range compared to the ATR can indicate weakening momentum and potentially less fuel for the trend to continue.

## MACD-V: Volatility Normalised Momentum ##
* **Tutorial** (https://school.stockcharts.com/doku.php?id=technical_indicators:macd-v_histogram)
* **Paper SSRN** (https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4099617)
* **Papper PDF** (https://www.naaim.org/wp-content/uploads/2022/05/MACD-V-Alex-Spiroglou-WEB.pdf)

## Kijun Arrow ##
This indicator places an arrow below or above the candlestick when the Kijun-sen changes direction. The remaining elements use standard Ichimoku Cloud settings. (see chart below)

## Quantity Quality Commitment (QQC) ##
The QQC aims to assess the underlying strength of momentum by examining three metrics: quantity, quality, and commitment. (see chart above)
* **Quantity**: This metric counts the number of bullish versus bearish candlesticks over defined periods.
* **Quality**: It measures the quality of bullishness versus bearishness in the candlesticks over defined periods. For example, if a bullish candlestick has minimal wicks, it indicates that the bulls maintained control from beginning to end, resulting in a high score for the bullish tally.
* **Commitment**: The previous two metrics can provide a false sense of direction if there is little volume. A lack of volume can lead to unstable momentum. Therefore, this element incorporates volume to provide a comprehensive view from three perspectives.
* **ADX**:  If the ADX is above 20, the market is considered to be in a trending environment. Otherwise, it's not in a trend, and price action is likely to be choppy. This indicator is presented in histogram format.

## ADX-Histogram ##
* ADX is a tool for assessing the trendiness of a market. If the ADX is below 20, it indicates that recent price action has been choppy, and this is represented by grey bars in the histogram. However, if the ADX is above 20, the bars are coloured orange.

## HOLP-LOHP ##

### Setting Panel ###

* HOLP stands for **H**igh **O**f the **L**ow **P**eriod
* LOHP stands for **L**ow **O**f the **H**igh **P**eriod
* HOLP and LOHP are indicators based on concepts developed by John Carter in his book, "Mastering the Trade." Their purpose is to identify potential reversal points in a trading session.
* The fundamental concept is to identify the session's high and mark the low of the session high for a short entry, and vice versa for a long entry.
* The default lookback period is set to 10 in this indicator, but John Carter emphasized using experience and common sense rather than relying solely on a fixed number.

## Candlestick Kicker Pattern ##

### Setting Panel ###

Few candlestick patterns inflict more pain on traders on the other side of the trade than this signal. When it occurs, think of it as a swift kick to the teeth; the pain is very real.

An upward signal is generated when you have a two-bar formation. The left candle is bearish, while the succeeding one is bullish. Both candles have fat bodies, meaning the open is close to the high, and the close is close to the low for the first candle. For the adjacent candle, the open is close to the low, and the close is close to the high. The other crucial condition is that the open of the first candle must be lower than the open of the latter one.

The downward signal is the opposite of the upward signal.

## Candlestick Inside Bar Pattern ##

### Setting Panel ###

An inside bar pattern is a two-bar scenario in which the range of the second bar is contained within the range of the preceding one. This pattern typically occurs when market volatility is diminishing, and it often precedes an expansion in the price range, resulting in a breakout. A signal will be generated above or below the breakout candle when these conditions are met.

## Candlestick Engulfing Pattern ##

### Setting Panel ###

This is a classic candlestick pattern that serves as a warning that the current trend may have come to an end or is pausing. In a bullish setup, the body of the second candle completely engulfs the body of the previous candle, and vice versa. There are options available for filtering based on the ratio of body size to the overall range for both candles.

## ATR warning ##
An objective way to determine if a candle's range has exceeded its average candle ranges is by comparing it to its Average True Range (ATR). When market conditions become volatile, resulting in notably large candles, such moves are less likely to be sustained, which increases the likelihood of a return to a consolidation phase. This tool can assist traders in tightening their stop-loss orders to lock in potential profits when candles have extended beyond their average range.

At the bottom of the chart, a row of dots is displayed, with colours ranging from black to light grey. These dots indicate the range of the current candle in relation to its ATR. Darker dots signify that the candle's range is closer to the ATR, while lighter grey indicates that it's farther away. When a black dot is present, it signifies that the candle has moved beyond the ATR.

## Body Mass Indicator (BMI) ##
This indicator highlights candles with the largest bodies (the range between open and close) over the past 26 periods. While a bullish candle may have a substantial range (the difference between its high and low), it's a sign of weak bullishness if the bulls can't maintain their position until the candle's close. Conversely, the same principle applies to bearish candles. The goal is to provide users with insight into subtle shifts in the balance of power within price action or the potential for trend continuation amid the ongoing battles between bulls and bears.

## Bar Fractal by Tom Hougaard ##

Source: (https://tradertom.com/wp-content/uploads/2021/04/Tom_Hougaard_The_Trading_Manual_Singles.pdf)

>There are 2 conditions to the technique.

>**Buy Signal**

> The CLOSE of the current bar (1) must be higher than the HIGH of the previous bar (2).
> The CLOSE on this bar (1) must be higher than the HIGH of the bar three bars back (4).
> 3 If those conditions are met, we have a BUY SIGNAL.

>**Sell Signal**

> The CLOSE of the current bar (1) must be lower than the LOW of the previous bar (2).
> The CLOSE on this bar (1) must be lower than the LOW of the bar three bars back (4).
> 3 If those conditions are met, we have a SELL SIGNAL.

## Bollinger Bands Force (BBForce) ##
* Bollinger Bands consist of three components: a simple moving average with +2 and -2 standard deviation lines above and below. When all three components align in the same direction, a Bollinger Bands Force arrow is displayed on the chart, indicating that the forces are in agreement. The default setting for the moving average has been adjusted to 26, instead of the standard 20.
* Fuchsia arrows are displayed whenever the three aforementioned components are in sync.
* Yellow arrows represent a minimal version that only indicates a change in direction among these three components.

## Disclaimer ##
The content and materials are for your information and education only and not financial advice or recommendation.
