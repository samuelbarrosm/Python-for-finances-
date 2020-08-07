#Nesse codigo calcularemos o valor de beta
#O beta mostra ate que ponto a mudança no preco de um ativo esta relacionado com o desempenho global do mercado
#O beta é a razao entra a covariancia do mercado e o ativo, pela variancia

import numpy as  np 
import pandas as pd 
import matplotlib.pyplot as plt 
from pandas_datareader import data as wb

data = pd.DataFrame() 

tickers = ['PG', '^GSPC']

for t in tickers:
    data[t] = wb.DataReader(t, data_source='yahoo', start='2012-1-1', end='2016-12-31')['Adj Close']

#Aqui estamos calculando a taxa de retorno logaritmica

sec_returns = np.log(data / data.shift(1))

#Aqui estamos calculando a covariancia entre o ativo e o mercado

cov = sec_returns['PG'].cov(sec_returns['^GSPC']) * 250

#O comando iloc nos permite um obter os valores em formato de floats


#Aqui estamos calculando a variancia anualizada do GSPC ou seja variancia do mercado 

market_var = sec_returns['^GSPC'].var() * 250

#Para calcularo beta, basta somente dividi-los 

PG_beta = cov / market_var

#O valor estara compreendido entre 0 e 2
#Menor que 1 acao defensiva
#Maior que 1 acao agressiva 

#OBS: diferentes bancos de dados devem apresentar uma variacao de no maximo 3% do valor

#Agora iremos fazer a precipitacao da taxa de retorno da PG
#Sabemos que a taxa de retorno esperada de um ativo segue a formula
#Taxa esperada = taxa de retorno livre de risco + betaPG * (retorno do mercado - retorno livre de risco)
#O retorno de mercado - retorno livre de risco é chamado de premio
#O premio de risco é medido baseado no premio que o investidor esta disposto a suportar num ativo

PG_er = 0.025 + PG_beta * 0.05

#O valor 0.025 é o retorno livre de risco que pode ser encontrado no site da Bloomberg sessao market
#Procura os ultimos 10 anos, e la tera o retorno livre de risco do mercado dos EUA
#Pesquisas recentes afirmam que 5% é um otimo valor para o premio de risco

print(str(round(PG_er * 100, 5)) +  '%')


#Vamos agora calcular o indice de sharpe
#Indice o qual tem como objetivo calcular uma melhor relacao para o investidor entre retorno-risco
#O indice de sharpe é calculado como a subtracao entre retorno esperado da acao e retorno livre de risco / desvio padrao da acao
#O desvio padrao é o desvio anualizado

Sharpe = (PG_er - 0.025) / (sec_returns['PG'].std() * 250 ** 0.5)