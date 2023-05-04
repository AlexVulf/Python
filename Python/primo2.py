n = int(input("Digite um número inteiro:"))
x =2
y = 0
naoprimo=False
while x<n:
	y = n % x
	x = x + 1
	if y==0:
		naoprimo=True
if naoprimo or n==1:
	print("nao primo")
else:
	print("primo")
