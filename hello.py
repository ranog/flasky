from flask import Flask, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return redirect('http://www.example.com')


@app.route('/user/<name>')
def user(name):
    return f'<h1>Hello, {name.title()}!</h1>'
