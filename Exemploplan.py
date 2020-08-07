#Objetivo do codigo
#Utilizar a biblioteca do quandl para obter dados
#Criar um arquivo do excel com esses dados
#Abrir os arquivos do excel

import quandl
import pandas as pd 

mydata = quandl.get('FRED/GDB')
mydata.head()
mydata.tail()

mydata.to_excel('C:/Users/Vanessa Barros/Desktop/edx/planilha1.xlsx')

mydata01 = pd.read_excel('C:/Users/Vanessa Barros/Desktop/edx/planilha1.xlsx')
