import mysql.connector
import datetime

class Conexao:
    # Criando conexao
    def criar_conexao():
        conexao = mysql.connector.connect(
            host="bd-godofredo-alexstocco-93db.b.aivencloud.com",
            port=27974,
            user="3ds",
            password="banana",
            database = "db_feedback"
        )

        return conexao

