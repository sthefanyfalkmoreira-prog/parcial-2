# 1. Pede para o usuário digitar um número 
numero = int(input("Digite um número: "))

# 2. Testa se o número pode ser dividido por 2 sem sobrar nada
if numero % 2 == 0:
    # 3. Se não sobrou nada (resto 0), ele avisa que é PAR
    print("O número é par")
# 4. Caso contrário (se sobrou 1 no resto da divisão)
else:
    # 5. Ele avisa que o número só pode ser ÍMPAR
    print("O número é ímpar")
