from flask import Blueprint

from application import db

bp = Blueprint("routes", __name__)


@bp.route("/")
def index():
    return "Hello"
