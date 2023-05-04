from dataclasses import dataclass
from datetime import date
from time import time


dia_t = input("Dia Trabalhado: ") 
Kmrodado = float(input("KM rodado: ")) 
combustivel = float(input("Gasto com Combustível: ")) 
combustivel_l = float(input("Litro de Combustivel: "))
hora_i = time(input("hora inicio: ")) 
hora_a = time(input("Hora almoço: ")) 
hora_a_v = time(input("Hora de retorno: ")) 
hora_f = time(input("hora final: ")) 
