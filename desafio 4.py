#Calculadora simples

# Pede para o usuário digitar o primeiro número
n1 = float(input("Digite o primeiro número: "))

# Pede para o usuário digitar o segundo número
n2 = float(input("Digite o segundo número: "))

# Soma os dois números
soma = n1 + n2

# Subtrai o segundo número do primeiro
subtracao = n1 - n2

# Multiplica os dois números
multiplicacao = n1 * n2

# Verifica se o segundo número é zero para não dividir por zero
if n2 != 0:
    divisao = n1 / n2
    print("Divisão:", divisao)
else:
    print("Não é possível dividir por zero!")

# Mostra os resultados das operações
print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
