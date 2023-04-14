import nltk
from pygtrie import StringTrie

nltk.download('punkt')

trie = StringTrie()

with open('UTD-0001.txt', 'r') as file:
    text = file.read()
    n = 10

    # Gera os tokens e os 10-grams correspondentes
    tokens = nltk.word_tokenize(text)
    n_grams = []
    fixed_size_10grams = []
    for token in tokens:
        # Remove caracteres especiais e números
        token = ''.join(e for e in token if e.isalnum())
        # Gera os n-grams
        for gram in nltk.ngrams(token, n):
            fixed_gram = ''.join(str(num).zfill(3) for num in gram)
            fixed_size_10grams.append(fixed_gram)

    for token in tokens:
        trie.setdefault(token, 0)
        trie[token] += 1

print(trie)

sequence = '6 6 63 6 42 120 6 195 120 6'
current_node = trie._root
for i in range(len(sequence) - n + 1):
    gram = sequence[i:i+n]
    fixed_gram = ''.join(str(num).zfill(3) for num in gram)
    if fixed_gram in current_node.children:
        current_node = current_node.children[fixed_gram]
    else:
        print("Sequência não encontrada na árvore!")
        break

# Verifica se chegou em um nó final da árvore
if current_node.value is not None:
    print("Sequência encontrada na árvore!")
else:
    print("Sequência não encontrada na árvore!")