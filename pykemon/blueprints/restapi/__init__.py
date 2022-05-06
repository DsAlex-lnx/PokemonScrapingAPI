from flask import Blueprint
from flask_restful import Api
from .resources import PokemonResource, CatchingPokemonResource


bp = Blueprint('restapi', __name__, url_prefix='/api/v1')
api = Api(bp)
api.add_resource(PokemonResource, '/pokemon/')
api.add_resource(CatchingPokemonResource, '/pokemon/<pokedex_id>')


def init_app(app):
    app.register_blueprint(bp)