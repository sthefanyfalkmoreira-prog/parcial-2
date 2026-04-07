# Cria uma lista com 5 nomes 

nomes = ["Sofia", "Maria", "Leonardo", "Arthur", "Cecilia"]

# Pede para o usuário digitar um nome que será adicionado à lista
novo_nome = input("Digite um nome para adicionar à lista: ")

# Adiciona o nome digitado pelo usuário no final da lista
nomes.append(novo_nome)

# Mostra todos os nomes da lista, um por um
for nome in nomes:
    print(nome)  # Exibe o nome que o usuário digitou da lista
