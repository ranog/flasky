from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Bad Request</h1>', 400


@app.route('/user/<name>')
def user(name):
    return f'<h1>Hello, {name.title()}!</h1>'
