import mysql.connector

banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "302302",
    database = "academiaturmad"
)
print(banco)

def SELECT(tabela):
    meucursor = banco.cursor()
    pesquisa = "select * from (%s);"
    data = (tabela)
    meucursor.execute(data, pesquisa)
    resultado = meucursor.fetchall()

    for e in resultado:
        print(e)

    banco.commit()
    meucursor.close()
    
def MODIFY(tabela, coluna, tipo):
    print("Você selecionou a opção para modificar os dados contidos na tabela.")
    meucursor = banco.cursor()
    sql = "alter table (%s) modify column (%s) (%s);"
    data =(tabela, coluna, tipo)
    meucursor.execute(sql, data)
    banco.commit()
    meucursor.close()

def InsertInTo(tabela, coluna, dados):
    print("Você selecionou a opção de inserir dados!")
    meucursor = banco.cursor()
    sql = "insert into (%s) (%s) values (%s);"
    data = (tabela, coluna, dados)
    meucursor.execute(sql, data)
    banco.commit()
    meucursor.close()

def DELETE(tabela, deletar):
    print("Você selecionou a opção de deletar dados!")
    meucursor = banco.cursor()
    sql = "delete from (%s) where (%s);"
    data = (tabela, deletar)
    meucursor.execute(sql, data)
    banco.commit()
    meucursor.close()

def CREATE(tabela, nome, tipo):
    print("Você selecionou a opção de criar mais uma coluna para a tabelas!")
    meucursor = banco.cursor()
    sql = "alter table (%s) ADD (%s) (%s) not null;"
    data = (tabela, nome, tipo)
    meucursor.execute(sql, data)
    banco.commit()
    meucursor.close()

def descTable(tabela):
    meucursor = banco.cursor()
    pesquisa = "desc (%s);"
    data = (tabela)
    meucursor.execute(pesquisa, data)
    resultado = meucursor.fetchall()
    print(resultado)
    banco.commit()
    meucursor.close()

def encerrarBD():
    banco.close()