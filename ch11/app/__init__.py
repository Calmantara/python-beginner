# app/__init__.py

from flask_restx import Api
from flask import Blueprint

from .main.controller.user import api as user_ns

blueprint = Blueprint("api", __name__)

api = Api(
    blueprint,
    title="Flask Beginner Tutorial",
    version="1.0",
    description="a flask beginner tutorial",
)

api.add_namespace(user_ns, path="/user")
