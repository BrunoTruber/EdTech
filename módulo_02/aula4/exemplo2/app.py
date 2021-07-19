from flask import Flask
from flask.templating import render_template

app = Flask(__name__)

@app.route("/")
def index():
    nome = input('digite seu nome: ')
    idade = 25
    if idade >= 18:
        maiordeidade= True
    else:
        maiordeidade = False
    cidade = "Curitiba"
    return render_template("index.html",nome=nome,idade=idade,cidade=cidade,maiordeidade=maiordeidade)

if (__name__ == "__main__"):
    app.run(debug=True)