import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt 

PG = wb.DataReader('PG', data_source='yahoo', start='1995-1-1')
#Para se calcular a taxa de retorno deve-se calcular 
#Usando os dados utilizados, a taxa simples de retorno sera a diferença do seu preço no dia um menos seu preço no dia 0 dividido pelo preço no dia 0
#Quando falamos de preço, estamos falando no preço de fechamento ajustado, reflete o pagamento de vididendo ou desmambramento de açoes
# P1/P0 - 1
#Dentro dos colchetes esta o nome da nova coluna que iremos criar
PG['simple_return'] = (PG['Adj Close'] / PG['Adj Close'].shift(1)) - 1
print(PG['simple_return'])


#A função shift determina o numero de dias anteriores que queremos trabalhar 
#O numero de dias é determinado pelo parametro da funçao, .shift(num)

