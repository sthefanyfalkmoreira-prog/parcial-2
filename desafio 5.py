#Calcular a área de um triângulo a partir de sua base e altura.

# Pede o valor da base do triângulo
base = float(input("Qual é a base do triângulo? "))

# Pede o valor da altura do triângulo
altura = float(input("Qual é a altura do triângulo? "))

# Se a base ou a altura forem zero ou negativos, dá erro
if base <= 0 or altura <= 0:
    print("A base e a altura precisam ser maiores que zero!")
else:
    # Calcula a área do triângulo
    area = (base * altura) / 2

    # Mostra o resultado
    print("A área do triângulo é:", area)
