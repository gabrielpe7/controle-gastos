import sqlite3

ARQUIVO = "gastos.db"


def criar_tabela():
    conexao = sqlite3.connect(ARQUIVO)
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS gastos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            valor REAL NOT NULL,
            categoria TEXT NOT NULL
        )
    """)
    conexao.commit()
    conexao.close()


def pedir_valor():
    while True:
        entrada = input("Valor (ex: 25.90): ")
        try:
            valor = float(entrada)
            if valor <= 0:
                print("O valor precisa ser maior que zero. Tente novamente.")
                continue
            return valor
        except ValueError:
            print("Valor inválido. Digite apenas números (ex: 25.90).")


def pedir_texto(mensagem):
    while True:
        texto = input(mensagem)
        if texto.strip() == "":
            print("Esse campo não pode ficar vazio. Tente novamente.")
        else:
            return texto


def cadastrar_gasto():
    descricao = pedir_texto("Descrição do gasto: ")
    valor = pedir_valor()
    categoria = pedir_texto("Categoria (ex: alimentação, transporte): ")

    conexao = sqlite3.connect(ARQUIVO)
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO gastos (descricao, valor, categoria) VALUES (?, ?, ?)",
        (descricao, valor, categoria)
    )
    conexao.commit()
    conexao.close()

    print("Gasto cadastrado com sucesso!\n")


def listar_gastos():
    conexao = sqlite3.connect(ARQUIVO)
    cursor = conexao.cursor()
    cursor.execute("SELECT descricao, valor, categoria FROM gastos")
    resultados = cursor.fetchall()
    conexao.close()

    if len(resultados) == 0:
        print("Nenhum gasto cadastrado ainda.\n")
        return

    for linha in resultados:
        descricao, valor, categoria = linha
        print(f"- {descricao} | R$ {valor:.2f} | {categoria}")
    print()


def total_por_categoria():
    conexao = sqlite3.connect(ARQUIVO)
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT categoria, SUM(valor)
        FROM gastos
        GROUP BY categoria
    """)
    resultados = cursor.fetchall()
    conexao.close()

    if len(resultados) == 0:
        print("Nenhum gasto cadastrado ainda.\n")
        return

    for linha in resultados:
        categoria, total = linha
        print(f"- {categoria}: R$ {total:.2f}")
    print()


def menu():
    while True:
        print("=== CONTROLE DE GASTOS ===")
        print("1 - Cadastrar gasto")
        print("2 - Listar gastos")
        print("3 - Ver total por categoria")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ").strip()

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


criar_tabela()
menu()