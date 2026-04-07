# Conversão de tempo

# Digitar a quantidade total de segundos 
total_segundos = int(input("Digite a quantidade total de segundos: "))

# Calcula a quantidade de horas inteiras na divisão por 3600
horas = total_segundos // 3600

# Calcula os minutos restantes usando o resto da divisão das horas por 60
minutos = (total_segundos % 3600) // 60

# O que sobrar são os segundos
segundos = total_segundos % 60

# Resultado final 
print(f"{horas} horas, {minutos} minutos e {segundos} segundos.")
