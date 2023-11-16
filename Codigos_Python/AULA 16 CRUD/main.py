from BibliotecaCRUD import *

opc = "s"

while opc in "sS":

    print(banco)

    opcMenu = int(input('''
                    MENU:
                        Informe qual tabela você deseja trabalhar.
                    1 - Alunos;
                    2 - Modalidades;
                    3 - Funcionarios;
                    4 - Personal;
                    5 - Sair.\n
                        Informe: '''))

    if opcMenu == 1:
        opcTable = int(input('''MENU:
                            Informe a função que você deseja trabalhar na tabela Alunos: 
                        1 - Cadastrar Colunas na Tabelas;
                        2 - Modificar Tabelas;
                        3 - Inserir Dados na Tabela;
                        4 - Deletar Dados na Tabela;
                        5 - Mostrar Dados da Tabela;
                        6 - Voltar para o MENU INICIAL.
                            '''))
        if opcTable == 1:
            nome = input("Informe o nome da coluna que você deseja, adicionar na tabela: ")
            tipo = input("Informe o tipo da sua nova coluna: ")
            CREATE(nome, tipo)

        elif opcTable == 2:


        elif opcTable == 3:
            descTable()
            onde = input("Deseja inserir em qual coluna ?")
            dados = input("Informe o Gênero Sexual (M/F) do aluno(a): ")
            InsertInTo(onde, dados)

        elif opcTable == 4:
            deletar = int(input("Insira a matricula do aluno que você deseja excluir da nossa Base de Dados: ")
            DELETE(deletar)

        elif opcTable == 5:
            SELECT()

    elif opcMenu == 5:
        opcMenu = input("Ainda deseja continuar a utilizar nossos serviços (s/n)? ")