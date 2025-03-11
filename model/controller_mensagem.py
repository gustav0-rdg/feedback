import mysql.connector
import datetime
# Importando classe que cria a conexao
from data.conexao import Conexao


class Mensagem:
    def cadastrar_mensagem(usuario, mensagem):
        dataHora = datetime.datetime.today()

        # Cadastrando informações no banco de dados
        conexao = Conexao.criar_conexao()

        cursorDb = conexao.cursor()
        # Comando do sql que sera executado
        sql = """INSERT INTO tbComentarios (username, comentarios, dataHora) 
                VALUES (%s, %s, %s)"""
        # Valores que serao inseridos no sql
        valores = (usuario, mensagem, dataHora)
        # Executando o comando (sql (comando), valores(valores))
        cursorDb.execute(sql, valores)
        # completando a inserção no banco de dados
        conexao.commit()
        # fechando a conexao
        conexao.close()
        cursorDb.close()
    
    def recuperar_mensagens():
        # Criar Conexao
        conexao = Conexao.criar_conexao()
        cursorDb = conexao.cursor(dictionary=True)
        # Codigo SQL
        sql = """select username, comentarios from tbComentarios;"""
        # Executando o comando 
        cursorDb.execute(sql)
        # Recuperando os dados e guardando em uma variavel
        resultado = cursorDb.fetchall()
        # Fechando a conexao
        conexao.close()
        cursorDb.close()

        return resultado
    
# Teste
    
