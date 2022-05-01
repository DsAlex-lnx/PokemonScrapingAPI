from flask import Flask 

from pykemon.blueprints import restapi

app = Flask(__name__)

restapi.init_app(app)