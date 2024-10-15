import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('C:/Users/karol/Documents/Analise de Dados/turnover.csv', sep= ",", encoding='ISO-8859-1') 

colunas = ['gender', 'age', 'industry', 'profession', 'way', 'extraversion', 'independ', 'selfcontrol', 'anxiety','novator']  
dados_filtrados = dados[colunas]
print(dados_filtrados)

contagem = { 
    'genero': dados_filtrados['gender'].value_counts(),
    'idade' : dados_filtrados['age'].value_counts(),
    'Industria' : dados_filtrados['industry'].value_counts()
}

df_contagem = pd.DataFrame(contagem).fillna(0)

plt.figure(figsize=(10, 6))
contagem.plot(kind='bar', color='skyblue')
plt.title('Distribuição de Valores')
plt.xlabel('Gênero')
plt.ylabel('Idade')
plt.ylabel('Industria')
plt.xticks(rotation=0)
plt.show()