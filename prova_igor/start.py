from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/exemplo", methods=['POST'])
def exemplo():
    desenvolvedor = request.form['desenvolvedor']
    turma = request.form['turma']
    professor = request.form['professor']
    data = request.form['data']
    dificuldade = request.form['dificuldade']
    confiante = request.form['confiante']
    return render_template("exemplo.html", desenvolvedor=desenvolvedor, turma=turma, professor=professor, data=data, dificuldade=dificuldade, confiante=confiante)

