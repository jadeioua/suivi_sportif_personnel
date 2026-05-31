from flask import Blueprint, request
from app.models import Sportif
from app import db
from flask import Blueprint

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return {
        "message": "API Suivi Sportif Personnel "
    }

@main.route("/sportifs", methods=["GET"])
def get_sportifs():
    sportifs = Sportif.query.all()

    return [sportif.to_dict() for sportif in sportifs]

