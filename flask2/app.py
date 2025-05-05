from flask import Flask, render_template, make_response, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("inicial.html")

@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    return render_template("cadastro.html")

@app.route('/cookie', methods=['POST'])
def cookie():
    response = make_response(redirect(url_for("preferencias")))
    nome = request.form['nome']
    opc = request.form['genr']
    email = 'email' in request.form

    semana = 7 * 24 * 60 * 60

    response.set_cookie("nome", nome, max_age=semana)
    response.set_cookie("genero", opc, max_age=semana)
    response.set_cookie("email", str(email), max_age=semana)
    return response

@app.route('/preferencias')
def preferencias():
    if not all(key in request.cookies for key in ['nome', "genero", "email"]):
        return '<a href="cadastro">Cadastrar</a>' 
    email = request.cookies.get("email")
    if request.cookies.get("genero") == 'comed':
        genero = "Comédia"
    elif request.cookies.get("genero") == 'acao':
        genero = "Ação"
    elif request.cookies.get("genero") == 'terror':
        genero = "Terror"
    elif request.cookies.get("genero") == 'ficcao':
        genero = "Ficção"
    else:
        genero = "Drama"
    
    if email == 'True':
        email = "Sim"
    else:
        email = "Não"
    nome = request.cookies.get("nome")
    return render_template('preferencias.html', gen=genero, email=email, nome=nome)

@app.route('/recomendacoes')
def recomendacoes():
    filmes = {
    "Ação": ["John Wick", "Mad Max: Estrada da Fúria", "Missão: Impossível – Efeito Fallout"],
    "Comédia": ["Superbad", "O Âncora: A Lenda de Ron Burgundy", "As Branquelas"],
    "Terror": ["Invocação do Mal", "Corra!", "O Exorcista"],
    "Drama": ["Forrest Gump", "Clube da Luta", "Os Infiltrados"],
    "Ficção": ["Interestelar", "Matrix", "Blade Runner 2049"]
    }
    gen = request.args.get('gen', '')
    rec1 = filmes[gen][0]
    rec2 = filmes[gen][1]
    rec3 = filmes[gen][2]
    return render_template("recomendacoes.html", gen=gen, rec1=rec1, rec2=rec2, rec3=rec3)
