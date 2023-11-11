import json
from flask import Flask, render_template, request

app = Flask(__name__)

# Lê as perguntas do arquivo JSON
with open('data/perguntas.json', 'r', encoding='utf-8') as file:
    questions = json.load(file)

# Função para simular o comportamento do enumerate
def jinja2_enumerate(iterable):
    return zip(range(1, len(iterable) + 1), iterable)

app.jinja_env.globals.update(enumerate=jinja2_enumerate)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sobre')
def sobre():
    return render_template("sobre.html")

@app.route('/contato')
def contato():
    return render_template("contato.html")

@app.route('/quiz')
def quiz():
    return render_template("quiz.html")

@app.route('/perguntas', methods=['GET', 'POST'])
def perguntas():
    if request.method == 'POST':
        # Lógica para verificar respostas aqui
        pontuacao = 0
        for i, pergunta in enumerate(questions):
            resposta_usuario = request.form.get(f'q{i+1}')
            if resposta_usuario == pergunta['resposta_correta']:
                pontuacao += 1

        return render_template('resultado.html', pontuacao=pontuacao)
    return render_template("perguntas.html", questions=questions)





if __name__ == '__main__':
    app.run(debug=True)