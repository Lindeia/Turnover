import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Carregar e preparar os dados
dados = pd.read_csv('C:/Users/karol/Documents/Analise de Dados/turnover.csv', sep=",", encoding='ISO-8859-1')
colunas = ['gender', 'age', 'industry', 'profession', 'way', 'extraversion', 'independ', 'selfcontrol', 'anxiety', 'novator']  
dados_filtrados = dados[colunas]
dados_filtrados = dados_filtrados.dropna()

# Configuração para exibir todas as linhas
pd.set_option('display.max_rows', 1129)
print(dados_filtrados.shape)
print(dados_filtrados)

# Análise descritiva e contagem de valores para algumas colunas
Genero = dados_filtrados['gender'].value_counts().sort_index()
Idade = dados_filtrados['age'].value_counts().sort_index()
Indústria = dados_filtrados['industry'].value_counts().sort_index()
Profissão = dados_filtrados['profession'].value_counts().sort_index()
Transporte = dados_filtrados['way'].value_counts().sort_index()
Extroversão = dados_filtrados['extraversion'].value_counts().sort_index()
Independência = dados_filtrados['independ'].value_counts().sort_index()
Autocontrole = dados_filtrados['selfcontrol'].value_counts().sort_index()
Ansiedade = dados_filtrados['anxiety'].value_counts().sort_index()
Novato = dados_filtrados['novator'].value_counts().sort_index()

#Exibe as colunas filtradas
print(Idade, Extroversão, Indústria, Transporte, Independência, Ansiedade, Novato, Genero)

# Visualização: Histograma das colunas selecionadas
plt.figure(figsize=(10, 7))

plt.hist(dados_filtrados['gender'], bins=20, alpha=0.5, label='Genero', color='cyan')
plt.hist(dados_filtrados['age'], bins=20, alpha=0.5, label='Idade', color='blue')
plt.hist(dados_filtrados['extraversion'], bins=20, alpha=0.5, label='Extroversão', color='orange')
plt.hist(dados_filtrados['industry'], bins=20, alpha=0.5, label='Indústria', color='red')
plt.hist(dados_filtrados['profession'], bins=20, alpha=0.5, label='Profissão', color='brown')
plt.hist(dados_filtrados['way'], bins=20, alpha=0.5, label='Transporte', color='purple')
plt.hist(dados_filtrados['independ'], bins=20, alpha=0.5, label='Independência', color='green')
plt.hist(dados_filtrados['selfcontrol'], bins=20, alpha=0.5, label='Autocontrole', color='gray')
plt.hist(dados_filtrados['anxiety'], bins=20, alpha=0.5, label='Ansiedade', color='yellow')
plt.hist(dados_filtrados['novator'], bins=20, alpha=0.5, label='Novato', color='magenta')

plt.title('Histograma de Turnover')
plt.xlabel('Categorias')
plt.ylabel('Contagem')
plt.xticks(ticks=[0, 10, 20, 30, 40, 50, 60], labels=['0', '10', '20', '30', '40', '50', '60'], rotation=45)
plt.legend()
plt.grid(axis='y', alpha=0.75)
plt.show()

# Implementação do modelo de Regressão Logística
# Codificar a variável 'profession'
le = LabelEncoder()
y = le.fit_transform(dados_filtrados['profession'])

# Selecionar as variáveis preditoras
X = dados_filtrados[['age', 'extraversion', 'independ', 'selfcontrol', 'anxiety', 'novator']]

# Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Escalar os dados
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Treinar o modelo de regressão logística com mais iterações
model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)

# Fazer previsões e calcular a acurácia
predictions = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, predictions)

print(f'Acurácia do modelo: {accuracy:.2f}')
