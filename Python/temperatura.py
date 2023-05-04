def MinMax(temperaturas):
    print('A menor temperatura do mês foi: ', mínimo(temperaturas), 'C.')
    print('A maior temperatura do mês foi: ', máxima(temperaturas), 'C.')

def máxima(temps):
    max = temps[0]
    i = 1
    while i < len(temps):
        if temps[i] > max:
            max = temps[i]
        i = i + 1
    return  max

def mínimo(temps):
    min = temps[0]
    i = 1
    while i < len(temps):
        if temps[i] < min:
            min = temps[i]
        i = i + 1
    return  min

def teste_pontual(temp, valor_esperado):
    valor_calculado = mínimo(temp)
    if valor_calculado != valor_esperado:
        print('valor errado para array', temp)
        print('valor esperado: ', valor_esperado, '. Valor Calculado: ', valor_calculado)

def testa_mínima():
    print('Iniciando os teste')
    teste_pontual([0], 0)
    teste_pontual([0, 0, 0, 0, 0], 0)
    teste_pontual([0, 1, 2, 3, 4, 5], 0)
    teste_pontual([32, 31, 25, 31, 24, 25, 27, 29, 29, 27, 28, 29, 24, 25, 22, 25, 24, 26, 30, 32, 31,
            28, 29, 32, 32, 32, 33, 33, 34, 34, 33, 31, 31, 28, 23, 21, 24, 24, 24, 28, 28, 28], 21)
    teste_pontual([-10, -15, -1, 0, 25, 30, 20], -15)
    print('fim')
