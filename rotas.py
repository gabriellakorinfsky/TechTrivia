import json
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lê as perguntas do arquivo JSON
with open('data/perguntas.json', 'r', encoding='utf-8') as file:
    perguntas = json.load(file)
with open('data/maturidade.json', 'r', encoding='utf-8') as file:
    perguntas_mat = json.load(file)
with open('data/python.json', 'r', encoding='utf-8') as file:
    perguntas_pyt = json.load(file)
    
num_perguntas = len(perguntas)
respostas_corretas = 0
respostas_marcadas = {}

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

@app.route('/perguntas/<int:num_pergunta>', methods=['GET', 'POST'])
def exibir_pergunta(num_pergunta):
    global respostas_marcadas, respostas_corretas
    
    if num_pergunta > num_perguntas or num_pergunta <= 0:
        return redirect(url_for('index'))

    pergunta_atual = perguntas[num_pergunta - 1]
    resposta_correta = pergunta_atual['resposta_correta']    
    
    mensagem_resposta = None
    
    if request.method == 'POST':
        # Aqui você pode processar a resposta submetida
        resposta_selecionada = request.form['resposta']
        respostas_marcadas[num_pergunta] = resposta_selecionada
      
        proxima_pergunta = num_pergunta + 1
        if proxima_pergunta > num_perguntas:
            return redirect(url_for('resultado'))
        else:
            return redirect(url_for('exibir_pergunta', num_pergunta=proxima_pergunta))

    return render_template('perguntas.html', pergunta=pergunta_atual, num_pergunta=num_pergunta, num_perguntas=num_perguntas)

@app.route('/perg_python/<int:num_pergunta>', methods=['GET', 'POST'])
def exibir_pergpython(num_pergunta):
    if num_pergunta > num_perguntas or num_pergunta <= 0:
        return redirect(url_for('index'))

    pergunta_atual = perguntas_pyt[num_pergunta - 1]
    if request.method == 'POST':
        resposta_selecionada = request.form['resposta']
        resposta_correta = pergunta_atual['resposta_correta']

        proxima_pergunta = num_pergunta + 1
        if proxima_pergunta > num_perguntas:
            return redirect(url_for('resultado'))
        else:
            return redirect(url_for('exibir_pergpython', num_pergunta=proxima_pergunta))

    return render_template('perg_python.html', pergunta=pergunta_atual, num_pergunta=num_pergunta, num_perguntas=num_perguntas)

@app.route('/perg_maturidade/<int:num_pergunta>', methods=['GET', 'POST'])
def exibir_pergmat(num_pergunta):
    if num_pergunta > num_perguntas or num_pergunta <= 0:
        return redirect(url_for('index'))

    pergunta_atual = perguntas_mat[num_pergunta - 1]
    if request.method == 'POST':
        resposta_selecionada = request.form['resposta']

        resposta_correta = pergunta_atual['resposta_correta']

        proxima_pergunta = num_pergunta + 1
        if proxima_pergunta > num_perguntas:
            return redirect(url_for('resultado'))
        else:
            return redirect(url_for('exibir_pergmat', num_pergunta=proxima_pergunta))

    return render_template('perg_maturidade.html', pergunta=pergunta_atual, num_pergunta=num_pergunta, num_perguntas=num_perguntas)


if __name__ == '__main__':
    app.run(debug=True)