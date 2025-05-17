# Cachorro Quente: R$4,00
# X-salada: 4.50
# X-bancon: 5.00
# Torrada simples: 2.00
# Refrigerante: 1.50

codigo, quantidade = input().split(" ")

codigo = int(codigo)
quantidade = float(quantidade)

if codigo == 1:
    valor = 4.00 * quantidade
    print(f"Total: R$ {valor:.2f}")

elif codigo == 2:
    valor = 4.50 * quantidade
    print(f"Total: R$ {valor:.2f}")

elif codigo == 3:
    valor =  5.00* quantidade
    print(f"Total: R$ {valor:.2f}")

elif codigo == 4:
    valor = 2.00 * quantidade
    print(f"Total: R$ {valor:.2f}")

elif codigo == 5:
    valor = 1.50 * quantidade
    print(f"Total: R$ {valor:.2f}")