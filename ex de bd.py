import sqlite3

conn = sqlite3.connect("ex.txt")

cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS titulos(codigo INTEGER PRIMARY KEY NOT NULL, nome TEXT NOT NULL, quantidade INTEGER NOT NULL, cod_editora INTEGER NOT NULL);")
cursor.execute("CREATE TABLE IF NOT EXISTS TituloAutor(cod_titulo INTEGER NOT NULL, cod_autor INTEGER NOT NULL);")
cursor.execute("CREATE TABLE IF NOT EXISTS autores(codigo INTEGER PRIMARY KEY NOT NULL, nome TEXT NOT NULL, telefone INTEGER, endereco INTEGER);")
cursor.execute("CREATE TABLE IF NOT EXISTS editoras(codigo INTEGER PRIMARY KEY NOT NULL, nome TEXT NOT NULL, telefone INTEGER, endereco INTEGER);")
cursor.execute("CREATE TABLE IF NOT EXISTS usuarios(codigo INTEGER PRIMARY KEY NOT NULL, nome TEXT NOT NULL, telefone INTEGER NOT NULL, endereco TEXT NOT NULL, atividade TEXT);")
cursor.execute("CREATE TABLE IF NOT EXISTS emprestimos(cod_usuario INTEGER NOT NULL, cod_titulo INTEGER NOT NULL, data_emprestimo TEXT , data_devolucao TEXT);")
#cursor.execute("ALTER TABLE titulos ADD COLUMN ano INTEGER;")
#cursor.execute("ALTER TABLE usuarios RENAME TO clientes;")

def cad_livro():
    cod = input('informe o codigo do livro')
    n = raw_input('informe o nome do livro')
    q = input('informe a quantidade de livros')
    ed = input('informe o codigo da editora do livro')
    cursor.execute("INSERT INTO titulos(codigo, nome, quantidade, cod_editora) VALUES(?,?,?,?);",(cod, n, q, ed))
    conn.commit()

def cad_ed():
    cod = input('informe o codigo da editora')
    n = raw_input('informe o nome da editora')
    t = input('informe o telefone da editora')
    e = raw_input('informe o endereco da editora')
    cursor.execute("INSERT INTO editoras(codigo, nome, telefone, endereco) VALUES(?,?,?,?);",(cod, n, t, e))

def cad_aut():
    cod = input('informe o codigo do autor')
    n = raw_input('informe o nome do autor')
    t = input('informe o telefone do autor')
    e = raw_input('informe o endereco do autor')
    cursor.execute("INSERT INTO autores(codigo, nome, telefone, endereco) VALUES(?,?,?,?);",(cod, n, t, e))

def alt_livro():
    cursor.execute("SELECT * FROM titulos;")
    vetor = cursor.fetchall()
    for n in vetor:
        print(n)
    cod = input('informe o codigo novo do livro')
    n = raw_input('informe o nome novo do livro')
    q = input('informe a quantidade novo de livros')
    ed = input('informe o codigo novo da editora do livro')
    l = raw_input('qual o codigo do livro que voce deseja alterar?')
    cursor.execute("UPDATE titulos SET codigo = ?, nome = ?, quantidade = ?, cod_editora = ? WHERE codigo = ?;",(cod,n,q,ed,l))

def alt_ed():
    cursor.execute("SELECT * FROM editoras;")
    for n in cursor.fetchall():
        print(n)
    cod = input('informe o codigo novo da editora')
    n = raw_input('informe o nome novo da editora')
    t = input('informe o telefone novo da editora')
    e = raw_input('informe o endereco novo da editora')
    l = input('qual o codigo dq editora que voce deseja alterar?')
    cursor.execute("UPDATE editoras SET codigo = ?, nome = ?, telefone = ?, endereco = ? WHERE codigo = ?;",(cod,n,t,e,l))

def alt_aut():
    cursor.execute("SELECT * FROM autores;")
    for n in cursor.fetchall():
        print(n)
    cod = input('informe o codigo novo do autor')
    n = raw_input('informe o nome novo do autor')
    t = input('informe o telefone novo do autor')
    e = raw_input('informe o endereco novo do autor')
    l = input('qual o codigo do autor que voce deseja alterar?')
    cursor.execute("UPDATE autores SET codigo = ?, nome = ?, telefone = ?, endereco = ? WHERE codigo = ?;",(cod,n,t,e,l))

