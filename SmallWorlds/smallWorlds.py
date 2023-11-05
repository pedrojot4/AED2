import networkx as nx  # Biblioteca NetworkX para trabalhar com grafos
import matplotlib.pyplot as plt  # Biblioteca Matplotlib para criação de gráficos
import seaborn as sns  # Biblioteca Seaborn para personalização de gráficos

# Criando uma lista vazia para armazenar objetos de grafos
gra = []

# Lendo um grafo a partir do arquivo "facebook.txt" e armazenando-o em 'gra0'
gra0 = nx.read_adjlist("facebook.txt")

# Adicionando 'gra0' à lista 'gra'
gra.append(gra0)

# Calculando a distribuição de graus e grau médio dos vizinhos dos nós no 'gra0'
deg0, average_deg0 = zip(*nx.average_degree_connectivity(gra0).items())
deg0 = list(deg0)
average_deg0 = list(average_deg0)

# Definindo o estilo do gráfico como "fivethirtyeight"
plt.style.use("fivethirtyeight")

# Criando uma figura e um eixo para o gráfico com tamanho personalizado
fig, ax = plt.subplots(1, 1, figsize=(13, 9))

# Criando um gráfico de dispersão com uma linha de regressão
sns.regplot(x=deg0, y=average_deg0, ax=ax)

# Definindo o rótulo do eixo y
ax.set_ylabel("Average neighbor degree")

# Definindo o rótulo do eixo x
ax.set_xlabel("Node Degree")

# Definindo os limites do eixo x para começar a partir de 0
ax.set_xlim(0, None)

# Exibindo o gráfico
plt.show()
