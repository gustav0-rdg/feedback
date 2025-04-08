import mysql.connector
import datetime
# Importando classe que cria a conexao
from data.conexao import Conexao
from hashlib import sha256
from flask import session
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

    def logar(usuario, senha):
        # Criando a conexão
        senha = sha256(senha.encode()).hexdigest()

        conexao = Conexao.criar_conexao()

        try:
            with conexao.cursor(dictionary=True) as cursorDb:
                sql = """
                        SELECT login, nome
                        FROM tb_usuarios
                        WHERE login = %s
                        AND BINARY senha = %s;
                    """
                valores = (usuario, senha)

                cursorDb.execute(sql, valores)
                resultado = cursorDb.fetchall()

                if resultado:
                    session['usuario'] = resultado[0]['login']
                    session['nome'] = resultado[0]['nome']
                    return True
                else:
                    return False
        except mysql.connector.Error as err:
            print(f"Erro no banco de dados: {err}")
            return False
        finally:
            conexao.close()
            
    def logoff():
        session.clear()