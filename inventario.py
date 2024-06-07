# Inicialização do inventário com alguns itens predefinidos
inventario = {
    "poção de cura": 10,
    "espada de ferro": 1,
    "escudo de madeira": 1,
    "flecha": 30
}

# Função para adicionar itens ao inventário
def adicionar_item(nome, quantidade):
    nome = nome.lower()
    if nome in inventario:
        inventario[nome] += quantidade
    else:
        inventario[nome] = quantidade
    print(f"{quantidade} unidade(s) do item '{nome}' foi(foram) adicionada(s) ao inventário.")

# Função para remover itens do inventário
def remover_item(nome, quantidade):
    nome = nome.lower()
    if nome in inventario:
        if inventario[nome] >= quantidade:
            inventario[nome] -= quantidade
            if inventario[nome] == 0:
                del inventario[nome]
            print(f"{quantidade} unidade(s) do item '{nome}' foi(foram) removida(s) do inventário.")
        else:
            print(f"Quantidade insuficiente do item '{nome}' para remover.")
    else:
        print(f"O item '{nome}' não foi encontrado no inventário.")

# Função para exibir o inventário completo
def exibir_inventario():
    if not inventario:
        print("O inventário está vazio.")
    else:
        print("Inventário do Personagem:")
        for item, quantidade in inventario.items():
            print(f"{item}: {quantidade} unidade(s)")

# Função para exibir o menu e obter a escolha do usuário
def exibir_menu():
    print("\nGerenciamento de Inventário")
    print("1. Adicionar Item")
    print("2. Remover Item")
    print("3. Exibir Inventário Completo")
    print("4. Sair")
    return input("Escolha uma opção: ")

# Loop principal do menu
while True:
    opcao = exibir_menu()
    
    if opcao == '1':
        nome = input("Nome do Item: ")
        quantidade = int(input("Quantidade do Item: "))
        adicionar_item(nome, quantidade)
    elif opcao == '2':
        nome = input("Nome do Item: ")
        quantidade = int(input("Quantidade a Remover: "))
        remover_item(nome, quantidade)
    elif opcao == '3':
        exibir_inventario()
    elif opcao == '4':
        print("Saindo do sistema de gerenciamento de inventário. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")