from app import db


class Sportif(db.Model):
    __tablename__ = "sportifs"

    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    prenom = db.Column(db.String(100), nullable=False)
    date_naissance = db.Column(db.Date, nullable=False)
    poids_kg = db.Column(db.Float, nullable=False)
    taille_cm = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "prenom": self.prenom,
            "date_naissance": self.date_naissance.isoformat(),
            "poids_kg": self.poids_kg,
            "taille_cm": self.taille_cm
        }
    

class TypeExercice(db.Model):
    __tablename__ = "types_exercices"

    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    categorie = db.Column(db.String(50), nullable=False)
    unite_mesure = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "categorie": self.categorie,
            "unite_mesure": self.unite_mesure
        }
    
class Seance(db.Model):
    __tablename__ = "seances"

    id = db.Column(db.Integer, primary_key=True)
    sportif_id = db.Column(db.Integer, db.ForeignKey("sportifs.id"), nullable=False)
    date = db.Column(db.Date, nullable=False)
    duree_minutes = db.Column(db.Integer, nullable=False)
    note_ressenti = db.Column(db.Integer, nullable=False)
    commentaire = db.Column(db.Text, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "sportif_id": self.sportif_id,
            "date": self.date.isoformat(),
            "duree_minutes": self.duree_minutes,
            "note_ressenti": self.note_ressenti,
            "commentaire": self.commentaire
        }
    
class ExerciceSeance(db.Model):
    __tablename__ = "exercices_seances"

    id = db.Column(db.Integer, primary_key=True)

    seance_id = db.Column(
        db.Integer,
        db.ForeignKey("seances.id"),
        nullable=False
    )

    type_exercice_id = db.Column(
        db.Integer,
        db.ForeignKey("types_exercices.id"),
        nullable=False
    )

    repetitions = db.Column(db.Integer, nullable=True)
    series = db.Column(db.Integer, nullable=True)
    duree_secondes = db.Column(db.Integer, nullable=True)
    distance_km = db.Column(db.Float, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "seance_id": self.seance_id,
            "type_exercice_id": self.type_exercice_id,
            "repetitions": self.repetitions,
            "series": self.series,
            "duree_secondes": self.duree_secondes,
            "distance_km": self.distance_km
        }
    
class Objectif(db.Model):
    __tablename__ = "objectifs"

    id = db.Column(db.Integer, primary_key=True)

    sportif_id = db.Column(
        db.Integer,
        db.ForeignKey("sportifs.id"),
        nullable=False
    )

    type_exercice_id = db.Column(
        db.Integer,
        db.ForeignKey("types_exercices.id"),
        nullable=False
    )

    valeur_cible = db.Column(db.Float, nullable=False)
    unite = db.Column(db.String(50), nullable=False)
    date_limite = db.Column(db.Date, nullable=False)
    atteint = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "sportif_id": self.sportif_id,
            "type_exercice_id": self.type_exercice_id,
            "valeur_cible": self.valeur_cible,
            "unite": self.unite,
            "date_limite": self.date_limite.isoformat(),
            "atteint": self.atteint
        }