def exc_livro():
    cursor.execute("SELECT * FROM titulos;")
    for n in cursor.fetchall():
        print(n)
    l = input('Qual codigo do livro que deseja excluir')
    cursor.execute("DELETE FROM titulos WHERE codigo=?;",(l,))

def exc_ed():
    cursor.execute("SELECT * FROM editoras;")
    for n in cursor.fetchall():
        print(n)
    l = input('Qual codigo da editora que deseja excluir')
    cursor.execute("DELETE FROM editoras WHERE codigo = ?;", (l,))


def exc_aut():
    cursor.execute("SELECT * FROM autores;")
    for n in cursor.fetchall():
        print(n)
    l = input('Qual codigo do autor que deseja excluir')
    cursor.execute("DELETE FROM autores WHERE codigo = ?;", (l,))


def list_liv():
    cursor.execute("SELECT * FROM titulos;")
    for n in cursor.fetchall():
        print(n)

def list_ed():
    cursor.execute("SELECT * FROM editoras;")
    for n in cursor.fetchall():
        print(n)

def list_aut():
    cursor.execute("SELECT * FROM autores;")
    for n in cursor.fetchall():
        print(n)


def emprestimo():
    cursor.execute("SELECT * FROM titulos;")
    vetor = cursor.fetchall()
    for n in vetor:
        print(n)

    codigo = raw_input('qual codigo do livro que deseja pegar emprestado?')
    quantidade = input('qual a quantidade?')  # type: object
    cod_usu = input('informe o codigo do usuario')
    data_emp = raw_input('informe a data do emprestimo')
    cursor.execute("INSERT INTO emprestimos(cod_usuario, cod_titulo, data_emprestimo) VALUES(?,?,?);", (cod_usu, codigo, data_emp))

    cursor.execute("SELECT quantidade FROM titulos WHERE codigo = {0};".format(codigo))
    q = cursor.fetchall()[0][0]
    # cursor.execute("SELECT * FROM titulos;")
    if (q < quantidade):
        print('nao temos essa quantidade')
    else:
        print 'livro emprestado'
        cursor.execute("UPDATE titulos SET quantidade = ? WHERE codigo = ?;", ((q-quantidade), codigo))

def dev_livro():
    cursor.execute("SELECT * FROM titulos;")
    vetor = cursor.fetchall()
    for n in vetor:
        print(n)
    codigo = raw_input('qual codigo do livro que deseja devolver?')
    quantidade = input('qual a quantidade que deseja devolver?')  # type: object
    cod_usu = input('informe o codigo do usuario')
    data_dev = raw_input('informe a data da devolucao')
    cursor.execute("UPDATE emprestimos SET data_devolucao = ? WHERE cod_usuario = ?;", (data_dev, cod_usu))
    cursor.execute("SELECT quantidade FROM titulos WHERE codigo = {0};".format(codigo))
    q = cursor.fetchall()[0][0]
    print 'livro devolvido'
    cursor.execute("UPDATE titulos SET quantidade = ? WHERE codigo = ?;", ((q + quantidade), codigo))

c = 0
while c != 15:
    c = input('1 - CADASTRAR LIVRO\n'
              '2 - CADASTRAR EDITORA\n'
              '3 - CADASTRAR AUTORES\n'
              '4 - ALTERAR LIVRO\n'
              '5 - ALTERAR EDITORA\n'
              '6 - ALTERAR AUTORES\n'
              '7 - EXCLUIR LIVRO\n'
              '8 - EXCLUIR EDITORA\n'
              '9 - EXCLUIR AUTORES\n'
              '10- LISTAR LIVROS\n'
              '11- LISTAR EDITORAS\n'
              '12- LISTAR AUTORES\n'
              '13- EMPRESTIMO\n'
              '14- DEVOLVER LIVRO\n'
              '15- SAIR\n'
              'OPCAO:')

    if c == 1:
        cad_livro()
    elif c == 2:
        cad_ed()
    elif c == 3:
        cad_aut()
    elif c == 4:
        alt_livro()
    elif c == 5:
        alt_ed()
    elif c == 6:
        alt_aut()
    elif c == 7:
        exc_livro()
    elif c == 8:
        exc_ed()
    elif c == 9:
        exc_aut()
    elif c == 10:
        list_liv()
    elif c == 11:
        list_ed()
    elif c == 12:
        list_aut()
    elif c == 13:
        emprestimo()
    elif c == 14:
        dev_livro()
    elif c == 15:
        break

conn.close()