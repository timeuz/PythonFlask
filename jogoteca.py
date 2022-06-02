from flask import Flask, render_template

app = Flask(__name__)

@app.route('/inicio')
def ola(): #função que define o que existe na route
    return render_template('lista.html')

app.run() # pode ser congigurado para outro host e porta: app.run(host='0.0.0.0', port=8080)