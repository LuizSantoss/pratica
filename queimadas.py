import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("queimadas.csv")
print(df['Porcentagem_Queimadas'].mean())

