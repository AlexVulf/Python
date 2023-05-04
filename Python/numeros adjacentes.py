n = int(input("Digite um número inteiro:"))
adjacente=False
resto=0

while n!=0 and not adjacente:
    resto=n%10
    n=n//10
    b=n%10
    if b==resto:
         adjacente = True
if adjacente:
    print("sim")
else:
    print("não")
    
	
