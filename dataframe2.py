#Criando um conjunto de dados com 5 colunas, mostrando o preço de fechamento ajustado de 5 empersas diferentes
#Para fazer isso baster a ultima coluna da tabela das açoes
#Como estamos interessados somente na ultima coluna de dados, escrevemos o nome da coluna que queremos ex: ['Adj Close']
#Para esse codigo funcionar é necessario que o nome das 5 colunas estejam iguais 

from pandas_datareader import data as wb
import pandas as pd 
import numpy as np

tickers = ['PG', 'MSFT', 'T', 'AAPL', 'GE']
new_data = pd.DataFrame()
for t in tickers:
    new_data[t] = wb.DataReader(t, data_source='yahoo', start='1995-1-1')['Adj Close']

print(new_data.tail())    
