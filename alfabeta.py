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

X = data['House Size (sq.ft.)']
Y = data['House Price']

#O matplotlib nos ajudara a fazer um grafico
plt.scatter(X,Y)


#Esse grafico tera os pontos dispersos no grafico, a cada valor de x, um respectivo y
#O grafico pode enganar a vista e parecer que certas casas sao ridiculamente baratas
#Para ajustar isso podemos usar o comando .axis que consiste em voce determinar os extremos de cada parametro
#Colaca-se valores que sabe-se quenao serao atigindos para tornar o grafico mais 'limpo'

plt.scatter(X,Y)
plt.axis([0, 2500, 0, 1500000])

#Ao criar um grafico profissional é necessario rotularos eixos, e para isso podemos fazer 
plt.ylabel('House Price')
plt.xlabel('House Size (sq.ft)')

plt.show()

#Criar uma boa apresentaçao de um grafico é extremamente necessaria e util.

#Vamos agora interpretar algumas estatisticas que podem ser obtidas apos a execucao da regressao
#O modulo statsmodels contem modelos estatiscos, possui ferramentas para executar uma regressao
#Esse procedimento que faremos a seguir necessita que inclua uma constante no modelo

X1 = sm.add_constant(X)

#Na variavel reg atribuiremos o resultado da regressao dos minimos quadrados ordinarios (OLS)
#O metodo fit é um metodo que aplica uma tecnica de estimativa especifica que vai obter o ajuste completo do modelo
 
reg = sm.OLS(Y, X1).fit()

#O comando summary ira mostrar o resultado da regressao e ira organiza-lo em tres tabelas
reg.summary()

#Interpretando as tabelas podemos priorizar alguns resultados importantes

#Primeira tabela
#R-squared é responsavel em dizer a porcentagem que a variavel dependente explica a variavel independente
#Quao maior R-squared, melhor. Acima de 30% é considerado alto

#Segunda tabela(mais importante)
#O python da os resultados em notacao cientifica ex:2608e+05, que pode ser escrito como 260,800
#o valor correspondente a, const x coef é o alfa da nossa equacao de regressao
#(VARIAVEL INDEPENTE(House Size (sq.ft))) x coef, é a estimativa de quanto varia por exemplo o preco por metro quadrado
#O valor acima representa a inclinacao da linha de regressao, ou seja o Beta
#std error x (VARIAVEL INDEPENDENTE(House Size (sq.ft))) representa o quanto pode variar o valor de ganho por m**2,pra cima ou para baixo


#Ao inves de usar a biblitoca statsmodels, podemos encontrar mais faclmente esses valores usando a biblioteca scipy lingregress
slope, intercept, r_value, p_value, std_err = stats.linregress(X,Y)

#slope = beta
#intercept = alfa
#r_value = 
#p_value = 
#std_err = erro padrao

#Esses valores obtidos estao em floats
#OBS: nao se esquecer que para obter o valor de R-squared é necessario elevar (r_value ** 2)