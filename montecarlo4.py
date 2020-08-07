#Vamos utilizar a simulacao de monte carlo para tentar prever o preco futuro de uma empresa

import numpy as np 
from pandas_datareader import data as wb 
import pandas as pd 
import matplotlib.pyplot as plt
from scipy.stats import norm 

ticker = ['PG']
data = pd.DataFrame() 
data[ticker] = wb.DataReader(ticker, data_source='yahoo', start='2007-1-1')['Adj Close']

#Essa é uma outra forma de obter o retorno simples a partir de uma base de dados
log_returns = np.log(1 + data.pct_change())
log_returns.tail() 

data.plot(figsize=(10, 6))
log_returns.plot(figsize=(10, 6))

u = log_returns.mean() 

var = log_returns.var() 

#Agora iremos calcular o drift(é o retorno diario esperado da açao)

drift = u - (0.5 * var)

#Aqui estamos determinando o desvio dos restornos logaritmicos
stdev = log_returns.std() 

#Obs: Nao iremos anualizar em momento algum os valores dos retornos, pois estamos tentando prever os retornos diarios das acoes

#Podemos dizer que o movimento browninano compreende a soma do drift com a variacia ajustava vezes E elevado a R
#r = drift + stdev * e ** r
#Tanto o drift quando stdev, sao series do panda
#Temos que transforma-los ambos em array numpy 

#Aqui usando numpy
np.array(drift)
np.array(stdev)

#A segunda variavel do movimento browniano é a variavel Z
#O Z corresponde a distancia entre a media e os eventos, expresso pelo numero de desvios padrao
#Usamos o comando norm.ppf para extrai-lo

norm.ppf(0.95)
#Se um evento tem por exemplo 95% de cahnce de ocorrer a distancia entre esse evento e a media sera o valor dado
#Para concluir essa analise podemos criar uma variavel
#Utilizando dois argumentos estamos criando uma matriz multidimensional com 10 linhas 2 colunas

x = np.random.rand(10, 2)

#Agora iremos incluir esses numeros aleatorios  dentro de norm.ppf

norm.ppf(x)

#Assim iremos encontrar a distancia da media a cada uma das prob geradas aleatoriamente
#Cada numero da matriz X corresponde ao mesmo da segunda matriz

#O valor de Z pode ser obtido por 
Z = norm.ppf(np.random.rand(10, 2))

#Estamos interessados em prever o preço das acoes para os proximos 1000 dias
t_intervals = 1000

#Aqui estamos determinando o numero de series de previcoes futuras para o preço das acoes
iterations = 10

#Vamos calcular o preço do retorno diario

daily_returns = np.exp(drift.values + stdev * norm.ppf(np.random.rand(t_intervals, iterations))) 

#Logo obteremos uma matriz de mil por dez com valores dos retornos diarios

#Vamos agora criar um lista de preços
#Cada preço deve ser igual ao produto do preço observado no dia interior e o retorno diario simulado
#Logo teremos por exemplo, o preço das acoes no dia posterior, podendo simular quantos dias for possiveis

#Aqui estamos selecionando o ultimo preço obtido pelo mercado
#O -1 dentro dos colchetes sinaliza que estamos procurando o ultimo valor obtido
S0 = data.eloc[-1]

#Ela so pode ser tao grande quanto a matriz dos retornos diarios
#Utilizando o metodo zeros_like, ele cria um array com as mesmas dimensoes de um array ja conhecido, e substitui os elementos por 0
price_list = np.zeros_like(daily_returns)

#Agora iremos substituir todos os valores da matriz pelos valores dos preços
#Primeiro vamos substituir o valor inicial, que sera o S0

price_list[0] = S0

#Agora iremos criar um loop que começa no dia um e vai ate o dia mil 
for t in range(1, t_intervals):
    price_list[t] = price_list[t - 1] * daily_returns[t]

plt.figure(figsize=(10, 6))
plt.plot(price_list)     