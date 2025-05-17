# 12km/L 
# Primeira Entrada - tempo gasto
# Segundo input - Velocidade média

velocidade = int(input())
tempo_gasto = int(input())

km_total = velocidade * tempo_gasto
litros_gasto = km_total / 12

#Limita as casas decimais para apenas 3
print(f"{litros_gasto:.3f}")
