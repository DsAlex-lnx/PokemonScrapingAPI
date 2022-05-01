from flask import abort, Response
import json
from flask_restful import Resource
from pykemon.blueprints.scraping import collector


class PokemonResource(Resource):
    def get(self):
        pokemons = collector.pokemons_infos() or abort(204)
        return Response( json.dumps({
            'pokemons' : pokemons
        }), mimetype='application/json')
            
class CatchingPokemonResource(Resource):
    def get(seld, pokedex_id):
        pokemon = collector.catching_by_id(pokedex_id) or abort(404)
        return Response(json.dumps({
            'pokemon' : pokemon
        }), mimetype='application/json')
