#Aqui iremos utilizar um metodo mais sofisticado para calcular o valor de uma acao no mercado de opcoes
#Chamado de discretizacao de Euler

import numpy as np 
import pandas as pd 
from pandas_datareader import data as wb 
from scipy.stats import norm 
import matplotlib.pyplot as plt 

ticker = 'PG'
data = pd.DataFrame() 
data[ticker] = wb.DataReader(ticker, data_source='yahoo', start='2007-1-1', end='2017-3-21')['Adj Close']

log_returns = np.log(1 + data.pct_change())

#Taxa livre de risco
r = 0.025
#Desvio padrao dos retornos logaritmos
stdev = log_returns.std() * 250 ** 0.5

#Vamos armazenar o novo objeto num array
stdev = stdev.values

#Significa o tempo em anos
T = 1.0 
#Significa os dias uteis dentro do periodo de tempo(anos)
t_intervals = 250 
delta_t = T / t_intervals
#Aqui determinamos o numero de vezes que ira se repetir
iterations = 10000

#A dimensao da matriz sera dada pelo numero de intervalo de tempo acrescido de um
Z = np.random.standard_normal((t_intervals + 1, iterations))
S = np.zeros_like(Z)
S0 = data.iloc[-1]
S[0] = S0



for t in range(1, t_intervals + 1):
    #Aqui temos a formula da discretizaçao de euler
    S[t] = S[t - 1] * np.exp((r - 0.5 * stdev ** 2) * delta_t + stdev * delta_t ** 0.5 * Z[t]) 

plt.figure(figsize=(10, 6))
plt.plot(S[t])



#Podemos determinar a opcao de compra como
#Se S - K > 0 COMPRA
#Se S - K < 0 NAO COMPRA
# 
#Podemos usar o metodo do numpy, .maximum que ira criar um array que contem 0s ou os numeros iguais as diferencas
p = np.maximum(S[-1] - 110, 0)  

#Podemos usar essa formula para descontar a media desse payoff
C = np.exp(-r * T) * np.sum(p) / iterations