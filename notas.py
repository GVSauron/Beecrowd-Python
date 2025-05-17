#  notas são 100, 50, 20, 10, 5, 2 e 1

valor = int(input())

# Quantas notas de 100 cabem
nota_100 = int(valor / 100)
print(f"Cabem {nota_100} nota(s) de 100")

# Quantas notas de 50 cabem
resto_100 = valor % 100
nota_50 = int(resto_100 / 50)
print(f"Cabem {nota_50} nota(s) de 50")

# Quantas notas de 20 cabem
resto_50 = nota_50 