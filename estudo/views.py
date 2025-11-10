from estudo import app
from flask import render_template, url_for

@app.route('/')
def homepage():
    usuario = 'Alexsandro'
    idade = 34

    context = {
        'usuario': 'Alex',
        'idade': 45
    }
    return render_template("index.html", context=context)

@app.route('/nova/')
def novapagina():
    return "Outra view"