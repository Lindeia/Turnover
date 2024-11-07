import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

dados = pd.read_csv('C:/Users/karol/Documents/Analise de Dados/turnover.csv', sep=",", encoding='ISO-8859-1')
colunas = ['gender', 'age', 'industry', 'profession', 'way', 'extraversion', 'independ', 'selfcontrol', 'anxiety', 'novator']  
dados_filtrados = dados[colunas]
dados_filtrados = dados_filtrados.dropna()

pd.set_option('display.max_rows', 1129)
print(dados_filtrados.shape)
print(dados_filtrados)

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

print(Idade, Extroversão, Indústria, Transporte, Independência, Ansiedade, Novato, Genero)

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


total_entradas = dados.shape[0]
media_idade = dados['age'].mean()
media_extraversion = dados['extraversion'].mean()
media_independencia = dados['independ'].mean()
media_autocontrole = dados['selfcontrol'].mean()
media_ansiedade = dados['anxiety'].mean()
media_inovacao = dados['novator'].mean()

genero_counts = dados['gender'].value_counts()
masculino = genero_counts.get('m', 0)
feminino = genero_counts.get('f', 0)


industria_analise = dados.groupby('industry').agg({
    'anxiety': ['mean', 'std'],
    'selfcontrol': ['mean', 'std'],
    'extraversion': ['mean', 'std'],
    'independ': ['mean', 'std']
}).reset_index()


industria_analise.columns = [
    'Indústria', 
    'Média de Ansiedade', 'Desvio Padrão Ansiedade',
    'Média de Autocontrole', 'Desvio Padrão Autocontrole',
    'Média de Extroversão', 'Desvio Padrão Extroversão',
    'Média de Independência', 'Desvio Padrão Independência'
]

X = dados[['age', 'extraversion', 'independ', 'selfcontrol', 'novator']]
y = dados['anxiety']

model = LinearRegression()
model.fit(X, y)
predictions = model.predict(X)
mse = mean_squared_error(y, predictions)
r2 = r2_score(y, predictions)

regressao_resultados = {
    'Ansiedade': (mse, r2),
}


print("Resultados da Análise de Dados")
print(f"Total de Entradas: {total_entradas}")
print("Variáveis:")
print(f"Gênero: Masculino: {masculino}, Feminino: {feminino}")
print(f"Idade: Média de {media_idade:.1f} anos")
print(f"Extraversion: Média de {media_extraversion:.2f}")
print(f"Independência: Média de {media_independencia:.2f}")
print(f"Autocontrole: Média de {media_autocontrole:.2f}")
print(f"Ansiedade: Média de {media_ansiedade:.2f}")
print(f"Inovação: Média de {media_inovacao:.2f}")

print("\nResultados da Regressão")
for var, (mse, r2) in regressao_resultados.items():
    print(f"{var}\nMean Squared Error: {mse:.2f}\nR² Score: {r2:.2f}")

print("\nEstatísticas Descritivas por Indústria:")
print(industria_analise)
