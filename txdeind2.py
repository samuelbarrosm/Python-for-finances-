import numpy as np 
import pandas as pd 
from pandas_datareader import data as wb 
import matplotlib.pyplot as plt



#Podemos pegar a taxa de fechamento de uma empresa e comparar com diferentes indices
#Vamos analisar a taxa de fechamento de uma empresa em relacao aos indices de retorno da GSPC e DJI

tickers_2 = ['PG', '^GSPC', '^DJI']

data_2 = pd.DataFrame()  

for c in tickers_2:
    data_2[c] = wb.DataReader(c, data_source='yahoo', start='2007-1-1')['Adj Close']

data_2.head() 
data_2.tail() 

(data_2 / data_2.iloc[0] * 100).plot(figsize=(15, 6))
plt.show()


data_return = (data_2 / data_2.shift(1)) - 1
data_return.head()
data_return.tail() 

annuald_return = data_return.mean() * 250 

print(str(round(annuald_return, 5) * 100) + '%')

