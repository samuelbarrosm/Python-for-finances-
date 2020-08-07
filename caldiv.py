#Vamos calcular o risco diversificado e nao diversificado de uma carteira de acoes
#Irei fazer com duas acoes, porem se aplica a mais

import numpy as np  
import pandas as pd  
import matplotlib.pyplot as plt  
from pandas_datareader import data as wb 

new_data = pd.DataFrame() 

tickers = ['PG', 'BEI.DE']

for t in tickers: 
    new_data[t] = wb.DataReader(t, data_source='yahoo', start='2007-1-1')['Adj Close']

#Atribuindo o peso de cada açao na carteira em estudo
weights = np.array([0.5, 0.5])

#Calculando a taxa de retorno
sec_returns = (new_data / new_data.shift(1)) - 1


#Calculando a variancia de cada acao
#Estamos atribuindo colchetes duplos pois, esses valores nao sao somente floats, e sim elementos unicos numa matriz bidimensional

PG_var_a = sec_returns['PG'].var() * 250 

BEI_var_a = sec_returns['BEI.DE'].var() * 250

#Para se o risco diversificavel é necessario obter a variancia do portfolio e subtrair da variancia anual ponderada

#Aqui se tem a variancia do portfolio 
pfolio_var = np.dot(weights.T, np.dot(sec_returns['PG'].cov(sec_returns['BEI.DE']) * 250, weights))
 
dr = pfolio_var - (weights[0] ** 2 * PG_var_a) - (weights[1] ** 2 * BEI_var_a)

print(str(round(dr * 100, 3)) + '%')

#O resultado em porcentagem é o risco diversificado(nao sistematico), ja a parte restante do risco é o risco nao diversificado(sistematico)
