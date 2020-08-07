import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt 

PG = wb.DataReader('PG', data_source='yahoo', start='1995-1-1')

PG['simple_return'] = (PG['Adj Close'] / PG['Adj Close'].shift(1)) - 1

#Podemos plotar esses valores em um grafico


PG['simple_return'].plot(figsize=(8, 5))


#Esses valores dentro do parentenses determinam somente o tamanho do grafico
#Para o grafico aparecer teremos que chamar a funçao


plt.show()


#Pode-se observar que os retornos negativos tem uma magnitude maior que os positivos, ja os positivos normalmente se acumulam ao longo do tempo
#Porem o investidor que esta interessado em comprar açoes e mantelas a longo prazo
#O recomendado é analisar o retorno medio ou taxa media de retorno


# avg_return_a = PG['simple return'].mean()


#O comando mean() calcula a taxa de retorno media diaria
#Porem a taxa media diaria é muito muito pequena
#Para isso calcula-se a taxa media anual de retorno, pois diz muito mais para o investidor
#obs: os dados que extraimos nao sao compostos de 350 observaçoes, nao sao levados em conta os dias que nao houve neg
#O numero de dias de negociacao por ano efetivos é 250

avg_return_a = PG['simple_return'].mean() * 250
#esses valores agora serao os de um ano de negociacao
#para deixar ainda mais apresentavel
#vamos torna-lo um str e arredondalo 
print(str(round(avg_return_a, 5) * 100) + '%')

