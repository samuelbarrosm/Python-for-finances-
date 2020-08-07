#Calculando a regressao dos minimos quadrados ordinarios, tambem chamada de OLS
import pandas as pd 
import numpy as np 

import matplotlib.pyplot as plt 

#API é um sufixo indicando que vamos importar uma grande parte do madulo statsmodels

from scipy import stats 
import statsmodels.api as sm 

#Vamos fazer um exemplo para casas:
#Tamanho, ano de construçao, preço, numero de quartos

#Com esse comando se carrega os dados de uma planlha do excel
data = pd.read_excel('DIRETORIO ONDE SE ENCONTRA.xlsx')

#Vamos primeiro analisar como funcionaria um variavel simples, por exemplo: dependencia do preco da casa com o tamanho
#Para isso usaremos somente uma variavel dependente
#Para isso seria interessante uma tabela com duas colunas
#Digitando o numero das colunas de interesses

data[['House Prince', 'House Size (sq.ft.)']]

#Para efetuar a regressao vamos atribuir o valor de cada coluna com o de uma variavel

x = data['House Size (sq.ft.)']
y = data['House Price']

#O matplotlib nos ajudara a fazdr um grafico
plt.scatter(x,y)


#Esse grafico tera os pontos dispersos no grafico, a cada valor de x, um respectivo y
#O grafico pode enganar a vista e parecer que certas casas sao ridiculamente baratas
#Para ajustar isso podemos usar o comando .axis que consiste em voce determinar os extremos de cada parametro
#Colaca-se valores que sabe-se quenao serao atigindos para tornar o grafico mais 'limpo'

plt.scatter(x,y)
plt.axis([0, 2500, 0, 1500000])

#Ao criar um grafico profissional é necessario rotularos eixos, e para isso podemos fazer 
plt.ylabel('House Price')
plt.xlabel('House Size (sq.ft)')

plt.show()

#Criar uma boa apresentaçao de um grafico é extremamente necessaria e util.