# Abrir o arquivo UTD-0001.txt em modo leitura
with open('UTD-0001.txt', 'r') as file:
    # Ler o conteúdo do arquivo
    content = file.read().strip()
    # Separar os números em uma lista
    numbers = content.split()

# Definir o tamanho do n-gram
n = 10

# Criar uma lista para armazenar os n-grams
ngrams = []

# Criar os n-grams
for i in range(len(numbers)-n+1):
    ngram = ' '.join(numbers[i:i+n])
    ngrams.append(ngram)

# Criar um novo arquivo para salvar os n-grams
with open('ngrams.txt', 'w') as file:
    # Escrever os n-grams no arquivo
    file.write('\n'.join(ngrams))

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

# Definir a classe para a árvore trie
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word




    # Método recursivo para imprimir os nós da trie
    def _print_nodes(self, node, prefix):
        if node.is_end_of_word:
            print(prefix)

        for char, child in node.children.items():
            self._print_nodes(child, prefix + char)


    # Método público para iniciar a impressão dos nós da trie
    def print_nodes(self):
        self._print_nodes(self.root, '')




    # Método recursivo para escrever os nós da trie em um arquivo
    def _write_nodes(self, node, prefix, file):
        if node.is_end_of_word:
            file.write(prefix + '\n')
        for char, child in node.children.items():
            self._write_nodes(child, prefix + char, file)

    # Método público para iniciar a escrita dos nós da trie em um arquivo
    def write_nodes_to_file(self, filename):
        with open(filename, 'w') as file:
            self._write_nodes(self.root, '', file)





# Criar uma nova instância da trie
trie = Trie()

# Ler o arquivo de ngrams.txt
with open('ngrams.txt', 'r') as file:
    # Ler cada linha do arquivo como uma palavra e inserir na trie
    for line in file:
        word = line.strip()
        trie.insert(word)

# Exemplo de busca na trie
word_to_search = '6 6 114 114 1 1 252 252 252 1'
result = trie.search(word_to_search)
if result:
    print(f'A palavra "{word_to_search}" foi encontrada na trie.')
else:
    print(f'A palavra "{word_to_search}" não foi encontrada na trie.')

trie.print_nodes()
trie.write_nodes_to_file('trie_nodes.txt')