import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('C:/Users/karol/Documents/Analise de Dados/turnover.csv', sep= ",", encoding='ISO-8859-1')

colunas = ['gender', 'age', 'industry', 'profession', 'way', 'extraversion', 'independ', 'selfcontrol', 'anxiety','novator']  
dados_filtrados = dados[colunas]
pd.set_option('display.max_rows', None)

print(dados_filtrados.shape)
print(dados_filtrados)

Genero = dados_filtrados ['gender'].value_counts().sort_index()
Idade = dados_filtrados['age'].value_counts().sort_index()
Indústria = dados_filtrados['industry'].value_counts().sort_index()
Profissão = dados_filtrados['profession'].value_counts().sort_index()
Transporte = dados_filtrados['way'].value_counts().sort_index()
Extroversão = dados_filtrados['extraversion'].value_counts().sort_index()
Independência = dados_filtrados['independ'].value_counts().sort_index()
Autocontrole = dados_filtrados['selfcontrol'].value_counts().sort_index()
Ansiedade = dados_filtrados['anxiety'].value_counts().sort_index()
Novato = dados_filtrados['novator'].value_counts().sort_index()

print(Idade, Extroversão, Indústria, Transporte, Independência, Ansiedade, Novato, Genero)

dados_filtrados = dados_filtrados.dropna()
print(dados_filtrados.head())

plt.figure(figsize=(10, 4))

plt.hist(dados_filtrados['gender'], bins=20, alpha=0.5, label='Genero', color='cyan')

plt.hist(dados_filtrados['age'], bins=20, alpha=0.5, label='Idade', color='blue')

plt.hist(dados_filtrados['extraversion'], bins=20, alpha=0.5, label='Extroversão', color='orange')

plt.hist(dados_filtrados['industry'], bins=20, alpha=0.5, label='Indústria', color='red')

plt.hist(dados_filtrados['profession'], bins=20, alpha=0.5, label='Profissão', color='brown')

plt.hist(dados_filtrados['way'], bins=20, alpha=0.5, label='Transporte', color='purple')

plt.hist(dados_filtrados['independ'], bins=20, alpha=0.5, label='Indepêndencia', color='green')

plt.hist(dados_filtrados['selfcontrol'], bins=20, alpha=0.5, label='Autocontrole', color='gray')

plt.hist(dados_filtrados['anxiety'], bins=20, alpha=0.5, label='Ansiedade', color='yellow')

plt.hist(dados_filtrados['novator'], bins=20, alpha=0.5, label='Novato', color='Magenta')

plt.title('Histograma de Turnover')
plt.xlabel('Categorias')
plt.ylabel('Contagem')

plt.xticks(ticks=[0, 10, 20, 30, 40, 50, 60], labels=['0', '10', '20', '30', '40', '50', '60'], rotation=45)

plt.legend()

plt.grid(axis='y', alpha=0.75)

plt.show()
