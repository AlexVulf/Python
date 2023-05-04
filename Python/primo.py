n= int(input("Digite um numero inteiro: "))
i=0
primo=0
while i<=n  or primo<2:
    i = i+1
    x=n%i
    if x==0 and n >=2:
       primo= primo + 1
       if primo <=2:
           print("primo")
       else:
           print("não primo")
    
