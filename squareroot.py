import math

# Achar quadrado perfeito 

numero = int(input())


raiz = math.sqrt(numero)
print(raiz)

if raiz % 2 != 0:
    print("Não é perfeita")
    

else:
    print("É perfeita")
    
