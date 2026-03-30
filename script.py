import pandas as pd

# 1. Carregar o arquivo
# O delimitador é ';' e configuramos o separador decimal e de milhar
df = pd.read_csv('salario_prof.csv', sep=';', decimal=',', thousands='.')

# Limpeza básica de nomes de colunas (remover espaços extras)
df.columns = df.columns.str.strip()

# --- ANÁLISES GERAIS ---

# Estado com menor e maior salário
menor_salario = df.loc[df['Salário inicial'].idxmin()]
maior_salario = df.loc[df['Salário inicial'].idxmax()]

# Posição de Goiás (Ordenando do maior para o menor)
df_ordenado = df.sort_values(by='Salário inicial', ascending=False).reset_index(drop=True)
posicao_go = df_ordenado[df_ordenado['UF'].str.strip() == 'GO'].index[0] + 1

# Média salarial geral
media_geral = df['Salário inicial'].mean()

# --- ANÁLISES POR REGIÃO ---

# Agrupamento para médias, máximos e mínimos por região
agrupado_regiao = df.groupby('Região')['Salário inicial'].agg(['mean', 'max', 'min'])

# Região com maior e menor média salarial
regiao_maior_media = agrupado_regiao['mean'].idxmax()
regiao_menor_media = agrupado_regiao['mean'].idxmin()

# --- EXIBIÇÃO DOS RESULTADOS ---

print(f"1. Estado com MENOR salário: {menor_salario['UF']} (R$ {menor_salario['Salário inicial']:.2f})")
print(f"2. Estado com MAIOR salário: {maior_salario['UF']} (R$ {maior_salario['Salário inicial']:.2f})")
print(f"3. Posição de Goiás (GO) no ranking nacional: {posicao_go}º lugar")
print(f"4. Média salarial nacional: R$ {media_geral:.2f}")

print("\n--- Estatísticas por Região ---")
print(agrupado_regiao.rename(columns={'mean': 'Média', 'max': 'Maior Salário', 'min': 'Menor Salário'}))

print(f"\n5. Região com MAIOR média salarial: {regiao_maior_media} (R$ {agrupado_regiao.loc[regiao_maior_media, 'mean']:.2f})")
print(f"6. Região com MENOR média salarial: {regiao_menor_media} (R$ {agrupado_regiao.loc[regiao_menor_media, 'mean']:.2f})")