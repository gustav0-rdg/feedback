# Importando tudo que vai ser utilizado pelo Flask
from flask import Flask, render_template, request, redirect
# Importando datetime pra pegar o horario atual
import datetime
# Importando o mysql
import mysql.connector

# Criando a variavel para instanciar o Flask
app = Flask(__name__)

# Rota inicial
@app.route("/", methods=["GET"])
def pagina_inicial():
    return render_template("index.html")

# Rota para pegar as informações do formulario

@app.route("/post/comentarios", methods=["POST"])
def cadastrar_comentario():
    
    # Pegando as informações do input 

    username = request.form.get("nomeUsuario")
    comentario = request.form.get("comentario")
    dataHora = datetime.datetime.today()

    # Cadastrando informações no banco de dados

    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database = "dbFeedback"
    )

    cursorDb = conexao.cursor()
    # Comando do sql que sera executado
    sql = """INSERT INTO tbComentarios (username, comentarios, dataHora) 
            VALUES (%s, %s, %s)"""
    # Valores que serao inseridos no sql
    valores = (username, comentario, dataHora)
    # Executando o comando (sql (comando), valores(valores))
    cursorDb.execute(sql, valores)
    # completando a inserção no banco de dados
    conexao.commit()
    # fechando a conexao
    conexao.close()
    cursorDb.close()
    return redirect("/")


app.run(debug=True, host="0.0.0.0", port=8080)