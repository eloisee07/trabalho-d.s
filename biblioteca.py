# Inicialização da biblioteca com alguns livros predefinidos
biblioteca = [
    {"titulo": "Python Básico", "autor": "João Silva", "ano": 2021, "disponivel": True},
    {"titulo": "Algoritmos Avançados", "autor": "Maria Souza", "ano": 2019, "disponivel": True},
    {"titulo": "Machine Learning", "autor": "Carlos Pereira", "ano": 2020, "disponivel": True},
    {"titulo": "Data Science", "autor": "Ana Martins", "ano": 2018, "disponivel": True},
    {"titulo": "Deep Learning", "autor": "Pedro Alves", "ano": 2022, "disponivel": True}
]

# Função para adicionar um novo livro à biblioteca
def adicionar_livro(titulo, autor, ano):
    # Verificar se o livro já existe na biblioteca
    for livro in biblioteca:
        if livro["titulo"].lower() == titulo.lower():
            print(f"O livro '{titulo}' já existe na biblioteca.")
            return
    # Adicionar o novo livro
    novo_livro = {"titulo": titulo, "autor": autor, "ano": ano, "disponivel": True}
    biblioteca.append(novo_livro)
    print(f"O livro '{titulo}' foi adicionado à biblioteca.")

# Função para buscar um livro pelo título
def buscar_livro(titulo):
    for livro in biblioteca:
        if livro["titulo"].lower() == titulo.lower():
            disponivel = "Disponível" if livro["disponivel"] else "Emprestado"
            print(f"Título: {livro['titulo']}\nAutor: {livro['autor']}\nAno: {livro['ano']}\nStatus: {disponivel}")
            return
    print(f"O livro '{titulo}' não foi encontrado na biblioteca.")

# Função para listar todos os livros da biblioteca
def listar_livros():
    if not biblioteca:
        print("A biblioteca está vazia.")
    else:
        for livro in biblioteca:
            disponivel = "Disponível" if livro["disponivel"] else "Emprestado"
            print(f"Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}, Status: {disponivel}")

# Função para emprestar um livro
def emprestar_livro(titulo):
    for livro in biblioteca:
        if livro["titulo"].lower() == titulo.lower():
            if livro["disponivel"]:
                livro["disponivel"] = False
                print(f"O livro '{titulo}' foi emprestado com sucesso.")
            else:
                print(f"O livro '{titulo}' já está emprestado.")
            return
    print(f"O livro '{titulo}' não foi encontrado na biblioteca.")

# Função para devolver um livro
def devolver_livro(titulo):
    for livro in biblioteca:
        if livro["titulo"].lower() == titulo.lower():
            if not livro["disponivel"]:
                livro["disponivel"] = True
                print(f"O livro '{titulo}' foi devolvido com sucesso.")
            else:
                print(f"O livro '{titulo}' já estava disponível na biblioteca.")
            return
    print(f"O livro '{titulo}' não foi encontrado na biblioteca.")
    
# Função para exibir o menu e obter a escolha do usuário
def exibir_menu():
    print("\nGerenciamento de Biblioteca")
    print("1. Adicionar Livro")
    print("2. Buscar Livro")
    print("3. Listar Livros")
    print("4. Emprestar Livro")
    print("5. Devolver Livro")
    print("6. Sair")
    return input("Escolha uma opção: ")

# Loop principal do menu
while True:
    opcao = exibir_menu()
    
    if opcao == '1':
        titulo = input("Título do Livro: ")
        autor = input("Autor do Livro: ")
        ano = int(input("Ano de Publicação: "))
        adicionar_livro(titulo, autor, ano)
    elif opcao == '2':
        titulo = input("Título do Livro: ")
        buscar_livro(titulo)
    elif opcao == '3':
        listar_livros()
    elif opcao == '4':
        titulo = input("Título do Livro: ")
        emprestar_livro(titulo)
    elif opcao == '5':
        titulo = input("Título do Livro: ")
        devolver_livro(titulo)
    elif opcao == '6':
        print("Saindo do sistema. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")        