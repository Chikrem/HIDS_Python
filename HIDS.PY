
from nltk.lm.preprocessing import pad_both_ends
text = [['a', 'b', 'c'], ['a', 'c', 'd', 'c', 'e', 'f']]
lista = list(pad_both_ends(text[0], n=2))

print(lista)