import matplotlib.pyplot as plt  # Importa a biblioteca Matplotlib para criação de gráficos
import numpy as np  # Importa a biblioteca NumPy para operações matemáticas
import generetor as cg  # Importa o módulo generetor como 'cg'

# Cria um histograma dos scores das equipes
plt.hist(cg.team_scores, bins=20, edgecolor='k')  # Cria o histograma com 20 bins e bordas pretas
plt.title('Team Scores Histogram')  # Define o título do gráfico
plt.xlabel('Team Score')  # Define o rótulo do eixo x
plt.ylabel('Frequency')  # Define o rótulo do eixo y

# Calcula o valor de corte (cutoff) com base no percentil 80
percen80 = np.percentile(cg.team_scores, 80)  # Calcula o percentil 80 dos scores e armazena em 'percentile_80'

# Adiciona uma linha vertical pontilhada no gráfico no valor de 'limit' com uma cor vermelha
plt.axvline(percen80, color='r', linestyle='dashed', linewidth=2, label=f'Cut-off: {limit}')

plt.legend()  # Adiciona a legenda ao gráfico
plt.savefig('team_scores_histogram.png')  # Salva o gráfico como uma imagem PNG com o nome 'team_scores_histogram.png'

# Ordena a lista de carros com base no último atributo dos carros
cg.all_cars.sort(key=lambda car: car.car_atributes()[-1], reverse=True)

# Seleciona os carros de melhor desempenho com base no percentil 80
top_cars = cg.all_cars[:percent_20]
