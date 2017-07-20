import os
import pandas as pd
from download_yahoo import get_symbols

def get_symbol_path(symbol, base_dir="data2"):
    """File path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_symbol_data(symbol):
        return pd.read_csv(get_symbol_path(symbol), index_col="Date",
                           parse_dates=True, usecols=["Date", "Adj Close"], 
                           na_values=["nan"]).rename(columns={"Adj Close":symbol})#.dropna()

def get_data(symbols, dates):
    """Percent difference data for symbols/dates."""
    df = pd.DataFrame(index=dates)

    for symbol in symbols:
        # TODO: Read and join data for each symbol
        if os.path.isfile(get_symbol_path(symbol)):
		dfSym = get_symbol_data(symbol)
        	dfSym[symbol] = dfSym[symbol][::-1].pct_change()
		df = df.join(dfSym, how='inner')
    return df

if __name__ == "__main__":
    
    # 20 years
    dates = pd.date_range('1996-09-10', '2016-09-10')
    
    # S&P500 symbols
    symbols = get_symbols()
    
    # Get stock data
    df = get_data(symbols, dates)
    df.to_csv('data.csv')

