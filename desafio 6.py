# Solicita a quantidade total de segundos ao usuário e converte para inteiro
total_segundos = int(input("Digite a quantidade total de segundos: "))

# Calcula a quantidade de horas inteiras na divisão por 3600
horas = total_segundos // 3600

# Calcula os minutos restantes usando o resto da divisão das horas por 60
minutos = (total_segundos % 3600) // 60

# Calcula os segundos que restaram após extrair as horas e os minutos
segundos = total_segundos % 60

# Exibe o resultado final formatado para o usuário no console
print(f"{horas} horas, {minutos} minutos e {segundos} segundos.")
