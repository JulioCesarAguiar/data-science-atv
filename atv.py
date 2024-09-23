
import pandas as pd

dados = pd.read_csv('c:/Users/Colaborador/Documents/data-science/seguro_de_vida.csv')


# 1. Classificar o tipo e escala de todas as variáveis
tipos_variaveis = dados.dtypes
print("Tipos de variaveis:")
print(tipos_variaveis)

# 2. Verificar se há valores faltantes
missing_values = dados.isnull().sum()
print("\nValores faltantes:")
print(missing_values)

# 3. Medidas descritivas das variáveis numéricas (ajustando para duas casas decimais)
medidas_numericas = dados.describe().round(2)

medidas_numericas = medidas_numericas.rename(index={
    'count': 'Contagem', 
    'mean': 'Media', 
    'std': 'Desvio Padrao', 
    'min': 'Minimo', 
    '25%': '1 Quartil', 
    '50%': 'Mediana', 
    '75%': '3 Quartil', 
    'max': 'Maximo'
})

print("\nMedidas descritivas (numericas):")
print(medidas_numericas)

# 4. Medidas descritivas das variáveis categóricas
medidas_categoricas = dados.describe(include=object)
print("\nMedidas descritivas (categoricas):")
print(medidas_categoricas)

# 5. Número de filhos mais frequente
filhos_mais_frequente = dados['filhos'].mode()[0]
print(f"\nNumero de filhos mais frequente: {filhos_mais_frequente}")

# 6. Percentual de clientes fumantes
percentual_fumantes = (dados['fumante'].value_counts(normalize=True) * 100)['sim']
print(f"\nPercentual de clientes fumantes: {percentual_fumantes:.2f}%")

# 7. Categorias na variável 'regiao' e quantidade de cada uma
categorias_regiao = dados['regiao'].value_counts()
print("\nCategorias de regiao:")
print(categorias_regiao)
