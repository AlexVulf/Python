lista = [7, 3, 33, 12, 3, 3, 3, 7, 12, 100]

def remove_repetidos(lista):
    result=[]
    for x in lista:
        if x not in result:
            result.append(x)
    return result

lista=remove_repetidos(lista)
lista=sorted(lista)
print(lista)
