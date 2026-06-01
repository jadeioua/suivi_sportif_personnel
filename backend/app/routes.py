from flask import Blueprint, request
from app.models import (Sportif,TypeExercice,Seance,ExerciceSeance,Objectif)
from app import db
from flask import Blueprint
from datetime import datetime
from sqlalchemy import func


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

@main.route("/types-exercices", methods=["GET"])
def get_types_exercices():
    types_exercices = TypeExercice.query.all()

    return [type_exercice.to_dict() for type_exercice in types_exercices]

@main.route("/types-exercices", methods=["POST"])
def create_type_exercice():

    data = request.get_json()

    categories_valides = [
        "cardio",
        "musculation",
        "flexibilite"
    ]

    if data["categorie"] not in categories_valides:
        return {"error": "Catégorie invalide"}, 400

    type_exercice = TypeExercice(
        nom=data["nom"],
        categorie=data["categorie"],
        unite_mesure=data["unite_mesure"]
    )

    db.session.add(type_exercice)
    db.session.commit()

    return type_exercice.to_dict(), 201

@main.route("/seances", methods=["GET"])
def get_seances():
    sportif_id = request.args.get("sportif_id")

    query = Seance.query

    if sportif_id:
        query = query.filter_by(sportif_id=sportif_id)

    seances = query.all()

    return [seance.to_dict() for seance in seances]

@main.route("/seances", methods=["POST"])
def create_seance():

    data = request.get_json()

    if data["duree_minutes"] <= 0:
        return {"error": "La durée doit être strictement positive"}, 400

    if data["note_ressenti"] < 1 or data["note_ressenti"] > 5:
        return {"error": "La note doit être comprise entre 1 et 5"}, 400

    seance = Seance(
        sportif_id=data["sportif_id"],
        date=datetime.strptime(
            data["date"],
            "%Y-%m-%d"
        ).date(),
        duree_minutes=data["duree_minutes"],
        note_ressenti=data["note_ressenti"],
        commentaire=data.get("commentaire")
    )

    db.session.add(seance)
    db.session.commit()

    for exercice in data.get("exercices", []):

        exercice_seance = ExerciceSeance(
            seance_id=seance.id,
            type_exercice_id=exercice["type_exercice_id"],
            repetitions=exercice.get("repetitions"),
            series=exercice.get("series"),
            duree_secondes=exercice.get("duree_secondes"),
            distance_km=exercice.get("distance_km")
        )

        db.session.add(exercice_seance)

    db.session.commit()

    return seance.to_dict(), 201

@main.route("/seances/<int:id>", methods=["GET"])
def get_seance_detail(id):

    seance = Seance.query.get_or_404(id)

    exercices = ExerciceSeance.query.filter_by(seance_id=id).all()

    result = seance.to_dict()
    result["exercices"] = [
        exercice.to_dict() for exercice in exercices
    ]

    return result

@main.route("/seances/<int:id>", methods=["DELETE"])
def delete_seance(id):

    seance = Seance.query.get_or_404(id)

    ExerciceSeance.query.filter_by(seance_id=id).delete()

    db.session.delete(seance)
    db.session.commit()

    return {"message": "Séance supprimée"}

@main.route("/sportifs/<int:id>/stats", methods=["GET"])
def get_sportif_stats(id):

    sportif = Sportif.query.get_or_404(id)

    stats = db.session.query(
        func.count(Seance.id),
        func.sum(Seance.duree_minutes),
        func.avg(Seance.duree_minutes)
    ).filter(Seance.sportif_id == id).first()

    exercices_distincts = db.session.query(
        func.count(func.distinct(ExerciceSeance.type_exercice_id))
    ).join(Seance).filter(Seance.sportif_id == id).scalar()

    return {
        "sportif": sportif.to_dict(),
        "total_seances": stats[0] or 0,
        "duree_totale": stats[1] or 0,
        "duree_moyenne": float(stats[2]) if stats[2] else 0,
        "exercices_distincts": exercices_distincts or 0
    }

@main.route("/objectifs", methods=["POST"])
def create_objectif():

    data = request.get_json()

    objectif = Objectif(
        sportif_id=data["sportif_id"],
        type_exercice_id=data["type_exercice_id"],
        valeur_cible=data["valeur_cible"],
        unite=data["unite"],
        date_limite=datetime.strptime(data["date_limite"], "%Y-%m-%d").date(),
        atteint=False
    )

    db.session.add(objectif)
    db.session.commit()

    return objectif.to_dict(), 201


@main.route("/objectifs/<int:id>", methods=["PUT"])
def update_objectif(id):

    objectif = Objectif.query.get_or_404(id)

    objectif.atteint = True

    db.session.commit()

    return objectif.to_dict()