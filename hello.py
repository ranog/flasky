from flask import Flask, make_response

app = Flask(__name__)


@app.route('/')
def index():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response


@app.route('/user/<name>')
def user(name):
    return f'<h1>Hello, {name.title()}!</h1>'
