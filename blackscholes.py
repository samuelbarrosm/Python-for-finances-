#Vamos utilizar a formula de black scholes merton para derivativos no mercado de opcoes
import numpy as np 
import pandas as pd 
from pandas_datareader import data as wb 
from scipy.stats import norm 

#Vamos utilizar as formulas do d1 e d2 para efetuar o calculo de BSM
#S = preço da acao 
#K = preco de exercicio
#r = taxa livre de risco
#stdev = desvio padrao
#T = intervalo de tempo (anos)

def d1(S, K, r, stdev, T):
    return (np.log(S/K) + (r + stdev ** 2 / 2) * T) / (stdev * np.sqrt(T))

def d2(S, K, r, stdev, T):
    return (np.log(S/K) + (r - stdev ** 2 / 2) * T) / (stdev * np.sqrt(T))

#Vamos utilizar a distribuiçao normal cumulativa (cdf)
#Mostra como os dados se acumulam no tempo
#norm.cdf(0)    

def BSM(S, K, r, stdev, T):
    return (S * norm.cdf(d1(S, K, r, stdev, T))) - (K * np.exp(-r * T) * norm.cdf(d2(S, K, r, stdev, T)))



ticker = 'PG'
data = pd.DataFrame() 
data[ticker] = wb.DataReader(ticker, data_source='yahoo', start='2007-1-1', end='2017-3-21')['Adj Close']

S = data.iloc[-1]
log_returns = np.log(1 + data.pct_change())

stdev = log_returns.std() * 250 ** 0.5

#Aqui estamos atribuindo valores para os parametros
r = 0.025
K = 110.0
T = 1