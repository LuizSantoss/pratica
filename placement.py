import pandas as pd
import matplotlib.pyplot as plt

#salvando dados da tabela
dados = pd.read_csv("placement.csv")

#removendo linhas com salários vazios
dados_sem_salarios = dados.dropna(subset="salary")

#gráfico de distribuição de salários por especialização
plt.figure(figsize=(7,5))
dados_sem_salarios.groupby("specialisation")["salary"].mean().plot(kind="bar", color="teal")
plt.title('Salário Médio por Especialização')
plt.ylabel('Salário (R$)')
plt.xlabel('Especialização')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#gráfico de colocação por gênero 
plt.figure(figsize=(6,5))
placement_por_genero = dados.groupby(["gender", "status"]).size().unstack()
(placement_por_genero.div(placement_por_genero.sum(axis=1), axis=0) * 100).plot(kind="bar", stacked=True, colormap='Pastel1')
plt.title('Taxa de Colocação por Gênero (%)')
plt.ylabel('Percentual')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

#gráfico de relação de MBA e salarios
plt.figure(figsize=(7, 5))
plt.scatter(dados_sem_salarios['mba_p'], dados_sem_salarios['salary'], alpha=0.6, color='purple')
plt.title('Correlação entre Nota MBA e Salário')
plt.xlabel('Nota no MBA')
plt.ylabel('Salário (R$)')
plt.grid(True)
plt.tight_layout()
plt.show()