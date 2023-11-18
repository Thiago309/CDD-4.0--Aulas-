from BibliotecaCRUD import *

opc = "s"
opcTable = 0

while opc in "sS":

    print(banco)

    opcMenu = input('''
                    \nMENU:
                        Informe qual tabela você deseja trabalhar.
                        alunos;
                        modalidades;
                        funcionarios;
                        personal;\n
                        informe: ''')

    while opcTable != 6:

        opcTable = int(input('''
                            \nMENU:
                            Informe a função que você deseja trabalhar na tabela Alunos: 
                        1 - Cadastrar Colunas na Tabelas;
                        2 - Modificar Tabelas;
                        3 - Inserir Dados na Tabela;
                        4 - Deletar Dados na Tabela;
                        5 - Mostrar Dados da Tabela;
                        6 - Voltar para o MENU INICIAL.
                            '''))
        tabela = opcMenu

        if opcTable == 1:
            nome = input("Informe o nome da coluna que você deseja, adicionar na tabela: ")
            tipo = input("Informe o tipo da sua nova coluna: ")
            CREATE(tabela, nome, tipo)

        elif opcTable == 2:
            descTable(tabela)
            coluna = input("Informe qual a coluna que você deseja modificar o tipo: ")
            tipo = input("Informe qual o tipo da coluna a ser alterada Ex.:[varchar(11)]: ")
            MODIFY(tabela, coluna, tipo)

        elif opcTable == 3:
            descTable(tabela)
            coluna = input("Deseja inserir em qual coluna ?")
            dados = input("Informe o dado que você deseja inserir na tabela: ")
            InsertInTo(tabela, coluna, dados)

        elif opcTable == 4:
            descTable(tabela)
            deletar = int(input("Insira o id que você deseja excluir da nossa Base de Dados: "))
            DELETE(tabela, deletar)

        elif opcTable == 5:
            SELECT(tabela)

        elif opcTable == 6:
            break

        else:
            print("Por favor, insira a opção correta !\n")

    opcMenu = input("Ainda deseja continuar a utilizar nossos serviços (s/n)? ")

encerrarBD()
print("Data Base desconecting ...")