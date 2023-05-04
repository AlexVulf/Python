n = int(input("digite o numero: "))
soma=0
while (n!=0):
     soma = soma + (n%10)
     n=n//10

print(soma)
