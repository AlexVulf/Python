lista = list()
while True:
    n = int(input(f'Digite um número: '))

    if n != 0:
        lista.append(n)
    else:
        for c in reversed(lista):
            print(c)
        break
