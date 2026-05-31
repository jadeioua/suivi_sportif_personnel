from flask import Blueprint, request
from app.models import Sportif
from app import db
from flask import Blueprint
from datetime import datetime


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

@main.route("/sportifs", methods=["POST"])
def create_sportif():

    data = request.get_json()

    sportif = Sportif(
        nom=data["nom"],
        prenom=data["prenom"],
        date_naissance=datetime.strptime(data["date_naissance"], "%Y-%m-%d").date(),
        poids_kg=data["poids_kg"],
        taille_cm=data["taille_cm"]
    )

    db.session.add(sportif)
    db.session.commit()

    return sportif.to_dict(), 201