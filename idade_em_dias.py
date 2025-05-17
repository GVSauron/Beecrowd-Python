import math
from math import floor # importa a funcão floor que pode ser usada para arredondaar valores para baixo
from math import ceil # ceil pode ser usado para arredonda os valor para cima 
dias = int(input())



ano = dias/365 # quantidade de anos
mes = (dias % 365)/30 # quantidade de meses
dias_idade = (dias % 365) % 30 #quantidade de dias

# converte em int para os valores serem arrendondas para o valor menor mais próximo
mes = int(mes) 
dias_idade = int(dias_idade)
ano = math.floor(ano)

print(f"{ano:.0f} ano(s)")
print(f"{mes:.0f} mes(es)")
print(f"{dias_idade:.0f} dia(s)")

