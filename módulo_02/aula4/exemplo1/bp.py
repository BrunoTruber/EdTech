from flask import Blueprint, render_template

bp = Blueprint("bp",__name__)

@bp.route("/")
def home():
    return "<h1>hollo world, ok"

@bp.route("/login/<nome>")
def login(nome=None):
    return "<center><h1>Ola, "+nome+" <br> faça seu login</center>"

@bp.route("/classe/")
def carrega():
    return render_template("index.html")