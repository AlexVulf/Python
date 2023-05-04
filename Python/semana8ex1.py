from random import randint

def remove_repetidos(lista):
    set(lista)
    return lista

def sorteia(lista):
    for cont in range(0, 10):
        lista.append(randint(1, 6))

lista = list()
sorteia(lista)
remove_repetidos(lista)
lista=list(set(lista))
print(lista)

