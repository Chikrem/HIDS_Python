#Implementação da Trie

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
