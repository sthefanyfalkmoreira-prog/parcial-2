# Cria uma lista chamada 'nomes' contendo 5 nomes iniciais
nomes = ["Sofia", "Maria", "Leonardo", "Arthur", "Cecilia"]

# Solicita ao usuário que digite um novo nome para a lista
novo_nome = input("Digite um nome para adicionar à lista: ")

# Adiciona o nome digitado pelo usuário ao final da lista existente
nomes.append(novo_nome)

# Inicia um laço de repetição para percorrer cada item dentro da lista
for nome in nomes:
    # Exibe no console o nome atual da repetição com uma mensagem
    print("Nome na lista:", nome)
