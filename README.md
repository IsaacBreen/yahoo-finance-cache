A simple library for caching Yahoo finance data. Built on top of Pandas DataReader.

## Usage

```python
from cached_yahoo_finance import CachedYahooDataReader


# Cache data in a directory called 'cache'
yahoo_data_reader = CachedYahooDataReader('cache')

# Download stock data for Apple from Yahoo Finance
df = yahoo_data_reader.DataReader('AAPL', start_date='2021-01-01', end_date='2021-01-31')

# Get the same data from the cache (will be much faster than downloading again)
df2 = yahoo_data_reader.DataReader('AAPL', start_date='2021-01-01', end_date='2021-01-31')
assert df.equals(df2), 'Data from cache and from Yahoo Finance should be the same'
```

## Install

```bash
pip install yahoo-finance-cahce
```