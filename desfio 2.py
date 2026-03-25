# Programa que verifica se um número é par ou ímpar

# Pede para o usuário digitar um número e transforma em inteiro
num = int(input("Digite um número: "))

# Verifica se o número é par usando o resto da divisão (%)
if num % 2 == 0:
    # Se o resto da divisão por 2 for zero, o número é par
    print("O número é par")
else:
    # Se não for zero, o número é ímpar
    print("O número é ímpar")
