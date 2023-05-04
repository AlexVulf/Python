import math

a = float(input("Digite a coordenada x: "))
b = float(input("Digite a coordenada y: "))
c = float(input("Digite a coordenada x: "))
d = float(input("Digite a coordenada y: "))
e = ((a-b)**2)+((c-d)**2)
distancia = math.sqrt(e)
if distancia>=10:
    print("longe")
else:
    print("perto")
