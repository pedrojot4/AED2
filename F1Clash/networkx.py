import networkx as nx
import matplotlib.pyplot as plt
import generetor as cg
import seaborn as sns

# Coleta os valores de pontuação de todas as carros na lista de cg.all_cars
team_scores = [car.car_atributes()[-1] for car in cg.all_cars]

# Seleciona os 0.01% principais carros com base em suas pontuações
top_20_percent = sorted(
    cg.all_cars, key=lambda car: car.car_atributes()[-1], reverse=True)[:int(0.0001 * len(cg.all_cars))]

# Itera sobre os carros no top 0.01% e imprime o nome do carro e o nome do sistema de freios
for car in top_20_percent:
    print(car.name, print(car.breaks.name))

# Cria um grafo vazio usando NetworkX
G = nx.Graph()

# Adiciona nós representando carros e peças no grafo
for car in top_20_percent:
    G.add_node(car.name, type='car')
    for part in [car.breaks, car.gearbox, car.rearwing, car.frontwing, car.suspension, car.engine]:
        part_name = part.name
        G.add_node(part_name, type='part')
        G.add_edge(car.name, part_name)

# Define o layout do grafo usando Kamada-Kawai e configura o tamanho da figura
pos = nx.kamada_kawai_layout(G)
plt.figure(figsize=(12, 8))

# Define as cores dos nós com base no tipo (carro ou peça)
node_colors = ['blue' if G.nodes[node]['type'] == 'car' else 'red' for node in G.nodes]

# Desenha o grafo com rótulos e cores dos nós
nx.draw(G, pos, with_labels=True, font_weight='bold', node_color=node_colors)

# Salva a visualização do grafo como 'graph.png'
plt.savefig('graph.png')

# Calcula os graus de saída (out-degrees) dos nós e gera um histograma com Seaborn
out_degrees = dict(G.degree(G.nodes(), weight=None))
out_degree_values = list(out_degrees.values())
plt.figure(figsize=(12, 8))
sns.histplot(out_degree_values, kde=True, color='blue')

# Configura rótulos e título do histograma
plt.xlabel('Out Degree')
plt.ylabel('PDF')
plt.title('PDF of Node Out Degrees')

# Salva o histograma como 'out_degree_pdf.png'
plt.savefig('out_degree_pdf.png')

# Exibe o gráfico e o histograma
plt.show()
