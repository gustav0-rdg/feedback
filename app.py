# Importando tudo que vai ser utilizado pelo Flask
from flask import Flask, render_template, request, redirect

# Criando a variavel para instanciar o Flask
app = Flask(__name__)

# Rota inicial
@app.route("/", methods=["GET"])
def pagina_inicial():
    return render_template("index.html")

# Rota para pegar as informações do formulario

@app.route("/post/comentarios", methods=["POST"])
def cadastrar_comentario():
    return redirect("/")
app.run(debug=True, host="0.0.0.0", port=8080)