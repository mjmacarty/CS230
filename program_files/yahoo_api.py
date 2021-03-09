import pandas_datareader as pdr

stocks = ['GOOG', 'AMZN', 'ZNGA']

data = pdr.get_quote_yahoo(stocks)['price']
print(data)
