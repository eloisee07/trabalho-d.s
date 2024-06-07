# Dicionário de traduções
tradutor = {
    "casa": "house",
    "gato": "cat",
    "cachorro": "dog",
    "livro": "book",
    "carro": "car",
    "árvore": "tree",
    "sol": "sun",
    "lua": "moon",
    "água": "water",
    "fogo": "fire"
}

# Função para traduzir uma palavra
def traduzir_palavra(palavra):
    palavra = palavra.lower()
    if palavra in tradutor:
        print(f"A tradução de '{palavra}' é '{tradutor[palavra]}'.")
    else:
        print(f"A palavra '{palavra}' não foi encontrada no dicionário.")

# Função para exibir o menu e obter a escolha do usuário
def exibir_menu():
    print("\nTradutor Simples")
    print("1. Traduzir Palavra")
    print("2. Sair")
    return input("Escolha uma opção: ")

# Loop principal do menu
while True:
    opcao = exibir_menu()
    
    if opcao == '1':
        palavra = input("Digite a palavra a ser traduzida: ")
        traduzir_palavra(palavra)
    elif opcao == '2':
        print("Saindo do tradutor. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")