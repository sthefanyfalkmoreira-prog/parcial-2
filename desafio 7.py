# Solicita o valor do capital inicial e converte para número decimal
capital = float(input("Digite o valor do capital (C): "))

# Solicita a taxa de juros (em porcentagem) e converte para decimal
taxa = float(input("Digite a taxa de juros (I): "))

# Solicita o tempo da aplicação e converte para número decimal
tempo = float(input("Digite o tempo (T): "))

# Aplica a fórmula matemática para calcular o valor dos juros (J)
juros = (capital * taxa * tempo) / 100

# Exibe o valor final dos juros calculados para o usuário no console
print("O valor dos juros simples (J) é:", juros)
