n=int(input('Entre com o número: '))
for y in range(1, n+1):
    div=0
    for x in range(1, y+1):
        resto = y % x
        if resto == 0:
            div += 1
    if div == 2:
        print(y)


