import mysql.connector
import datetime
# Importando classe que cria a conexao
from data.conexao import Conexao

class Usuario:
    def cadastrar_usuario(usuario, nome, senha):
        # Cadastrando informações no banco de dados
        conexao = Conexao.criar_conexao()

        cursorDb = conexao.cursor()
        # Comando do sql que sera executado
        sql = """INSERT INTO tb_usuarios (login, nome, senha) 
                VALUES (%s, %s, %s)"""
        # Valores que serao inseridos no sql
        valores = (usuario, nome, senha)
        # Executando o comando (sql (comando), valores(valores))
        cursorDb.execute(sql, valores)
        # completando a inserção no banco de dados
        conexao.commit()
        # fechando a conexao
        conexao.close()
        cursorDb.close()