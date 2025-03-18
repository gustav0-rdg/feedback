# Importando tudo que vai ser utilizado pelo Flask
from flask import Flask, render_template, request, redirect
# Importando datetime pra pegar o horario atual
import datetime
# Importando o mysql
import mysql.connector
# Importando classe para criar conexao
from data.conexao import Conexao
# Importando classe que envia a mensagem para o banco de dados
from model.controller_mensagem import Mensagem
# Criando a variavel para instanciar o Flask
app = Flask(__name__)

# Rota inicial
@app.route("/", methods=["GET"])
def pagina_inicial():
    mensagens = Mensagem.recuperar_mensagens()
    return render_template("index.html", mensagens = mensagens)

# Rota para pegar as informações do formulario

@app.route("/post/comentarios", methods=["POST"])
def cadastrar_comentario():
    
    # Pegando as informações do input 

    username = request.form.get("nomeUsuario")
    mensagem = request.form.get("mensagem")
   
    # Importando a funcao da classe para enviar a mensagem
    Mensagem.cadastrar_mensagem(username, mensagem)
    return redirect("/")

@app.route("/delete/mensagem/<codigo>")
def excluir_comentario(codigo):
    return redirect("/")
    
app.run(debug=True, host="0.0.0.0", port=8080)