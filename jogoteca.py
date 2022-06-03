from flask import Flask, render_template, request

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

@app.route('/inicio')
def ola(): #função que define o que existe na route
    return render_template('lista.html', titulo='Jogos', jogos=lista_jogos)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar')
def criar():
    #pega dados do form
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    
    #cria objeto do tipo Jogo
    jogo = Jogo(nome, categoria, console)
    
    #add dados à lista
    lista_jogos.append(jogo)
    
    #mostrando dados da lista_jogos
    return render_template('lista.html', titulo='Jogos', jogos=lista_jogos)

app.run() # pode ser congigurado para outro host e porta: app.run(host='0.0.0.0', port=8080)