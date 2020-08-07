import numpy as np
import pandas as pd
from pandas_datareader import data as wb
from pandas.util.testing import assert_frame_equal


#O objetivo aqui é extrair dados por ex da yahoo finance
#Voce determina a empresa
#Voce determina o periodo
#O primeiro parametro é o simbolo da ação da empresa avaliada(ticker)
#O segundo parametro é determinar a sua fonte de dados
#O terceiro parametro é determinar a data de inicio

df = pd.DataFrame()
acao = 'AAPL'

df = wb.DataReader(acao, data_source='yahoo', start='01-01-2000')

#DataReader tem como objetivo extrair os dados da web e anexar no python

print(df)

#Mosta que estamos analisando um objeto dataframe, pode ver quantas entradas de dados existem e o intervalo deles.
df.info()

#Pode-se se usar as primeiras e ultimas 5 linhas da sua analise de dados, porem se quer checar um num especifico df.tail(numero)
df.tail()
df.head()

