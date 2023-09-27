import csv
import time
import random

def row_price(row):
    return row[-1]

class Inventory():                    
    
    def __init__(self, csv_filename):
        # Abre o arquivo CSV especificado e lê seus dados
        with open(csv_filename, encoding="ISO-8859-1") as f:
            reader = csv.reader(f)
            rows = list(reader)
        # Armazena o cabeçalho e as linhas de dados
        self.header = rows[0]
        self.rows = rows[1:]
        
        # Converte o preço de cada laptop para um número de ponto flutuante
        for row in self.rows:
            row[-1] = float(row[-1])
        
        # Cria um dicionário que mapeia IDs de laptops para suas respectivas linhas
        self.id_to_row = {}
        for row in self.rows:
            self.id_to_row[row[0]] = row
        
        # Cria um conjunto contendo todos os preços únicos dos laptops
        self.prices = set()
        for row in self.rows:
            self.prices.add(row[-1])
        
        # Ordena as linhas de laptops com base no preço
        self.rows_by_price = sorted(self.rows, key=row_price)
    
    # Obtém um laptop pelo seu ID
    def get_laptop_from_id(self, laptop_id):
        for row in self.rows:                 
            if row[0] == laptop_id:
                return row
        return None
    #Big O - O(n) - Pior caso, pior quando estiver no final da lista.
    #Big Theta - O(n/2) - Caso Intermediario, melhor no inicio da lista.
    #Big Omega - O(1) -  Melhor caso, melhor se estiver no inicio da lista
    
    # Obtém um laptop pelo seu ID de forma mais eficiente usando um dicionário
    def get_laptop_from_id_fast(self, laptop_id):  
        if laptop_id in self.id_to_row:           
            return self.id_to_row[laptop_id]
        return None
    #Big O - O(1) - Constante, um unico item corresponde.
    #Big Theta - O(1) - Constante, um unico item corresponde.
    #Big Omega - O(1) - Constante, um unico item corresponde.

    # Verifica se é possível encontrar laptops cujo preço some para igualar 'dollars'
    def check_promotion_dollars(self, dollars):    
        for row in self.rows:                   
            if row[-1] == dollars:
                return True
        for row1 in self.rows:                  
            for row2 in self.rows:
                if row1[-1] + row2[-1] == dollars:
                    return True
        return False
    #Big O - O(n^2) - Pior caso, pior se tiver que verificar todos os itens da lista.
    #Big Theta - O(n^2) - Caso Intermediario, no maximo metade precisa ser veriicado.
    #Big Omega - O(1) - Melhor caso, operação constante, um unico item corresponde.                       
    
    # Verifica promoções de forma mais eficiente usando um conjunto
    def check_promotion_dollars_fast(self, dollars):
        if dollars in self.prices:                   
            return True
        for price in self.prices:                    
            if dollars - price in self.prices:
                return True
        return False
    #Big O - O(n) - Pior caso, o loop pode precisar de muitas operações.
    #Big Theta - O(n) - Caso Intermediario, loop com menos complexidade.
    #Big Omega - O(1) - Melhor caso, operação constante, um unico item corresponde.                                
    
    # Encontra um laptop com um preço específico usando busca binária
    def find_laptop_with_price(self, target_price):
        range_start = 0                                   
        range_end = len(self.rows_by_price) - 1                       
        while range_start < range_end:
            range_middle = (range_end + range_start) // 2  
            value = self.rows_by_price[range_middle][-1]
            if value == target_price:                            
                return range_middle                        
            elif value < target_price:                           
                range_start = range_middle + 1             
            else:                                          
                range_end = range_middle - 1 
        if self.rows_by_price[range_start][-1] != target_price:                  
            return -1                                      
        return range_start
    #Big O - O(log(n)) - Pior caso, resultante da busca binaria.
    #Big Theta - O(log(n)) - Caso intermediario, já que a busca binaria vai trabalhar com a media.
    #Big Omega - O(1) - Melhor caso, operação constante, um unico item corresponde.
    
    # Encontra o índice do primeiro laptop mais caro que um preço alvo usando busca binária
    def find_first_laptop_more_expensive(self, target_price): 
        range_start = 0                                   
        range_end = len(self.rows_by_price) - 1                   
        while range_start < range_end:
            range_middle = (range_end + range_start) // 2  
            price = self.rows_by_price[range_middle][-1]
            if price > target_price:
                range_end = range_middle
            else:
                range_start = range_middle + 1
        if self.rows_by_price[range_start][-1] <= target_price:                  
            return -1                                   
        return range_start
    #Big O - O(log(n)) - Pior caso, resultante da busca binaria.
    #Big Theta - O(log(n)) - Caso intermediario, já que a busca binaria vai trabalhar com a media.
    #Big Omega - O(1) - Melhor caso, operação constante, um unico item corresponde.
    
    # Encontra todos os laptops cujo preço esteja dentro de uma faixa especificada
    def find_laptops_in_price_range(self, min_price, max_price):
        laptops_in_range = []
        for row in self.rows_by_price:
            price = row[-1]
            if min_price <= price <= max_price:
                laptops_in_range.append(row)
        return laptops_in_range
    #Big O - O(n) - Pior caso, percorre toda a lista no pior caso.
    #Big Theta - O(n/2) - Caso intermediario, ja que vai trabalhar com a media.
    #Big Omega - O(1) - Melhor caso, constante, sem loop.
    
    # Encontra o laptop mais barato com as características desejadas
    def find_cheapest_laptop_with_specifications(self, ram_gb, storage_gb):
        cheapest_laptop = None
        cheapest_price = float('inf')  # Inicializa o preço mais barato com infinito

        for row in self.rows:
            laptop_ram_str = row[4]  # Supondo que a quantidade de RAM está na coluna 4
            laptop_storage_str = row[5]  # Supondo que a capacidade do disco está na coluna 5

            # Verifica se as strings podem ser convertidas em números de ponto flutuante
            try:
                laptop_ram = float(laptop_ram_str)
                laptop_storage = float(laptop_storage_str)
            except ValueError:
                # Se não for possível converter, ignore esta linha
                continue

            price = row[-1]

            # Verifica se o laptop atende às especificações e se é mais barato
            if laptop_ram >= ram_gb and laptop_storage >= storage_gb and price < cheapest_price:
                cheapest_laptop = row
                cheapest_price = price

        return cheapest_laptop
    #Big O - O(nr) -
    #Big Theta - O(nr) -
    #Big Omega - O(n) -

# Cria uma instância da classe Inventory com o arquivo CSV 'laptops.csv'
inventory = Inventory('laptops.csv') 

# Encontra e imprime todos os laptops cujo preço esteja dentro de uma faixa especificada
print(inventory.find_laptops_in_price_range(1585,1590))

# Uso do novo método para encontrar o laptop mais barato com 8GB de RAM e 256GB de disco
ram_gb = 4
storage_gb = 500
cheapest_laptop = inventory.find_cheapest_laptop_with_specifications(ram_gb, storage_gb)

# Imprime o laptop mais barato com as especificações desejadas, se encontrado
if cheapest_laptop:
    print("Laptop mais barato com as especificações desejadas:")
    print(cheapest_laptop)
else:
    print("Nenhum laptop encontrado com as especificações desejadas.")





