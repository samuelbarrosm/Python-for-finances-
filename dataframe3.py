#Carregando dados
#Importando os dados por quandl
#Apos criar o objeto o que vai dentro do parenteses é a acao em estudo

import quandl

mydata = quandl.get('FRED/GDP')
print(mydata.tail())


