from flask import Flask

app = Flask(__name__)

@app.route('/inicio')
def ola(): #função que define o que existe na route
    return '<h1>Hello World</h1>'

app.run()