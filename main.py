import os
from flask import Flask
from flask_cors import CORS
from services import Mysql
from services import CustomJSONEncoder
from api import setup_blueprint as pizza_blueprint


app = Flask(__name__)

app.json_encoder = CustomJSONEncoder
CORS(app)


def _register_blueprints(app):
    print("Registering blueprints")
    app.register_blueprint(pizza_blueprint())

def _start_services():
    print("Starting services")
    Mysql()
    print("Services started")


def start_app(app):
    _start_services()
    _register_blueprints(app)


def run_server():
    port = int(os.environ.get("PORT", 5000))

    _register_blueprints(app)

    app.run(host='0.0.0.0', port=port)

run_server()