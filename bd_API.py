#importação da biblioteca comunicação com banco de dados sqlite3
import sqlite3
#importação de biblioteca para informar o caminho
from pathlib import Path
#indicação de caminho
ROOT_PATH = Path(__file__).parent
#criação de comunicação com banco de dados/criação do banco na mesma pasta
conexao=sqlite3.connect(ROOT_PATH/"meu_banco.db")  
#função de interação com o banco de dados
cursor =conexao.cursor()

#criação de funções para organização de código
def criar_tabela(conexao,cursor):
    #criação dos atributos da tabela
    cursor.execute("CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(180),email VARCHAR(150))")
    #envio dos dados ao banco
    conexao.commit()

def inserir_registro(conexao, cursor, nome, email):
    #criação de variável para armazenar dados
    data = (nome, email)
    #comando para inserção de dados no banco de dados
    cursor.execute("INSERT INTO clientes (nome, email) VALUES(?,?);",data)
    #envio dos dados ao banco
    conexao.commit()

def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    #comando para atualização de dados no banco de dados
    #CUIDADO COM WHERE
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;",data)
    
    #envio dos dados ao banco
    conexao.commit()
    
def excluir_registro(conexao, cursor, id):
    data = (id,)
    #comando para excluir de dados no banco de dados
    #CUIDADO COM WHERE
    cursor.execute("DELETE FROM clientes WHERE id=?",data)
    
    #envio dos dados ao banco
    conexao.commit()
    
def inserir_muitos(conexao, cursor, dados):
    #comando para inserção de uma lista de dados no banco de dados
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES(?,?);",dados)
    #envio dos dados ao banco
    conexao.commit()    
    

def dados_def():
    #criação de tuplas
    dados={
        ("Guilherme","guilherme@gmail.com"),
        ("Chappie","chapie@gmail.com"),
        ("Melanie","melanie@gmail.com"),
    }


def recuperar_cliente(cursor, id):
    #realizar buscas no banco de dados
    #pesquisa pode ser restrita, substituindo o * pelos atributos
    cursor.execute("SELECT * FROM clientes WHERE id=?",(id,))
    #retornar 1 registro / não precisa do commint
    return cursor.fetchone()



def recuperar_cliente_row(cursor, id):
    #realizar buscas no banco de dados
    #pesquisa pode ser restrita, substituindo o * pelos atributos
    cursor.row_factory = sqlite3.Row
    cursor.execute("SELECT * FROM clientes WHERE id=?",(id,))
    #retornar 1 registro / não precisa do commint
    return cursor.fetchone()


def listar_clientes(cursor):
    #realizar buscas no banco de dados com valor iterável
    #pesquisa pode ser restrita, substituindo o * pelos atributos
    return cursor.execute("SELECT * FROM clientes ORDER BY nome;")  #possibilidade consulta por ordenação
    

#chamndo função    
cliente = recuperar_cliente(cursor,2)
print(cliente)
#demostração de exibição iteravel
clientes=listar_clientes(cursor)
for cliente in clientes:
    print(cliente)
    
    
#utilizando cursor.row
#dessa forma é exibido de forma de dicionário
cliente=recuperar_cliente_row(cursor,2)
print(dict(cliente))