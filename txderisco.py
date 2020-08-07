import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from pandas_datareader import data as wb 

tickers = ['PG', 'BEI.DE']

sec_data = pd.DataFrame()

for t in tickers:
    sec_data[t] = wb.DataReader(t, data_source='yahoo', start='2007-1-1')['Adj Close']


#Vamos utilizar a taxa de retorno logaritmica 
#O desvio padrao dos retornos de uma empresa tambem pode ser chamado de risco ou volatilidade
#Uma acao que mostra um grande desvio de sua media, é chamada de mais volatil

sec_returns = np.log(sec_data / sec_data.shift(1))

#Agora iremos calcular a media da taxa de retorno log.
sec_returns['PG'].mean()

#Agora iremos calcular a media da taxa de retorno log. anual
sec_returns['PG'].mean() * 250

#agora iremos calcular o desvio padrao, que é calculado com o comando .std()
sec_returns['PG'].std()
sec_returns['PG'].std() * 250 ** 0.5

#Agora iremos calcular a media da taxa de retorno log.
sec_returns['BEI.DE'].mean()

#Agora iremos calcular a media da taxa de retorno log. anual
sec_returns['BEI.DE'].mean() * 250

#agora iremos calcular o desvio padrao, que é calculado com o comando .std()
sec_returns['BEI.DE'].std()
sec_returns['BEI.DE'].std() * 250 ** 0.5

#Podemos printar ambos resultados juntos, para ficar mais facil analisar
#Poderia simplesmente, escrever um a um ex: print(sec_returns....)

#Porem vamos imprimir na mesma linha os resultados, e para isso vamos usar o numpy

#A media e os desvios padrao que obtivemos foram resultado de matrizes unidemensionais
#Para isso vamos criar um array em duas dimensoes para satisfazer
#Para fazer isso vamos adcionar outro colchetes, cada par de colchetes aumenta o numero de dimensoes da matriz numpy

print(sec_returns[['PG', 'BEI.DE']].mean() * 250)
print(sec_returns[['PG', 'BEI.DE']].std() * 250 ** 0.5)