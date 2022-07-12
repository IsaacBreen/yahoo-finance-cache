from yahoo_finance_cache import __version__


def test_version():
    assert __version__ == '0.1.0'


def test_tutorial():
    from yahoo_finance_cache import CachedYahooDataReader
    
    
    # Cache the data in a directory called 'cache'
    yahoo_data_reader = CachedYahooDataReader('cache')

    # Download stock data for Apple from Yahoo Finance
    df = yahoo_data_reader.DataReader('AAPL', start_date='2021-01-01', end_date='2021-01-31')

    # Get the same data from the cache (will be much faster than downloading again)
    df2 = yahoo_data_reader.DataReader('AAPL', start_date='2021-01-01', end_date='2021-01-31')
    assert df.equals(df2), 'Data from cache and from Yahoo Finance should be the same.'