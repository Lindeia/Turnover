# Importa bibliotecas
import pandas as pd
import matplotlib.pyplot as plt

# Le o arquivo CSV
df = pd.read_csv('C:/Users/karol/Documents/Analise de Dados/turnover.csv', encoding='ISO-8859-1')


# Exibe as primeiras linhas do dataframe
print(df.head())

# Verifica informações gerais dos dados (tipo de dados, valores nulos, etc.)
print(df.info())

# Estatísticas descritivas das colunas numéricas
print(df.describe())

# Verifica se há valores nulos
print(df.isnull().sum())
