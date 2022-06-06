from flask import Flask, render_template, request, redirect, session, flash, url_for

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('World of Warcraft', 'MMORPG', 'PC')
jogo2 = Jogo('Red Dead Redemption', 'RPG', 'XBOX')
jogo3 = Jogo('Age of Empires', 'Estrategia', 'PC')
lista_jogos = [jogo1, jogo2, jogo3]

class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha

usuario1 = Usuario("Tester 1", "tester", "alohomora")
usuario2 = Usuario("Tester 2", "tester2", "123456")
usuario3 = Usuario("Tester 3", "tester3", "654321")

usuarios = {
    usuario1.nickname: usuario1,
    usuario2.nickname: usuario2,
    usuario3.nickname: usuario3
}
app = Flask(__name__)
app.secret_key = 'kabong'

@app.route('/')
def index(): #função que define o que existe na route
    return render_template('lista.html', titulo='Jogos', jogos=lista_jogos)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
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
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash('Usuario ' + usuario.nickname + ' logado com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)            
    else:
        flash('Usuario não logado')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))

app.run(debug=True) # pode ser congigurado para outro host e porta: app.run(host='0.0.0.0', port=8080)