# Juros simples
# Pede o valor do Capital e transforma em número inteiro 
C = int(input("Digite o Capital (C): "))

# Pede a taxa de juros e transforma em número inteiro 
I = int(input("Digite a Taxa de juros (I): "))

# Pede o tempo da aplicação e transforma em número inteiro 
T = int(input("Digite o Tempo (T): "))

# Multiplica os três valores e divide por 100 para achar os juros
J = (C * I * T) / 100

# Mostra o resultado final calculado na tela
print(f"O valor dos juros simples (J) é: {J}")
