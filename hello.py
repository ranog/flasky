from flask import Flask, redirect, abort

app = Flask(__name__)


@app.route('/')
def index():
    return redirect('http://www.example.com')


@app.route('/user/<name>')
def user(name):
    return f'<h1>Hello, {name.title()}!</h1>'


@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return f'<h1>Hello, {user.name}</h1>'
