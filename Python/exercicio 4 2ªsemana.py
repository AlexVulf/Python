totals=input("Por favor, entre com o número de segundos que deseja converter:")
total=int(totals)
a=total//86400
resth=total%86400
b=resth//3600
restseg=resth%3600
c=restseg//60
d=restseg%60

print(a,"dias,", b,"horas,", c,"minutos e", d,"segundos.")
