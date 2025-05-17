
# Calcular peso nos planetas
# Limitar a 2 casas decimais

# Mercúrio: 3,7 m/s²
# Vênus: 8,87 m/s²
# Terra: 9,80 m/s²
# Lua: 1,6 m/s²
# Marte: 3,711 m/s²
# Júpiter: 24,79 m/s²
# Saturno: 10,44 m/s²
# Urano: 8,87 m/s²
# Netuno: 11,15 m/s²
# Plutão: 0,62 m/s² 


g_mercurio = 3.7
g_venus = 8.87
g_terra = 9.80
g_lua = 1.6
g_marte =  3.711
g_jupiter = 24.79
g_saturno = 10.44


print("1 - Mercurio")
print("2 - Vênus")
print("3 - Terra")
print("4 - Lua")
escolha = int(input("Escolha em qual planeta deseja ver seu peso: "))

if escolha == 1:
    print("Planeta Mercurio escolhido")
    peso = float(input("Digite seu peso na Terra: "))

    P = peso * g_mercurio
    peso_planeta = P/9.8 # 9,8N equivale a 1kg na Terra
    print(f"Seu peso no planeta Mercurio é {peso_planeta:.2f}Kg.")

elif escolha == 2:
    print("Planeta Venus escolhido")
    peso = float(input("Digite seu peso na Terra: "))

    P = peso * g_venus
    peso_planeta = P/9.8 # 9,8N equivale a 1kg na Terra
    print(f"Seu peso no planeta Venus é {peso_planeta:.2f}Kg.")

