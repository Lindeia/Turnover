import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('C:/Users/karol/Documents/Analise de Dados/turnover.csv', sep= ",", encoding='ISO-8859-1') 

colunas = ['gender', 'age', 'industry', 'profession', 'way', 'extraversion', 'independ', 'selfcontrol', 'anxiety','novator']  
dados_filtrados = dados[colunas]
print(dados_filtrados)
#
genero = dados_filtrados['gender'].value_counts()

#
plt.figure(figsize=(10, 6))
genero.plot(kind='bar', color='skyblue')
plt.title('Distribuição de Gêneros')
plt.xlabel('Gênero')
plt.ylabel('Contagem')
plt.xticks(rotation=0)
plt.show()