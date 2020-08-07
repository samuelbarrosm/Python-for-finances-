#Nosso objetivo é executar as regressoes multivariadas 

import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 
from scipy import stats
import statsmodels.api as sm 

#Aqui vamos abrir o banco de dados em estudo, pode ser um arquivo do excel..
data = pd.read_excel('DIRETORIO')

#Vamo supor que estamos olhando uma tabela de preco de casas
#numero de quartos, ano de construcao, e tamanho, sao variaveis.
#Lembre-se de nomear cada uma delas
#Vamos analisar se essas variaveis afetam o valor da casa

#Usaremos os parenteses dobrados para mostrar que o x sera multidimensional
X = data[['House Size (sq.ft.)', 'Number of Rooms', 'Yeah of Construction']]
Y = data['House Price']

#Com a ajuda das mesmas variaveis vamos usar uma regressao de minimos quad.
X1 = sm.add_constant(X)
reg = sm.OLS(Y,X1).fit() 

#Rodando o codigo vamos analisar as estatisticas obtidas
#Podemos analisar a const. e ver se variou muito antes de adcionar a variavel
#Se a variaçao aparentemente for ruim, deve-se olhar o R quadrado
#Analisando o R quadrado pode-se avaliar se é mais explicativo ou nao
#Se for mais explicativo significa que pelo menos uma variavel é utilizavel

#Um bom investidor ele ira fazer diversas regressoes para avaliar a melhor possibilidade
#Ou seja, uma melhor combinacao de variaveis que satisfaça a predicao de valores

#So repetir o mesmo processo alterando as variaveis