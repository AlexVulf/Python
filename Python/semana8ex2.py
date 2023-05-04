lista=[1, 2, 3, 4, 5]
def soma_elementos(lista):
    soma=0
    for n in lista:
        soma = soma + n
    return (soma)

lista=soma_elementos(lista)
print(lista)