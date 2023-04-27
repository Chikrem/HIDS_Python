from trie import *

# Abrir o arquivo UTD-0001.txt em modo leitura
with open('arquivo_saida.txt', 'r') as file:
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

# Criar uma nova instância da trie
trie = Trie()

# Ler o arquivo de ngrams.txt
with open('ngrams.txt', 'r') as file:
    # Ler cada linha do arquivo como uma palavra e inserir na trie
    for line in file:
        word = line.strip()
        trie.insert(word)

# Exemplo de busca na trie
word_to_search = '6 6 114'
result = trie.search(word_to_search)
if result:
    print(f'A palavra "{word_to_search}" foi encontrada na trie.')
else:
    print(f'A palavra "{word_to_search}" não foi encontrada na trie.')

trie.print_nodes()
trie.write_nodes_to_file('trie_nodes.txt')


with open('arquivo_saida_b.txt', 'r') as file:
    # Ler o conteúdo do arquivo
    content = file.read().strip()
    # Separar os números em uma lista
    numbers = content.split()

# Criar uma lista para armazenar os n-grams
ngrams_b = []

# Criar os n-grams
for i in range(len(numbers)-n+1):
    ngram = ' '.join(numbers[i:i+n])
    ngrams_b.append(ngram)

# Criar um novo arquivo para salvar os n-grams
with open('ngrams_a.txt', 'w') as file:
    # Escrever os n-grams no arquivo
    file.write('\n'.join(ngrams_b))


# Inicializar o contador
not_found_count = 0

# Ler o arquivo de ngrams_a.txt
with open('ngrams_a.txt', 'r') as file:
    # Ler cada linha do arquivo como uma entrada de busca e procurar na trie
    for line in file:
        search_query = line.strip()
        if trie.search(search_query):
            print(f'Encontrado: {search_query}')
        else:
            print(f'Não encontrado: {search_query}')
            not_found_count += 1

# Verificar se o contador é maior que 5
if not_found_count > 5:
    print('Intrusão detectada!')
