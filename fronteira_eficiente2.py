#Esse codigo é utilizado para calcular a fronteira eficiente de um portfolio
#Esse codigo tem como objetivo avaliar a eficiencia das de um portfolio

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt  
from pandas_datareader import data as wb 

assets = ['PG', '^GSPC']

pf_data = pd.DataFrame() 

for a in assets:
    pf_data[a] = wb.DataReader(a, data_source='yahoo', start='2010-1-1')['Adj Close']

pf_data.tail()

(pf_data / pf_data.iloc[0] * 100).plot(figsize=(10, 5))

log_returns = np.log(pf_data / pf_data.shift(1))

log_returns.mean() * 250 

log_returns['PG'].cov(log_returns['^GSPC']) * 250

#Correlacao superior a 30% indica que sao muito correlacionados, isso é bom
log_returns['PG'].corr(log_returns['^GSPC']) 

#Agora vamos aprtir pra uma otimizacao do portfolio por uma perspectiva mais tecnica
#Vamos criar uma variavel que ira contar o numero de ativos na nossa carteira

num_assets = len(assets)

#Agora iremos criar dois pesos alatorios para esses ativos

#O metodo random.random pode gerar dois numeros aleatorios entre o e 1
arr = np.random.random(2)

#Vamos calcular a soma do valor dos dois pesos obtidos aleatoriamente 
arr[0] + arr[1]
#A soma desses pesos aleatorios nem sempre sera igual a 1

#Para fazer com que a soma seja = 1, temos
weights = np.random.random(num_assets)
weights /= np.sum(weights)

print(weights)

#O codigo /= significa o peso, dividido pela soma dos pesos, como um loop
#Lembrando, quando se usa o numpy estamos transformando esses valores em elementos da matriz
#Por isso quando atribuimos esse codigo a soma dos pesos é igual a 1

#Para escrever o retorno esperado de um portfolio:
#Retorno = soma do produto da media dos retornos logaritmicos anualizados pelo seus respectivos pesos
#Essa funcao .sun do numpy, funciona somando objetos em mais de uma dimensao, por isso difere do sum(nativo do python)

np.sum(weights * log_returns.mean()) * 250

#Esse codigo como ja foi visto fornece a variancia
np.dot(weights.T, np.dot(log_returns['PG'].cov(log_returns['^GSPC']) * 250, weights))

#Esse codigo como ja foi visto fornece a volatilidade
np.sqrt(np.dot(weights.T, np.dot(log_returns['PG'].cov(log_returns['^GSPC']) * 250, weights)))

#Usaremos esses 3 codigos para calcular o retorno e a volatilidade na simulacao dos portfolios de minima variancia
#Agora iremos criar um grafico onde mil simulacoes de minima variancia serao plotadas
#Nao estamos fazendo 1000 investimentos diferentes
#estamos fazendo 1000 combinacoes dos mesmos ativos(pesos)

#Esse loop, gerara uma repeticao de 1000 possibilidades para os pesos dos ativos
pfolio_returns = []
pfolio_volatilities = []

for x in range (1000):
    weights = np.random.random(num_assets)
    weights /= np.sum(weights)
    pfolio_returns.append(np.sum(weights * log_returns.mean()) * 250)
    pfolio_volatilities.append(np.sqrt(np.dot(weights.T, np.dot(log_returns['PG'].cov(log_returns['^GSPC']) * 250, weights))))


#Fazemos isso para transformar os numeros dispersos, em arrays contidos numa matriz, fica mais pratico de trabalhar
pfolio_returns = np.array(pfolio_returns)
pfolio_volatilities = np.array(pfolio_volatilities)

pfolio_volatilities,pfolio_returns

#Agora iremos criar um objeto no dataframe com duas colunas, uma para os retornos e outra para as respectivas volatilidades

portfolios = pd.DataFrame({'Return': pfolio_returns, 'Volatility': pfolio_volatilities})
portfolios.head()
portfolios.tail()

#Agora estamos plotando os valores do dataframe num grafico 
#O tipo de grafico que estamos inserindo é to tipo scatter (grafico de dispersao)
portfolios.plot(x='Volatility', y='Return', kind='scatter', figsize=(10, 6))

plt.xlabel('Expected Volatility') 
plt.ylabel('Expected Return')

plt.show()




