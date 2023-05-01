from trie import *
import glob

#######################################################################################################################
#######################################################################################################################

# 1) Carregar os arquivos do Dataset: Escolhidos os arquivos de treino, esses serão unidos em um único .txt
# que será carregado na trie. Assim a árvore conterá as n combinações de entradas para cada n-grams.

# O DataSet utilizado está disponível em 'https://github.com/thefrankinator7/anomaly-detection/tree/97c5edd0051e8f13ee3aa1a305f785e77c130809'
# e é uma versão mais trabalhada do DataSet ADFA-LD citado na documentação do trabalho.

# Nome do arquivo de entrada
input_file = "ADFA-LD\ADFA-LD\Training_Data_Attack\*.txt"
input_file_b = "ADFA-LD\ADFA-LD\Training_Data_Clean\*.txt"

# Nome do arquivo de saída
output_file = 'arquivo_saida.txt'
output_file_b = 'arquivo_saida_b.txt'

# Opicional: analizar cada amostra do dataset por vez na hora da validação. Achei melhor dessa forma ja que cada arquivo
# analizado seria como um processo distinto executando no HOST. Os arquivos de validação já são compilados de Syscalls,
# então esse passo é opicional, se desejar-se criar um arquivo de teste maior.

# with open(output_file, 'w') as out:
#     # Loop pelos arquivos no diretório
#     for filepath in glob.iglob(input_file, recursive=True):
#         # Abre o arquivo atual para leitura
#         with open(filepath, 'r') as f:
#             # Copia o conteúdo do arquivo para o arquivo de saída
#             out.write(f.read())

# Abre o arquivo de saída para escrita.

with open(output_file_b, 'w') as out:
     # Loop pelos arquivos no diretório
     for filepath in glob.iglob(input_file_b, recursive=True):
         # Abre o arquivo atual para leitura
         with open(filepath, 'r') as f:
                # Copia o conteúdo do arquivo para o arquivo de saída
                out.write(f.read())

# 'output_file_b' contém toda a lista sequencia de Syscalls de todos os arquivos.

# Abrir o arquivo_saida_b.txt em modo leitura
with open('arquivo_saida_b.txt', 'r') as file:
    # Ler o conteúdo do arquivo
    content = file.read().strip()
    # Separar os números em uma lista
    numbers = content.split()

# O arquivo 'arquivo_saida_b.txt' é acessado para que seja carregado para a criação dos n-grams. Todos os passos de
# execução geram arquivos .txt de saída que serão utilizados no passo subsequente. Facilitando sua a análize,
# compreensão e economizando memória.


#######################################################################################################################
#######################################################################################################################

# 2) Criar os n-grams: carregado o arquivo 'arquivo_saida_b.txt', o mesmo será percorrido e separado em n-grams definidas
# abaixo. O resultado final será gravado em 'ngrams.txt' que subsequentemente será carregado para insersão na Trie.

# nltk.lm package -> módulo do python capaz de trabalhar com n-grams. A princípio foi utilizado essa abordagem, mas
# por conta de alguns bugs acabei abandonando e adotando um método mais simplificado com strings.
# Documentação disponível em: 'https://www.nltk.org/api/nltk.lm.html'

# Definir o tamanho do n-gram
n = 2

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

# 'ngrams.txt' contém todos os n-grams do Dataset. Um por linha e separados por espaço -> 168 168 168 168 265 168 168 168 3 168.

#######################################################################################################################
#######################################################################################################################

# 3) Criar uma Trie e Inserir o grams: feita a implementação simples de uma Trie (Insersão e Busca). Cria-se uma instância
# e o 'ngrams.txt' é lido, percorrido e carregado na Trie. Todas as combinações presentes na Trie são gravadas em 'trie_nodes.txt'


# Criar uma nova instância da trie
trie = Trie()

# Ler o arquivo de ngrams.txt
with open('ngrams.txt', 'r') as file:
    # Ler cada linha do arquivo como uma palavra e inserir na trie
    for line in file:
        word = line.strip()
        trie.insert(word)

# Exemplo de busca na trie
# word_to_search = '6 6 114'
# result = trie.search(word_to_search)
# if result:
#     print(f'A palavra "{word_to_search}" foi encontrada na trie.')
# else:
#     print(f'A palavra "{word_to_search}" não foi encontrada na trie.')

#Printar os nós
#trie.print_nodes()

# Método recursivo de Trie para escrever os nós da trie em um arquivo
trie.write_nodes_to_file('trie_nodes.txt')


#######################################################################################################################
#######################################################################################################################

# 4) Arquivo de teste: Agora precisamos repetir o passo 1 mas com a amostra que queremos testar, ou seja, transforma-la
# em n-grams e salvar os n-grams em um novo .txt. Assim a busca na árvore pode ser executada.


# Ler o arquivo de amostra
with open('UTD-0001.txt', 'r') as file:
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

#######################################################################################################################
#######################################################################################################################

# 5) Executar os testes: Com a amostra e a Trie carrega, o último passo é percorrer a arvore e verificar se as sequencias
# n-grams coincidem com as combinações presentes na árvore.

# Inicializar o contador. Sempre que uma sequencia não for encontrada na arvore, uma infração é contabilizada. Sendo o máximo
# de 5 até ser considerada uma intrusão.
not_found_count = 0

# Ler o arquivo de ngrams_a.txt
with open('ngrams_a.txt', 'r') as file:
    # Ler cada linha do arquivo como uma entrada de busca e procurar na Trie
    for line in file:
        search_query = line.strip()
        if trie.search(search_query):
            print(f'Encontrado: {search_query}')
        else:
            print(f'Não encontrado: {search_query}')
            not_found_count += 1

# Verificar se o contador é maior que 6. O projeto pede um n = 5, mas ocorre de os n-grams não serem distribuidas de maneira
# uniforme. Por exemplo, se o n-grams for ímpar e a quantidade de syscalls no arquivo de amostragem for par, a última string
# terá caracteres a menos e possívelmente não será encontrada na busca. Portando foi adicionado 1 ao n para descartar esse
# possível falso positivo. Utilizando o nltk.py é possível tratar esses casos, mas seria necessário mais tempo de pesquisa
# na documentação para fazer funcionar.

if not_found_count > 6:
    print('Resultados negativos: ', not_found_count)
    print('Intrusão detectada!')


#######################################################################################################################
#######################################################################################################################
