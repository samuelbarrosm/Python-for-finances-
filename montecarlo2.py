#Utilizando as simulacoes de monte carlo para projetar despesas e receitas futuras de uma empresa

#1. Prevendo o lucro bruto futuro de uma empresa
#Requisitos: receita esperada, CMV esperado(custo de mercadoria vendida), nos EUA se chamam de COGS


import numpy as np 
import matplotlib.pyplot as plt 

#Aqui seria por exemplo a receita do ano passado da empresa
#Tendo uma ideia da receita esperada

#Aqui temos a receita media
rev_m = 170 
#Aqui o desvio padrao
rev_stdev = 20 
#Aqui o numero de simulaçoes
iterations = 1000

#Usando o gerador aleatorio de distribuiçao do numpy
rev = np.random.normal(rev_m, rev_stdev, iterations)

#Vamos plotar os valores num grafico para fazer avaliaçoes
plt.figure(figsize=(15, 6))
plt.plot(rev)
plt.show() 

#Tendo um conhecimento a cerca da empresa em estudo: Podemos dizer que o CMV é aproximadamente 60% da receita
#Para definir a distribuiçao é necessario varias 10% em torno da media da receita
#CMV é o valor gasto, logo é negativo
#Agora para determinar o CMV estamos atribuindo uma media de 60% na receita e um desvio padrao de 10%
COGS = - (rev * np.random.normal(0.6, 0.1))

plt.figure(figsize=(15, 6))
plt.plot(COGS)
plt.show()

COGS.mean()
COGS.std()

#Nosso objetivo agora é prever o lucro bruto
#Apos gerar mil receitas potenciais e valores possiveis para o cmv, fazemos a combinacao do cmv e receita
#Como geramos o CMV como um numero negativo, atribuiremos o valor de '+' 

Gross_Profit = rev + COGS 

plt.figure(figsize=(15, 6))
plt.plot(Gross_Profit)
plt.show()

#Aqui estamos calculando o valor maximo e minimo possiveis para o lucro bruto a partir das simulacoes
max(Gross_Profit)
min(Gross_Profit)
Gross_Profit.mean() 
Gross_Profit.std()

#Podemos plotar esses resultados num histograma
#É um outro tipo de grafico que ajuda a identificar a distribuicao do resultado
#Funciona como um grafico normal, porem usamos o comando hist, e podemos atribuir diversos parametros
#O 'bins' é relacionado com as classes de frequencia, se refere a como os dados sao agrupados no graficos
#Criando uma lista os elementos serao usados para separar as classes no eixo x
#Classes pequenas nao sao muito usuais pois nao da para visualizar a distribuiçao normal dos dados 

plt.figure(figsize=(10, 6))
plt.hist(Gross_Profit, bins = [40, 50 , 60, 70, 80, 90 , 100, 110, 120])
plt.show()


#Usando agora dessa forma o histograma, montamos o grafico com 20 classe deixando assim claro a visualizacao da distribuiçao normal
plt.figure(figsize=(10, 6))
plt.hist(Gross_Profit, bins = 20)
plt.show()
