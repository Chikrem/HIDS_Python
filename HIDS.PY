from nltk.util import bigrams
text = [['a', 'b', 'c'], ['a', 'c', 'd', 'c', 'e', 'f']]
lista = list(bigrams(text[0]))
print(lista)