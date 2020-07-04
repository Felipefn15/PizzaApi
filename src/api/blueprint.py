from flask import Blueprint
from flask_restful import Api

from .cart import Cart
from .itens import Itens
from .login import Login


def setup_blueprint():
    blueprint = Blueprint(
        "pizza", __name__,
    )

    api = Api(blueprint)
    api.add_resource(Login, "/login")
    api.add_resource(Cart, "/cart")
    api.add_resource(Itens, "/itens")
    return blueprint
