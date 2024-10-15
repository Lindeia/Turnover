import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('C:/Users/karol/Documents/Analise de Dados/turnover.csv', sep= ",", encoding='ISO-8859-1')

colunas = ['gender', 'age', 'industry', 'profession', 'way', 'extraversion', 'independ', 'selfcontrol', 'anxiety','novator']  
dados_filtrados = dados[colunas]
pd.set_option('display.max_rows', None)

print(dados_filtrados.shape)
print(dados_filtrados)




'''for col in ['gender', 'industry', 'profession', 'way']:
    dados_filtrados[col] = dados_filtrados[col].str.strip().str.lower()


for col in ['age', 'extraversion', 'independ', 'selfcontrol', 'anxiety', 'novator']:
    dados_filtrados[col] = pd.to_numeric(dados_filtrados[col], errors='coerce').fillna(0)


dados_filtrados['gender'] = dados_filtrados['gender'].str.strip().str.lower()
dados_filtrados['industry'] = dados_filtrados['industry'].str.strip().str.lower()
dados_filtrados['profession'] = dados_filtrados['profession'].str.strip().str.lower()
dados_filtrados['way'] = dados_filtrados['way'].str.strip().str.lower()



print(dados_filtrados.isnull().sum())


contagens = {
    'Gênero': dados_filtrados['gender'].value_counts(),
    'Idade': dados_filtrados['age'].value_counts(),
    'Indústria': dados_filtrados['industry'].value_counts(),
    'Profissão': dados_filtrados['profession'].value_counts(),
    'Transporte': dados_filtrados['way'].value_counts(),
    'Extroversão': dados_filtrados['extraversion'].value_counts(),
    'Independência': dados_filtrados['independ'].value_counts(),
    'Autocontrole': dados_filtrados['selfcontrol'].value_counts(),
    'Ansiedade': dados_filtrados['anxiety'].value_counts(),
    'Novato': dados_filtrados['novator'].value_counts()
}

df_contagens = pd.DataFrame(contagens).fillna(0)


df_contagens.plot(kind='bar', figsize=(14, 8), colormap='tab10', alpha=0.8)
plt.title('Distribuição de Características dos Funcionários')
plt.xlabel('Características')
plt.ylabel('Contagem')
plt.xticks(rotation=45)
plt.legend(title='Valores')
plt.tight_layout()
plt.show()
'''
