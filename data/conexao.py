import mysql.connector
import datetime

class Conexao:
    # Criando conexao
    def criar_conexao():
        conexao = mysql.connector.connect(
            host="10.110.134.2",
            port=3306,
            user="3ds",
            password="banana",
            database = "db_feedback"
        )

        return conexao

