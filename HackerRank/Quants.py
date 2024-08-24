__author__ = 'harsshal'

from matplotlib.finance import quotes_historical_yahoo_ohlc
date1=(2010,12,31)
date2=(2015,12,31)
price=quotes_historical_yahoo_ohlc('MSFT', date1, date2)
print("hi")