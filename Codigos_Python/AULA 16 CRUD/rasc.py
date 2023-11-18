# import mysql.connector
#
# banco = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "302302",
#     database = "academiaturmad"
# )
# print(banco)
#
# meucursor = banco.cursor()
# pesquisa = "select matricula, nome, CPF, telefone from alunos;"
# meucursor.execute(pesquisa)
# resultado = meucursor.fetchall()  # fetchall recebe tudo da pesquisa e retorna atraves de uma tupla
#
# for e in resultado:
#     print(e)

# nome1 = input("Informe o nome que deseja adicionar na Base de dados: ")
# telefone1 = int(input("Informe o telefone que voce deseja adicionar na Base de Dados: "))
# sql = "insert into alunos (nome, telefone) values (%s, %s)"
# data = (nome1, telefone1)
# meucursor.execute(sql, data)
# banco.commit()

# userid = meucursor.lastrowid
# print(userid)
#
# meucursor.close()
# banco.close()