import pandas as pd
import matplotlib.pyplot as plt

#salvando dados da tabela
dados = pd.read_csv("placement.csv")

#removendo linhas com salários vazios
dados_sem_salarios = dados.dropna(subset="salary")

#gráfico de distribuição de salários por especialização
dados_sem_salarios.groupby("specialization")["salary"].mean().plot(kind="bar", color="teal")
plt.title('Salário Médio por Especialização')
plt.ylabel('Salário (R$)')
plt.xlabel('Especialização')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
