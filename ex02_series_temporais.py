!kaggle datasets download -d saadaliyaseen/climate-and-atmospheric-conditions-data
!unzip climate-and-atmospheric-conditions-data.zip

###Exercício 2 (Série temporal com Climate dataset)

!pip install -q statsmodels
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

df_clima= pd.read_csv("Project 1 - Weather Dataset.csv")
print("Colunas disponíveis:", df_clima.columns.tolist())
print("\nPrimeiras linhas do dataset:")
display(df_clima.head())

df_clima['Date/Time'] = pd.to_datetime(df_clima['Date/Time'])
df_clima = df_clima.set_index('Date/Time')

variavel = "Temp_C"

ts_data = df_clima['Temp_C']

print("\nDados da Série Temporal (Amostra):")
print(ts_data.head())
print(f"Período da Série: {ts_data.index.min()} a {ts_data.index.max()}")

plt.figure(figsize=(12,3))
plt.plot(ts.index, ts.values)
plt.title("Série temporal - Temperatura")
plt.xlabel("Data")
plt.ylabel("Temperatura")
plt.show()

print("n registros:", len(ts))
print("first:", ts.index.min(), "last:", ts.index.max())
freq = pd.infer_freq(ts_data.index)
print("freq inferida:", freq)

period = 24
if len(ts) < 2*period:
    print("Atenção: série pode ser curta para decomposição com esse period. Ajuste o period.")
decomp = seasonal_decompose(ts, model='additive', period=period)

plt.figure(figsize=(12,3)); plt.plot(decomp.trend); plt.title("Tendência"); plt.show()
plt.figure(figsize=(12,3)); plt.plot(decomp.seasonal); plt.title("Sazonalidade"); plt.show()
plt.figure(figsize=(12,3)); plt.plot(decomp.resid); plt.title("Resíduo"); plt.show()

df_clima_temp = df_clima.copy()
df_clima_temp['Hour'] = df_clima_temp.index.hour # Extrai a hora (0 a 23)

plt.figure(figsize=(14, 6))
# Plotando a temperatura pela hora do dia
sns.boxplot(x='Hour', y=variavel, data=df_clima_temp, palette='coolwarm')
plt.title('Distribuição da Temperatura por Hora do Dia (Sazonalidade Diária)', fontsize=16)
plt.xlabel('Hora do Dia (0 a 23)', fontsize=12)
plt.ylabel('Temperatura (°C)', fontsize=12)
plt.show()

# (Rolling Mean)
# Janela de 24 horas (1 dia) para suavizar a sazonalidade diária
rolling_window = 24
ts_rolling_mean = ts_data.rolling(window=rolling_window).mean()

plt.figure(figsize=(14, 4))
plt.plot(ts_data, label='Série Original', alpha=0.5, color='gray')
plt.plot(ts_rolling_mean, label=f'Média Móvel de {rolling_window} Horas', color='red', linewidth=2)
plt.title('Temperatura: Série Original vs. Média Móvel (Tendência)', fontsize=16)
plt.xlabel('Data/Hora', fontsize=12)
plt.ylabel('Temperatura (°C)', fontsize=12)
plt.legend()
plt.show()

"""#Interpretação dos resultados:
1. Há uma tendência clara (crescente ou decrescente)?
###### Analisando a linha de Tendência da Decomposição e a Média Móvel de 24 horas, observa-se que, no longo prazo, a série é relativamente estacionária ou flutua em torno de uma média.

###### Pode haver tendências de curto ou médio prazo (por exemplo, um aumento gradual da temperatura durante a transição de estações), mas não há uma tendência linear clara de crescimento ou queda acentuada ao longo de todo o período registrado.

2. Existe algum padrão sazonal?

###### Sim, um padrão sazonal forte é evidente.

###### O gráfico de Sazonalidade da Decomposição mostra um ciclo de picos e vales muito regular que se repete a cada 24 horas. A temperatura sobe e desce diariamente.

###### O Boxplot por Hora do Dia confirma isso: as caixas de distribuição da temperatura são mais baixas nas primeiras horas do dia (0h-6h) e atingem seu pico no meio da tarde (geralmente entre 13h e 17h).

3. Você encontrou anomalias/outliers?
###### Sim. O gráfico de Resíduo (Ruído) mostra os pontos que a Tendência e a Sazonalidade não conseguiram explicar. Se a linha de resíduo tiver picos ou vales muito distantes de zero, eles representam dias ou horas em que a temperatura foi excepcionalmente diferente do esperado.
###### Os Boxplots Horários também indicam outliers (pontos isolados acima ou abaixo das hastes), representando medições de temperatura que foram atipicamente altas ou baixas para aquela hora do dia.
"""