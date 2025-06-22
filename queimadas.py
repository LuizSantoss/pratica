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

for estado in df_tratado["Estado"].unique():
    dados_estado = df_tratado[df_tratado["Estado"] == estado]
    plt.plot(dados_estado["Ano"], dados_estado["Porcentagem_Queimadas"], marker='o', label=estado)

plt.title("Porcentagem de Queiamadas no Brasil ")
plt.xlabel("Ano")
plt.ylabel("Porcentagem de Queimadas")
plt.legend(title="Estado")
plt.grid(True)
plt.tight_layout()
plt.show()