from pandas_datareader import data as wb
import pandas as pd 
import numpy as np

tickers = ['PG', 'MSFT', 'T', 'AAPL', 'GE']
new_data = pd.DataFrame()
for t in tickers:
    new_data[t] = wb.DataReader(t, data_source='yahoo', start='1995-1-1')['Adj Close']

new_data.tail(20).to_excel('C:/Users/Vanessa Barros/Desktop/edx/Analise.xlsx')