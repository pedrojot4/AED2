import time

# Define a classe AVLNode que representa um nó na árvore AVL.
class AVLNode:
    def __init__(self, key):
        self.key = key            # A chave (valor) do nó
        self.left = None          # Referência para o filho esquerdo
        self.right = None         # Referência para o filho direito
        self.height = 1           # Altura inicial do nó é 1

# Define a classe AVLTree que representa a árvore AVL.
class AVLTree:
    def __init__(self):
        self.root = None          # Inicializa a raiz da árvore como None (árvore vazia)

    # Métodos auxiliares para cálculos de altura e fator de equilíbrio.

    def _height(self, node):
        if node is None:
            return 0
        return node.height

    def _update_height(self, node):
        if node is not None:
            node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _balance_factor(self, node):
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    # Métodos para rotações (esquerda e direita) para manter o equilíbrio da árvore.

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        self._update_height(z)
        self._update_height(y)

        return y

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self._update_height(y)
        self._update_height(x)

        return x

    # Método para balancear um nó.

    def _balance(self, node):
        if node is None:
            return node

        balance = self._balance_factor(node)

        if balance > 1:
            if self._balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1:
            if self._balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    # Método público para inserir um valor na árvore AVL.

    def insert(self, key):
        self.root = self._insert(self.root, key)

    # Método privado para inserir um valor em um nó da árvore AVL.

    def _insert(self, node, key):
        if node is None:
            return AVLNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        self._update_height(node)

        return self._balance(node)

    # Método para encontrar palavras com um prefixo dado na árvore AVL.

    def _find_words_with_prefix(self, node, prefix, results):
        if node is None:
            return

        if node.key.startswith(prefix):
            results.append(node.key)

        if prefix < node.key:
            self._find_words_with_prefix(node.left, prefix, results)
        else:
            self._find_words_with_prefix(node.right, prefix, results)

    # Método público para encontrar palavras com um prefixo dado na árvore AVL.

    def find_words_with_prefix(self, prefix):
        results = []
        self._find_words_with_prefix(self.root, prefix, results)
        return results

# Função para pré-processar e construir a árvore AVL.

def build_avl_tree(corpus):
    avl_tree = AVLTree()

    # Pré-processamento do corpus: dividir em palavras e remover pontuações.
    words = corpus.lower().split()
    words = [word.strip('.,;?!()[]{}"\'') for word in words]

    # Construção da árvore AVL inserindo cada palavra do corpus.
    for word in words:
        avl_tree.insert(word)

    return avl_tree

# Implementação de uma árvore binária de busca simples (BST).
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return BSTNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        return node

    def find(self, key):
        return self._find(self.root, key)

    def _find(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node.key
        elif key < node.key:
            return self._find(node.left, key)
        else:
            return self._find(node.right, key)

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0
        left_height = self._height(node.left)
        right_height = self._height(node.right)
        return max(left_height, right_height) + 1

# Função para comparar o desempenho da árvore AVL e da árvore binária de busca simples.
def compare_performance():
    import time

    corpus = "Como vês, Capitu, aos quatorze anos, tinha já ideias atrevidas, muito menos que outras que lhe vieram depois; mas eram só atrevidas em si, na prática faziam-se hábeis, sinuosas, surdas, e alcançavam o fim proposto, não de salto, mas aos saltinhos."
    
    # Árvore AVL
    start_time = time.time()
    avl_tree = build_avl_tree(corpus)
    insertion_time_avl = time.time() - start_time
    avl_height = avl_tree.root.height

    prefix = "cap"
    start_time = time.time()
    completions_avl = avl_tree.find_words_with_prefix(prefix)
    search_time_avl = time.time() - start_time

    # Árvore binária de busca simples (BST)
    start_time = time.time()
    bst = BST()
    words = corpus.lower().split()
    words = [word.strip('.,;?!()[]{}"\'') for word in words]
    for word in words:
        bst.insert(word)
    insertion_time_bst = time.time() - start_time
    bst_height = bst.height()

    start_time = time.time()
    completion_bst = bst.find(prefix)
    search_time_bst = time.time() - start_time

    # Imprime os resultados
    print("Árvore AVL:")
    print(f"Tempo de inserção: {insertion_time_avl} segundos")
    print(f"Altura da árvore: {avl_height}")
    print(f"Tempo de busca: {search_time_avl} segundos")
    print()

    print("Árvore binária de busca simples (BST):")
    print(f"Tempo de inserção: {insertion_time_bst} segundos")
    print(f"Altura da árvore: {bst_height}")
    print(f"Tempo de busca: {search_time_bst} segundos")
    print()

if __name__ == "__main__":
    compare_performance()

# Exemplo de uso:

if __name__ == "__main__":
    corpus = "Eis aqui outro seminarista. Chamava-se Ezequiel de Sousa Escobar era um rapaz esbelto, olhos claros, um pouco fugitivos, como as mãos, como os pés, como a fala, como tudo. Quem não estivesse acostumado com ele podia acaso sentir-se mal, não sabendo por onde lhe pegasse. Não fitava de rosto, não falava claro nem seguido as mãos não apertavam as outras, nem se deixavam apertar delas, por que os dedos, sendo delgados e curtos, quando a gente cuidava tê-los entre os seus, já não tinha nada. (...) Quando ele entrou na minha intimidade pedia-me freqüentemente explicações e repetições miúdas, e tinha memória para guardá-las todas, até as palavras. Talvez esta faculdade prejudicasse alguma outra." 
    # Constrói uma árvore AVL a partir do corpus.
    avl_tree = build_avl_tree(corpus)

    prefix = "p"
    
    # Encontra palavras que começam com o prefixo "cap".
    completions = avl_tree.find_words_with_prefix(prefix)
    
    if completions:
        print(f"Palavras que começam com '{prefix}':")
        for word in completions:
            print(word)
    else:
        print(f"Nenhuma palavra encontrada com o prefixo '{prefix}'.")