linha=1
coluna=1
while linha <= 10:
    while coluna <= 10:
        print (linha,"x", coluna, "=", linha*coluna, end = "\t \t \t")
        coluna = coluna + 1
    linha = linha + 1
    print()
    coluna = 1