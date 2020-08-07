import numpy as np
from pandas_datareader import data as wb 
import pandas as pd 
import matplotlib.pyplot as plt 

ind_data = pd.DataFrame()

#Atribuindo os indices avaliados

tickers = ['^GSPC', '^IXIC', '^GDAXI']

#O uso de ^ é para indicar que estamos tratando de indices

for t in tickers:
    ind_data[t] = wb.DataReader(t, data_source='yahoo', start='2007-1-1')['Adj Close']
    

ind_data.head() 
ind_data.tail() 

#Normalizando os graficos

(ind_data / ind_data.iloc[0] * 100).plot(figsize=(15, 6))
plt.show()
#Calculando a taxa de retorno simples dos indices

ind_returns = (ind_data / ind_data.shift(1)) - 1
ind_returns.tail() 
ind_returns.head() 

#Aqui temos os retornos anuais
annual_ind_returns = ind_returns.mean() * 250

#Podemos analisar qual indice produziu melhores resultados

print(str(round(annual_ind_returns, 5) * 100) + '%')



