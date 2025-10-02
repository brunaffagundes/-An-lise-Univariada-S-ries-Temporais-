!pip install -q kaggle
from google.colab import files
files.upload()

!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

!kaggle datasets download -d mohankrishnathalla/diabetes-health-indicators-dataset

!ls -la /content

!unzip diabetes-health-indicators-dataset.zip

###Exercício 1: Análise Univariada com Histogramas e Boxplots"""

!pip install -q scipy statsmodels
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

import pandas as pd

df_diabetes = pd.read_csv("diabetes_dataset.csv")

print(df_diabetes.shape)
display(df_diabetes.head())
display(df_diabetes.info())

var = 'age'
s = df_diabetes[var].dropna()

idade = df_diabetes['age']

media = idade.mean()
mediana = idade.median()
moda = idade.mode()[0]
variancia = idade.var()
desvio_padrao = idade.std()

print("Estatísticas - Idade")
print(f"Média: {media:.2f}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
print(f"Variância: {variancia:.2f}")
print(f"Desvio Padrão: {desvio_padrao:.2f}")

plt.figure(figsize=(10, 5))
sns.histplot(idade, bins=13, kde=True, color='skyblue')
plt.axvline(media, color='red', linestyle='--', linewidth=1.5, label=f'Média ({media:.2f})')
plt.axvline(mediana, color='green', linestyle='-', linewidth=1.5, label=f'Mediana ({mediana:.0f})')
plt.title("Distribuição da Variável Age (Faixas Etárias)", fontsize=16)
plt.xlabel("Faixa de Idade (1=18-24 ... 13=80+)", fontsize=12)
plt.ylabel("Frequência", fontsize=12)
plt.legend()
plt.show()

plt.figure(figsize=(10, 2))
sns.boxplot(x=idade, color='lightcoral')
plt.title("Boxplot da Variável Age (Faixas Etárias)", fontsize=16)
plt.xlabel("Faixa de Idade", fontsize=12)
plt.show()

Q1 = idade.quantile(0.25)
Q3 = idade.quantile(0.75)
IQR = Q3 - Q1
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

outliers_detectados = idade[
    (idade < limite_inferior) | (idade > limite_superior)
]

print(f"\nNúmero de Outliers detectados: {len(outliers_detectados)}")
print(f"Limite Inferior (Outliers abaixo de): {limite_inferior:.1f}")
print(f"Limite Superior (Outliers acima de): {limite_superior:.1f}")

"""#Interpretação dos resultados:
1. O histograma mostra uma distribuição simétrica, enviesada à
esquerda/direita, ou multimodal?  
###### O histograma mostra uma distribuição que é quase perfeitamente simétrica, ou no máximo, ligeiramente enviesada à direita (assimetria positiva).

###### Média e Mediana: A Média (50.12) é quase idêntica à Mediana (50.0). Em uma distribuição perfeitamente simétrica, a Média é igual à Mediana. A diferença mínima aqui sugere uma simetria muito alta.

###### Forma da Curva (KDE): A curva de densidade (linha azul sobre as barras) se assemelha muito a uma curva normal, com o pico centralizado em torno de 50 anos e as caudas diminuindo de forma equilibrada para ambos os lados.

###### Visualização: O pico mais alto (a Moda, próxima a 52 anos) está bem no centro da distribuição, e a dispersão das barras parece equilibrada à esquerda e à direita.

2. O boxplot indica presença de outliers? Eles fazem sentido no contexto dos
dados?

###### Não, o Boxplot e as estatísticas confirmam a ausência de outliers.

###### No gráfico, não há pontos isolados (os asteriscos ou círculos) além das hastes (whiskers). As hastes se estendem até os limites mínimo e máximo dos dados.

###### O cálculo de outliers confirmou: "Número de Outliers detectados: 0".

###### A ausência de outliers faz total sentido. O cálculo definiu um Limite Inferior (6.0) e um Limite Superior (94.0). Como a variável representa idades humanas, e o dataset geralmente inclui idades entre 18 e 80+ anos (faixas 1 a 13), não há valores que estejam "fora do normal" para a população estudada. A ausência de outliers indica que o conjunto de dados é limpo e não contém idades impossíveis ou erros de registro extremos.
