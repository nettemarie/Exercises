from flask import Flask

app = Flask(__name__)


@app.route('/welcome')
def say_welcome():
    """Says welcome"""
    return "Welcome!"


@app.route('/welcome/home')
def say_welcome_home():
    """Says welcome home"""
    return "Welcome Home!"


@app.route('/welcome/back')
def say_welcome_back():
    """Says welcome back"""
    return "Welcome Back!"
