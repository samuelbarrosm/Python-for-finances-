#Carregando dados
#Importando os dados por quandl
#Apos criar o objeto o que vai dentro do parenteses é a acao em estudo

import quandl

mydata = quandl.get('FRED/GDP')


#Usando o formato csv, podemos salvar os dados obtidos no quandl num arquivo csv
#Podemos fazer isso usando a biblioteca do pandas
#Dentro dos parenteses coloca-se o diretorio onde voce criar o arquivo
#Deve-se indicar o nome_do_arquivo.csv

import pandas as pd

mydata.to_csv('C:/Users/Vanessa Barros/Desktop/edx/example01.csv')

#Se quisermos ler um arquivo do dataframe em um arquivo csv 
#Deve-se indicar o diretorio do arquivo da mesma forma do exemplo anterior
#Nome_do_diretorio.csv

mydata01 = pd.read_csv('C:/Users/Vanessa Barros/Desktop/edx/example01.csv')



#Se quiser alterar o indice da sua planilha pode-se usar o comando index_col()
#mydata01 = pd.read_csv('C:/Users/Vanessa Barros/Desktop/edx/example01.csv', index_col='Date')
#Isso serve para qualquer parametro que voce quer que seja o indice




#Se quisermos salvar um arquivo do dataframe em uma planilha do excel seguimos o mesmo exemplo
#Dentro do parenteses deve-se indicar o diretorio onde ira salvar 
#Nome_do_diretorio.xlsx

mydata01.to_excel('C:/Users/Vanessa Barros/Desktop/edx/example01.xlsx')


#Se quisermos ler um arquivo do dataframe em um arquivo excel 
#Deve-se indicar o diretorio do arquivo da mesma forma do exemplo anterior
#Nome_do_diretorio.xlsx

mydata02 = pd.read_excel('C:/Users/Vanessa Barros/Desktop/edx/example01.xlsx')


#Possuindo uma planilha qualquer no python
#Podemos alterar o indice com o .set_index()
#Ex: mydata03, para alterar o indice de mydata03
#mydata03.set_index(nome_do_que_quer_alterar)
#Apos assim isso reescreve
#mydata03 = mydata03.set_index(nome_do_que_quer_alterar)





#TROCAR O INDICE, É TIRAR A LEITURA DE INTEIROS E COLOCAR UM LEITURA TEMPORAL

