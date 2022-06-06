from flask import Flask, render_template, request, redirect, session, flash

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('World of Warcraft', 'MMORPG', 'PC')
jogo2 = Jogo('Red Dead Redemption', 'RPG', 'XBOX')
jogo3 = Jogo('Age of Empires', 'Estrategia', 'PC')
lista_jogos = [jogo1, jogo2, jogo3]

app = Flask(__name__)
app.secret_key = 'kabong'

@app.route('/')
def index(): #função que define o que existe na route
    return render_template('lista.html', titulo='Jogos', jogos=lista_jogos)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=novo')
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST', ])
def criar():
    #pega dados do form
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    
    #cria objeto do tipo Jogo
    jogo = Jogo(nome, categoria, console)
    
    #add dados à lista
    lista_jogos.append(jogo)
    
    #redirecionando para pagina inicial com os dados já cadastrados
    return redirect('/')

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST', ])
def autenticar():
    proxima_pagina = request.form['proxima']
    if 'alohomora' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario'] #salvando nome do usuario na session
        flash('Usuario ' + session['usuario_logado'] + ' logado com sucesso!')
        return redirect('/{}'.format(proxima_pagina))
    else:
        flash('Usuario não logado')
        return redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect('/')

app.run(debug=True) # pode ser congigurado para outro host e porta: app.run(host='0.0.0.0', port=8080)