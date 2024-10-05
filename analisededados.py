# Importando a biblioteca pandas
import pandas as pd

# Lendo o arquivo CSV
df = pd.read_csv('C:/Users/karol/Documents/Analise de Dados/turnover.csv', encoding='ISO-8859-1')


# Exibindo as primeiras linhas do dataframe
print(df.head())

# Verificando informações gerais dos dados (tipo de dados, valores nulos, etc.)
print(df.info())

# Estatísticas descritivas das colunas numéricas
print(df.describe())

# Verificando se há valores nulos
print(df.isnull().sum())
