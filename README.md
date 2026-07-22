# Controle de Gastos

Sistema de linha de comando (CLI) para cadastro e controle de gastos pessoais, desenvolvido em Python como projeto de estudo, aplicando conceitos de lógica de programação, persistência de dados e banco de dados relacional.

## Funcionalidades

- Cadastro de gastos com descrição, valor e categoria
- Listagem de todos os gastos cadastrados
- Cálculo automático do total de gastos por categoria
- Validação de entradas do usuário (impede valores inválidos ou campos vazios)
- Persistência de dados em banco de dados SQLite (os dados não se perdem ao fechar o programa)

## Tecnologias utilizadas

- **Python 3**
- **SQLite** (via módulo `sqlite3`, nativo do Python)

## Sobre o projeto

Este projeto foi construído em etapas, como forma de aplicar na prática os conceitos aprendidos no curso de Análise e Desenvolvimento de Sistemas:

1. **CRUD básico em memória** — lógica de programação com listas, dicionários e funções
2. **Persistência em arquivo JSON** — leitura e escrita de arquivos
3. **Tratamento de erros** — validação de entrada e tratamento de exceções (`try/except`)
4. **Migração para banco de dados SQLite** — modelagem de tabela e uso de comandos SQL (`INSERT`, `SELECT`, `GROUP BY`)

## Como executar

Pré-requisito: ter o [Python 3](https://www.python.org/) instalado.

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/controle-gastos.git

# Entre na pasta do projeto
cd controle-gastos

# Execute o programa
python main.py
```

## Como usar

Ao rodar o programa, um menu é exibido no terminal:

```
=== CONTROLE DE GASTOS ===
1 - Cadastrar gasto
2 - Listar gastos
3 - Ver total por categoria
4 - Sair
```

Basta digitar o número da opção desejada e seguir as instruções na tela.

## Possíveis melhorias futuras

- Interface gráfica com `tkinter`
- Filtro de gastos por período (data)
- Edição e exclusão de gastos cadastrados
- Exportação de relatórios em PDF ou Excel

## Autor

Desenvolvido por [Gabriel Pereira de Oliveira] — estudante de Análise e Desenvolvimento de Sistemas.

[LinkedIn](https://www.linkedin.com/in/gabriel-pereira-de-oliveira-ba1a06316/) · [GitHub](https://github.com/gabrielpe7)
