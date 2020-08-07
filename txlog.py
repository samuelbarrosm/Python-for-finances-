import numpy as np
#A biblioteca numpy oferece a possibilidade de computaçao vetorizada
#Vetorizaçao é a capacidade de organizar varios tipos de tarefas de processamento de dados como expressoes de uma array
from pandas_datareader import data as wb
import matplotlib.pyplot as plt 

PG = wb.DataReader('PG', data_source='yahoo', start='1995-1-1')

#Aqui estamos utilizando a funçao np.log para calcular o log desejado
PG['log_return'] = np.log(PG['Adj Close'] / PG['Adj Close'].shift(1))

#Aqui estamos plotando os dados obtidos no grafico e os mostrando
PG['log_return'].plot(figsize=(8, 5))
plt.show()

#Aqui estamos mostrando a media anual das taxas logaritmicas de retorno
avg_return = PG['log_return'].mean() * 250

print(str(round(avg_return, 5) * 100) + '%')
