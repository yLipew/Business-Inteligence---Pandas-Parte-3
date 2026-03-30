# Análise de Salários Estaduais (Professores) 📊

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)

## 🎯 Objetivo Acadêmico
Este projeto foi desenvolvido como parte integrante dos estudos em **Inteligência Artificial e Business Intelligence**. O objetivo principal é exercitar a manipulação de grandes volumes de dados (ETL), aplicando técnicas de limpeza, conversão de tipos monetários e extração de métricas estatísticas para suporte à tomada de decisão.

## 🚀 Funcionalidades e Templates

O script realiza o processamento de uma base de dados governamental/educacional para extrair os seguintes insights:

### 1. Extremos Nacionais
Identifica os estados com o maior e o menor piso salarial nacional, apresentando a UF e o valor formatado.

### 2. Ranking e Localização (Goiás)
Gera um ranking ordenado (do maior para o menor) para situar a posição exata do estado de Goiás (GO) frente às demais unidades federativas.

### 3. Estatísticas por Região
Agrupamento inteligente de dados (GroupBy) para exibir:
* Média salarial por região geográfica.
* O maior e o menor salário registrado em cada região.

### 4. Comparativo de Médias Regionais
Determina as regiões com os maiores e menores desempenhos salariais médios do país.

## 📂 Estrutura de Arquivos

* `salario_prof.csv`: Base de dados (delimitada por `;`, com padrão decimal `,` e milhar `.`).
* `script.py`: Implementação lógica utilizando a biblioteca Pandas.

## 📊 Exemplo de Processamento
O script garante a integridade dos dados ao remover espaços em branco e tratar caracteres especiais de moeda:

| UF | Salário Inicial | Região |
|---|---|---|
| MS | 13.007,12 | Centro-Oeste |
| GO | 5.160,49 | Centro-Oeste |

---

## 👨‍💻 Autor

**Felipe Mendonça** *Inteligência Artificial / Business Intelligence* **FATESG / SENAI** 2026
