import mysql.connector
import datetime

class Conexao:
    # Criando conexao
    def criar_conexao():
        conexao = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="root",
            database = "dbFeedback"
        )

        return conexao

