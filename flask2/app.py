from flask import Flask, render_template, make_response, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("inicial.html")

@app.route('/form', methods=['POST', 'GET'])
def form():
    return render_template("cadastro.html")

@app.route('/cookie', methods=['POST'])
def cookie():
    response = make_response(redirect(url_for("ver_cookies")))
    nome = request.form['nome']
    opc = request.form['genr']
    email = 'email' in request.form

    semana = 7 * 24 * 60 * 60

    response.set_cookie("nome", nome, max_age=semana)
    response.set_cookie("genero", opc, max_age=semana)
    response.set_cookie("email", str(email), max_age=semana)
    return response

@app.route('/ver_cookies')
def ver_cookies():
    if not all(key in request.cookies for key in ['nome', "genero", "email"]):
        return redirect(url_for("form"))
    email = request.cookies.get("email")
    genero = request.cookies.get("genero")
    nome = request.cookies.get("nome")
    return render_template('preferencias.html', gen=genero, email=email, nome=nome)

@app.route('/recomendacoes')
def recomendacoes():
    gen = request.args.get('gen', '')

    if gen:
        resultado = f"recomendações para {gen}"
    else:
        return redirect(url_for('index'))
    return render_template("recomendacoes.html", gen=gen)
