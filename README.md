# Análise Exploratória de Dados (AED) em Python e Séries Temporais

Este repositório contém os códigos e resultados de dois exercícios práticos de Análise Exploratória de Dados (AED) usando a linguagem Python, com foco em estatísticas descritivas, visualização de distribuição e análise de séries temporais.

## 📁 Datasets Utilizados

Para esta atividade, foram utilizados dois conjuntos de dados principais, com seus respectivos links no Kaggle:

| Exercício | Nome do Dataset | Tipo de Análise | Link para o Dataset |
| :---: | :--- | :--- | :--- |
| **01** | **Diabetes Health Indicators Dataset** | Análise Univariada | [Acessar no Kaggle](https://www.kaggle.com/datasets/mohankrishnathalla/diabetes-health-indicators-dataset) |
| **02** | **Climate and Atmospheric Conditions Data** | Séries Temporais | [Acessar no Kaggle](https://www.kaggle.com/datasets/saadaliyaseen/climate-and-atmospheric-conditions-data) |

---

## 🎯 Estrutura e Conteúdo dos Exercícios

### Exercício 1: Análise Univariada e Estatísticas Descritivas

**Objetivo:** Explorar a distribuição, tendência central e dispersão da variável **`Age`** (faixas etárias) no contexto do dataset de diabetes.

**Atividades Realizadas:**

1.  **Cálculo de Estatísticas:** Média, Mediana, Moda, Variância e Desvio Padrão.
2.  **Visualização da Distribuição:** Geração de um **Histograma** para verificar a forma da distribuição (simetria, assimetria).
3.  **Análise de Outliers:** Geração de um **Boxplot** e cálculo do Intervalo Interquartil (IQR) para identificar a ausência de valores atípicos.
4.  **Conclusão:** A distribuição da idade foi classificada como **simétrica**, e não foram encontrados *outliers*.

### Exercício 2: Visualização e Decomposição de Séries Temporais

**Objetivo:** Analisar os padrões de tendência e sazonalidade nos dados horários de temperatura.

**Atividades Realizadas:**

1.  **Pré-processamento:** Conversão da coluna de data/hora (`Date/Time`) para o formato `datetime` e definição como índice.
2.  **Visualização Inicial:** Plotagem da série temporal de **`Temp_C`** para identificar visualmente tendências e picos.
3.  **Análise de Tendência:** Utilização da **Média Móvel de 24 horas** para suavizar o ruído.
4.  **Análise de Sazonalidade:**
    * **Decomposição Sazonal:** Separação da série nos componentes de Tendência, Sazonalidade e Resíduo (Ruído), usando um período de **24 horas** (ciclo diário).
    * **Boxplots Sazonais:** Geração de *boxplots* da temperatura por **Hora do Dia** para confirmar o forte padrão sazonal diário.
