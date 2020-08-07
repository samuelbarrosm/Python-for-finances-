#Aqui iremos calcular a covariancia e a correlacao´
#Uma matriz de covariancia, é uma representacao da maneira que duas ou mais variaveis se relacionam entre si
#A covariancia entre uma variavel e ela propria na verdade é a propria variancia dessa mesma variavel
#Ao longo da diagonal principal, tem-se a variancia das mesmas variaveis, e nas restantes posicoes teremos a covariancia entre elas

#Por exemplo, se estivermos analisando duas açoes
#Sera formado uma matriz de segunda ordem, onde na diagonal principal teremos as variancias, e os demais termos as covariancias

#Para calcular a variancia de uma açao, usa-se o comando .var do numpy

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from pandas_datareader import data as wb 

new_data = pd.DataFrame()  

tickers = ['PG', 'BEI.DE']

for t in tickers:
    new_data[t] = wb.DataReader(t, data_source='yahoo', start='2007-1-1')['Adj Close']

sec_returns = np.log(new_data / new_data.shift(1))

#Vamos calcular a variancia das acoes da PG
PG_var = sec_returns['PG'].var()

#Vamos calcular a variancia anual das acoes da PG
PG_var_a = sec_returns['PG'].var() * 250

#Vamos calcular a variancia das acoes da BEI
BEI_var = sec_returns['BEI.DE'].var() 

#Vamos calcular a variancia anual das acoes da BEI
BEI_var_a = sec_returns['BEI.DE'].var() * 250

#É desnecessario nesse estagio criar um dataframe e preenche-lo com esses valores

#O metodo .cov() faz isso automaticamente, calcula a covariancia de pares de colunas

#Calculando a covariancia da matriz 2x2
cov_matrix = sec_returns['PG'].cov(sec_returns['BEI.DE'])

#Calculando a covariancia anual da matriz 2x2
cov_matrix_a = sec_returns['PG'].cov(sec_returns['BEI.DE']) * 250

#Para se calcular a correlaçao, usa-se o metodo .corr()
#Ao longo da diagonal diagonal principal observa-se o valor 1
#Pois divide-se o valor de cada elemento pela sua respectiva variancia
#Ja os elementos das outras diagonais representam a correleçao entre os retornos das empresas
#Quao mais baixo o valor menor a correlaçao entre as duas 
#A correlacao entre empresas iguais deve ser igual
#É diferente a correlaçao de precos para correlacao de retornos
#Corr(retornos) reflete a dependencia entre os precos em diferentes momentos e se concentranos retornos do seu portfolio
#Corr(precos) reflete nos niveis de preco das acoes
#Não se anualiza a tabela de correlacao

corr_matrix = sec_returns['PG'].corr(sec_returns['BEI.DE'])

print(cov_matrix_a)
print(corr_matrix)