from flask import Flask
from app.view import *

def create_app():
    app = Flask(__name__)
    app.add_url_rule('/', '/', hello_world, methods=['GET'])
    app.add_url_rule('/login', 'login', login, methods=['GET', 'POST'])
    return app