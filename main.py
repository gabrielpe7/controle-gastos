import json

ARQUIVO = "gastos.json"
gastos = []


def cadastrar_gasto():
    descricao = input("Descrição do gasto:")
    valor = float(input("Valor (ex: 25.90):"))
    categoria = input("Categoria (ex: alimentação, transporte):")

    gasto = {
        "descricao": descricao,
        "valor": valor,
        "categoria": categoria
    }

    gastos.append(gasto)
    salvar_dados()
    print("Gasto cadastrado com sucesso!\n")

def listar_gastos():
    if len(gastos) == 0:
        print("Nenhum gasto cadastrado ainda.\n")
        return
        
    for gasto in gastos:
        print(f"- {gasto['descricao']} | R$ {gasto['valor']:.2f} | {gasto['categoria']}")
    print()

def total_por_categoria():
    totais = {}

    for gasto in gastos:
        categoria = gasto["categoria"]
        valor = gasto["valor"]

        if categoria in totais:
            totais[categoria] = totais[categoria] + valor
        else:
            totais[categoria] = valor

    for categoria, total in totais.items():
        print(f"- {categoria}: R$ {total:.2f}")
    print()

def salvar_dados():
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(gastos, arquivo, ensure_ascii=False, indent=4)

def carregar_dados():
    global gastos
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            gastos = json.load(arquivo)
    except FileNotFoundError:
        gastos = []

def menu():
    while True:
        print("=== CONTROLE DE GASTOS ===")
        print("1 - Cadastrar gasto")
        print("2 - Listar gastos")
        print("3 - Ver total por categoria")
        print("4 - Sair")

        opcao = input("Escolha uma opção:")

        if opcao == "1":
            cadastrar_gasto()
        elif opcao == "2":
            listar_gastos()
        elif opcao == "3":
            total_por_categoria()
        elif opcao == "4":
            print("Até mais!")
            break
        else:
            print("Opção inválida, tente novamente.\n")

carregar_dados()
menu()