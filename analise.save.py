import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar o arquivo CSV do diretório
file_path = "/home/luiz/Downloads/Projetos One/Analise de comportamento/dataset_clientes_final.csv"
dataset = pd.read_csv(file_path)

# Distribuição por gênero
sns.countplot(x='Gênero', data=dataset)
plt.title("Distribuição por Gênero")
plt.savefig("/home/luiz/Downloads/Projetos One/Analise de comportamento/grafico_genero.png")
plt.close()

# Faixa etária
plt.hist(dataset['Idade'], bins=10, color='skyblue', edgecolor='black')
plt.title("Distribuição de Idades")
plt.xlabel("Idade")
plt.ylabel("Frequência")
plt.savefig("/home/luiz/Downloads/Projetos One/Analise de comportamento/grafico_idade.png")
plt.close()

# Métodos de pagamento
sns.countplot(x='Pagamento', data=dataset)
plt.title("Distribuição de Métodos de Pagamento")
plt.savefig("/home/luiz/Downloads/Projetos One/Analise de comportamento/grafico_pagamento.png")
plt.close()

# Produtos mais vendidos
produtos_dist = dataset['Produto'].value_counts()
sns.barplot(x=produtos_dist.head(10).index, y=produtos_dist.head(10).values)
plt.title("Top 10 Produtos mais Vendidos")
plt.xticks(rotation=45)
plt.savefig("/home/luiz/Downloads/Projetos One/Analise de comportamento/grafico_produtos.png")
plt.close()
