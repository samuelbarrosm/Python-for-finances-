#Iremos calcular a variancia de um portfolio de duas ou mais açoes
#Se um portfolio tiver duas açoes, seu risco sera uma funcao das variancias das duas açoes e da correlacao entre elas

#variancia do portfolio de duas açoes pode ser dado por (A.B + C.D)**2
#Com A, C etc sendo os pesos das acoes, e B, D etc é o desvio padrao de cada açao
#A soma de A, C etc = 1 
#Pode ser extendido para um numero N de acoes


#Usando o numpy podemos utiliza-lo para facilitar as manipulacoes com matrizes

import numpy as np  
import pandas as pd  
import matplotlib.pyplot as plt   
from pandas_datareader import data as wb

new_data = pd.DataFrame()     

tickers = ['PG', 'BEI.DE']

for t in tickers: 
    new_data[t] = wb.DataReader(t, data_source='yahoo', start='2007-1-1')['Adj Close']

sec_returns = ((new_data / new_data.shift(1)) - 1) 

#Vamos considerar uma carteira igualmente ponderada para essas empresas

#Vamos salvar esses valores numa matriz numpy chamada weights

weights = np.array([0.5, 0.5])   

#O codigo abaixo se refere a uma multiplacao de matrizes 
#Multiplicao de matrizes é diferente de multiplicao de escalares
#O codigo numpy.dot() faz o produto de duas arrays 
#Para o produto de duas matrizes, ex: (AB) ** 2 = A(TRANSPOSTA).B.A 
#O comando .T apos uma array, calcula a transposta da mesma

pfolio_var = np.dot(weights.T, np.dot(sec_returns['PG'].cov(sec_returns['BEI.DE']) * 250, weights))

#O resultado dessa linha acima é a variancia da carteira

#OBS:Se quisermos a volatilidade da carteira deve-se elevar a expressao a 0.5

pfolio_vol = (pfolio_var ** 0.5)

print(str(round(pfolio_vol, 5) * 100) + '%')
print(pfolio_var)
