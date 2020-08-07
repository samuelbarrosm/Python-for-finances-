#Nessas linhas de codigo o objetivo é calcular a taxa media de retorno anual para um portfolio 


import numpy as np
import pandas as pd 
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

tickers = ['AAPL', 'MSFT', 'PG', 'GE']

new_data = pd.DataFrame() 

for t in tickers:
    new_data[t] = wb.DataReader(t, data_source='yahoo', start='1995-1-1')['Adj Close']

#Vamos criar um grafico de linhas para entender como essas açoes se comportaram em todo o periodo analisado.
#Para normalizar os dados na base 100 podemos fazer P1/P0 * 100
#O indexador .iloc[0] ira extrair os dados da primeira coluna da tabela

(new_data / new_data.iloc[0] * 100).plot(figsize=(15, 6))
#Fazendo isso, esses calculos vao normalizar o grafico com 100 como parametro, todas iniciando no mesmo ponto vertical 100

#O comando .loc{rotulo} o rotulo é para indicar a primeira linha, as datas sao rotulos
#Para usar o .iloc[numero da linha], usa-se o numero da linha que se deseja
#Pode-se usar os dois, depende da praticidade que o programador achar 
plt.show()

#Tem como objetivo analisar o historico das acoes e tentar prever o futuro, uma negociacao lucrativa



#Iremos calcular o retorno simples dessas açoes e criar uma nova tabela com eles
#Usa-se mais retornos simples para negociaçoes num mesmo periodo de tempo
#Utiliza-se a funcao numpy
returns = (new_data / new_data.shift(1)) - 1
returns.head()

weights = np.array([0.25, 0.25, 0.25, 0.25])
#Estamos atribuindo que os pesos das açoes sao iguais, e sempre os pesos devem somar 1
#Utilizando o metodo np.dot, podemos calcular o produto vetorial ou de matrizes de forma rapida
#Em python a matriz unidimensional ou multidimensional que obtivemos é referida como o produto dot entre as variaveis
#Fazendo isso iremos multiplicar o peso de cada açao com o seu respectivo retorno
#Fazendo isso obtem-se o retorno diario da carteira, e não é isso que desejamos no momento
#Podemos calcular o anual como
annual_returns = returns.mean() * 250

np.dot(annual_returns, weights)

pfolio1 = str(round(np.dot(annual_returns, weights), 5) * 100) + '%'
print(pfolio1)

weights2 = np.array([0.4, 0.4, 0.15, 0.05])

pfolio2 = str(round(np.dot(annual_returns, weights2), 5) * 100) + '%'

print(pfolio2)



