from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sobre')
def sobre():
    return render_template("sobre.html")

@app.route('/contato')
def contato():
    return render_template("contato.html")

@app.route('/')
def escolha():
    return render_template("escolha.html")

@app.route('/')
def perguntas():
    return render_template("perguntas.html")

@app.route('/quiz')
def quiz():
    return render_template("quiz.html")



if __name__ == '__main__':
    app.run(debug=True)