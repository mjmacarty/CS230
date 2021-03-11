import pandas_datareader as pdr
import matplotlib.pyplot as plt

stocks = ['GOOG', 'AMZN', 'ZNGA']

data = pdr.get_quote_yahoo(stocks)['price']

