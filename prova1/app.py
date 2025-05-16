from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    return render_template('cadastro.html')

@app.route('/cookieset', methods=['POST', 'GET'])
def setacookie():
    if request.method == 'GET':
        return '<h1>Nada para ver aqui vá para <a href="/cadastro">cadastro'
    nome = request.form['nome']
    curso = request.form['curso']
    response = make_response(redirect(url_for('perfil', params = [nome, curso])))

    response.set_cookie('nome', nome, max_age=60*2) #2 minutos 
    return response


@app.route('/perfil', methods=['POST', 'GET'])
def perfil():
    params = request.args.to_dict(flat=False)
    nome = params['params'][0]
    curso = params['params'][1]
    if 'nome' in request.cookies:
        usr = request.cookies.get('nome')
    else:
        usr = 'Visitante'
    return render_template('perfil.html', nome=nome, curso=curso, usr=usr)

    