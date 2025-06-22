import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("queimadas.csv")
print(df['Porcentagem_Queimadas'].mean())

#visualizando onde falta dados (True)
print(df.isna())

print("\n\n")

#dados subsituidos pela media
df_tratado = df.fillna(df["Porcentagem_Queimadas"].mean())
print(df_tratado)
