n1, n2, n3, n4 = input().split()

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / (2 + 3 + 4 + 1)

print(f"Media: {media:.1f}")

if media >= 7:
    print("Aluno aprovado.")

elif media < 5.0:
   print("Aluno reprovado.")

elif media >= 5.0 and media <=6.9:
    print("Aluno em exame.")
    nota_aluno = float(input())
    print(f"Nota do exame: {nota_aluno:.1f}")
    mediafinal = (media + nota_aluno) / 2

    if mediafinal >= 5.0:
        print("Aluno aprovado.")
        print(f"Media final: {mediafinal:.1f}")
        
    elif mediafinal <= 4.9:
        print("Aluno reprovado.")
        print(f"Media final: {mediafinal:.1f}")


    






