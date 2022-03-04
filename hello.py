from flask import Flask

app = Flask(__name__)


def index():
    return '<h1>Hello World!<h1>'


app.add_url_rule(rule='/', endpoint='index', view_func=index)
