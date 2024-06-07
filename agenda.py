# Inicialização da agenda telefônica com alguns contatos predefinidos
agenda = [
    {"nome": "João Silva", "numero": "1111-1111"},
    {"nome": "Maria Souza", "numero": "2222-2222"},
    {"nome": "Carlos Pereira", "numero": "3333-3333"},
    {"nome": "Ana Martins", "numero": "4444-4444"},
    {"nome": "Pedro Alves", "numero": "5555-5555"}
]

# Função para adicionar um novo contato à agenda telefônica
def adicionar_contato(nome, numero):
    # Verificar se o contato já existe na agenda
    for contato in agenda:
        if contato["nome"].lower() == nome.lower():
            print(f"O contato '{nome}' já existe na agenda.")
            return
    # Adicionar o novo contato
    novo_contato = {"nome": nome, "numero": numero}
    agenda.append(novo_contato)
    print(f"O contato '{nome}' foi adicionado à agenda.")

# Função para buscar um contato pelo nome
def buscar_contato(nome):
    for contato in agenda:
        if contato["nome"].lower() == nome.lower():
            print(f"Nome: {contato['nome']}\nNúmero: {contato['numero']}")
            return
    print(f"O contato '{nome}' não foi encontrado na agenda.")

# Função para listar todos os contatos da agenda
def listar_contatos():
    if not agenda:
        print("A agenda está vazia.")
    else:
        for contato in agenda:
            print(f"Nome: {contato['nome']}, Número: {contato['numero']}")

# Função para exibir o menu e obter a escolha do usuário
def exibir_menu():
    print("\nAgenda Telefônica")
    print("1. Adicionar Contato")
    print("2. Buscar Contato")
    print("3. Listar Contatos")
    print("4. Sair")
    return input("Escolha uma opção: ")

# Loop principal do menu
while True:
    opcao = exibir_menu()
    
    if opcao == '1':
        nome = input("Nome do Contato: ")
        numero = input("Número do Contato: ")
        adicionar_contato(nome, numero)
    elif opcao == '2':
        nome = input("Nome do Contato: ")
        buscar_contato(nome)
    elif opcao == '3':
        listar_contatos()
    elif opcao == '4':
        print("Saindo da agenda telefônica. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")