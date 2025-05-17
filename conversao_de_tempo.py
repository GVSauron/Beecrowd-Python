hora = 0
segundo = 0
user_segundo = int(input())

# 1 hora = 3600s
# 1 minuto = 60s



hora = (user_segundo/3600)
minuto = (user_segundo % 3600)/60
segundo = user_segundo % 60

hora = int(hora)
minuto = int(minuto)

    
print(f"{hora:.0f}:{minuto:.0f}:{segundo:.0f}")
