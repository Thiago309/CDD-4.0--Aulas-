import mysql.connector

banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "302302",
    database = "academiaturmad"
)
print(banco)

def SELECT():
    meucursor = banco.cursor()
    pesquisa = "select * from alunos;"
    meucursor.execute(pesquisa)
    resultado = meucursor.fetchall()

    for e in resultado:
        print(e)
def MODIFY():
    print("Você selecionou a opção para modificar os dados contidos na tabela.")
    meucursor = banco.cursor()
    sql = ""
def InsertInTo(onde, dados):
    print("Você selecionou a opção de inserir dados!")
    meucursor = banco.cursor()
    sql = "insert into alunos (%s) values (%s);"
    data = (onde, dados)
    meucursor.execute(sql, data)
    banco.commit()
    meucursor.close()

def DELETE(deletar):
    print("Você selecionou a opção de deletar dados!")
    meucursor = banco.cursor()
    sql = "delete from alunos where (matricula);"
    data = (deletar)
    meucursor.execute(sql, data)
    banco.commit()
    meucursor.close()

def CREATE(nome, tipo):
    print("Você selecionou a opção de criar mais uma coluna para a tabelas!")
    meucursor = banco.cursor()
    sql = "alter table alunos ADD (%s, %s) not null;"
    data = (nome, tipo)
    meucursor.execute(sql, data)
    banco.commit()
    meucursor.close()

def descTable():
    meucursor = banco.cursor()
    pesquisa = "desc alunos;"
    meucursor.execute(pesquisa)
    print(pesquisa)