lista_de_compras = []
totalProdutos = 0

def adicionar_produto():
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade: "))
    valor_unitario = float(input("Digite o valor unitário: "))
    total = quantidade * valor_unitario
    produto = {"nome": nome, "quantidade": quantidade, "valor_unitario": valor_unitario, "total": total}
    lista_de_compras.append(produto)
    atualizar_total()

def ver_lista_de_produtos():
    if not lista_de_compras:
        print("A lista de compras está vazia.")
    else:
        for produto in lista_de_compras:
            print(f"Produto: {produto['nome']}, Quantidade: {produto['quantidade']}, Valor Unitário: {produto['valor_unitario']}, Total: {produto['total']}")
        print(f"Total de todos os produtos: {totalProdutos}")

def atualizar_produto():
    nome = input("Digite o nome do produto que deseja atualizar: ")
    for produto in lista_de_compras:
        if produto["nome"] == nome:
            quantidade = int(input("Digite a nova quantidade: "))
            valor_unitario = float(input("Digite o novo valor unitário: "))
            produto["quantidade"] = quantidade
            produto["valor_unitario"] = valor_unitario
            produto["total"] = quantidade * valor_unitario
            atualizar_total()
            print("Produto atualizado com sucesso.")
            return
    print("Produto não encontrado na lista.")

def remover_produto():
    nome = input("Digite o nome do produto que deseja remover: ")
    for produto in lista_de_compras:
        if produto["nome"] == nome:
            lista_de_compras.remove(produto)
            atualizar_total()
            print("Produto removido com sucesso.")
            return
    print("Produto não encontrado na lista.")

def atualizar_total():
    global totalProdutos
    totalProdutos = sum(produto["total"] for produto in lista_de_compras)

while True:
    print("\nOpções:")
    print("1. Adicionar produto")
    print("2. Ver lista de produtos")
    print("3. Atualizar produto")
    print("4. Remover produto")
    print("5. Encerrar programa")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_produto()
    elif opcao == "2":
        ver_lista_de_produtos()
    elif opcao == "3":
        atualizar_produto()
    elif opcao == "4":
        remover_produto()
    elif opcao == "5":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.")
