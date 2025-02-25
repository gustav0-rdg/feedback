# Importando tudo que vai ser utilizado pelo Flask
from flask import Flask, render_template, request, redirect

# Criando a variavel para instanciar o Flask
app = Flask(__name__)

# Rota inicial
@app.route("/", methods=["GET"])
def pagina_inicial():
    return render_template("index.html")

app.run(debug=True, host="0.0.0.0", port=8080)