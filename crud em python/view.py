import sqlite3 as lite


#criando conexao
con = lite.connect('dados.db')
#lista teste
lista = ['renato','renato@gmail.com',12314564, "12/19/2022",'Normal', "Gostaria de uma consulta"]

#inserindo informações
def inserindo_info(lista):
    with con:
        cur = con.cursor()
        query = "INSERT INTO formulario(nome, email, telefone, dia_em, estado, assunto) VALUES(?,?,?,?,?,?)"
        cur.execute(query, lista)

#acessando informações
def mostrar_info():
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM formulario"
        cur.execute(query)
        info = cur.fetchall()
        for i in info:
            lista.append(i)
    return lista



def atualiza_info(i):
    with con:
        cur= con.cursor()

        query = "UPDATE formulario SET nome=?, email=?, telefone=?, dia_em=?, estado=?, assunto=? WHERE id=?"

        cur.execute(query, i)

#DELETE
def deletar_info(i):
    with con:
        cur= con.cursor()
        query = "DELETE FROM formulario WHERE id=?"
        cur.execute(query,i)