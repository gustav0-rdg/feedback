# Importando tudo que vai ser utilizado pelo Flask
from flask import Flask, render_template, request, redirect, session
# Importando datetime pra pegar o horario atual
import datetime
# Importando o mysql
import mysql.connector
# Importando classe para criar conexao
from data.conexao import Conexao
# Importando classe que envia a mensagem para o banco de dados
from model.controller_mensagem import Mensagem
from model.controller_usuario import Usuario
from hashlib import sha256
# Criando a variavel para instanciar o Flask
app = Flask(__name__)

app.secret_key = "balofosgogo"
# Rota inicial
@app.route("/")
def pagina_login():
    return render_template("login.html")

@app.route("/mensagem", methods=["GET"])
def pagina_inicial():
    if "usuario" in session:
        mensagens = Mensagem.recuperar_mensagens()
        return render_template("index.html", mensagens = mensagens)
    else:
        return redirect("/")

# Rota para pegar as informações do formulario

@app.route("/post/comentarios", methods=["POST"])
def cadastrar_comentario():
    
    # Pegando as informações do input 

    username = request.form.get("nomeUsuario")
    mensagem = request.form.get("mensagem")
   
    # Importando a funcao da classe para enviar a mensagem
    Mensagem.cadastrar_mensagem(username, mensagem)
    return redirect("/mensagem")

@app.route("/delete/mensagem/<codigo>")
def excluir_comentario(codigo):
    Mensagem.excluir_mensagem(codigo)
    return redirect("/mensagem")

@app.route("/aumenta/mensagem/<codigo>")
def aumentar_curtidas(codigo):
    Mensagem.add_likes(codigo)
    return redirect("/mensagem")

@app.route("/diminui/mensagem/<codigo>")
def remover_curtidas(codigo):
    Mensagem.remove_likes(codigo)
    return redirect("/mensagem")

@app.route("/cadastrar")
def cadastrar_usuario():
    return render_template("cadastrar.html")

@app.route("/cadastrar/usuario", methods=["POST"])
def add_usuario():
    username = request.form.get("usuario")
    nome = request.form.get("nome")
    senha = request.form.get("senha")
    Usuario.cadastrar_usuario(username, nome, senha)
    return redirect("/")

@app.route("/post/logar", methods=["POST"])
def post_logar():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    esta_logado = Usuario.logar(usuario, senha)
    
    if esta_logado:
        return redirect('/mensagem')
    else:
        return redirect('/')

@app.route("/sair/usuario", methods=["GET"])
def logoff():
    Usuario.logoff()
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)