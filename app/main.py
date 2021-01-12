import os
from flask import Flask

app = Flask(__name__)

APP_VERSION = '1.0.0'

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/version')
def version():
    return APP_VERSION
