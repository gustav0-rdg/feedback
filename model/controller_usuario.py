import mysql.connector
import datetime
# Importando classe que cria a conexao
from data.conexao import Conexao
from hashlib import sha256
class Usuario:
    def cadastrar_usuario(usuario, nome, senha):
        # Criptografando a Senha
        senha = sha256(senha.encode()).hexdigest()
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

    def logar(usuario, senha):
        # Criando a conexão
        senha= sha256(senha.encode()).hexdigest
        conexao = Conexao.criar_conexao()

        cursorDb = conexao.cursor(dictionary=True)
        sql = """
                SELECT login, senha 
                FROM tb_usuarios
                WHERE LOGIN = %s
                AND BINARY SENHA = %s;
                """
        
        valores = (usuario, senha)

        cursorDb.execute(sql, valores)
        resultado = cursorDb.fetchall()
        conexao.close()
        cursorDb.close()

        return resultado