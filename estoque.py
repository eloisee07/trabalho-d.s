# Inicialização do estoque com alguns produtos predefinidos
estoque = {
    "maçã": 50,
    "banana": 100,
    "laranja": 75,
    "uva": 40
}

# Função para adicionar um novo produto ao estoque
def adicionar_produto(nome, quantidade):
    nome = nome.lower()
    if nome in estoque:
        print(f"O produto '{nome}' já existe no estoque. Use a opção de atualizar quantidade.")
    else:
        estoque[nome] = quantidade
        print(f"O produto '{nome}' foi adicionado ao estoque com {quantidade} unidades.")

# Função para atualizar a quantidade de um produto existente no estoque
def atualizar_produto(nome, quantidade):
    nome = nome.lower()
    if nome in estoque:
        estoque[nome] += quantidade
        print(f"A quantidade do produto '{nome}' foi atualizada para {estoque[nome]} unidades.")
    else:
        print(f"O produto '{nome}' não existe no estoque. Use a opção de adicionar produto.")

# Função para consultar a quantidade disponível de um produto
def consultar_produto(nome):
    nome = nome.lower()
    if nome in estoque:
        print(f"O produto '{nome}' tem {estoque[nome]} unidades disponíveis no estoque.")
    else:
        print(f"O produto '{nome}' não foi encontrado no estoque.")

# Função para exibir o menu e obter a escolha do usuário
def exibir_menu():
    print("\nGerenciamento de Estoque")
    print("1. Adicionar Produto")
    print("2. Atualizar Quantidade de Produto")
    print("3. Consultar Quantidade de Produto")
    print("4. Sair")
    return input("Escolha uma opção: ")

# Loop principal do menu
while True:
    opcao = exibir_menu()
    
    if opcao == '1':
        nome = input("Nome do Produto: ")
        quantidade = int(input("Quantidade do Produto: "))
        adicionar_produto(nome, quantidade)
    elif opcao == '2':
        nome = input("Nome do Produto: ")
        quantidade = int(input("Quantidade a Adicionar: "))
        atualizar_produto(nome, quantidade)
    elif opcao == '3':
        nome = input("Nome do Produto: ")
        consultar_produto(nome)
    elif opcao == '4':
        print("Saindo do sistema de gerenciamento de estoque. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")