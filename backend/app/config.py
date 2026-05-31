import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:postgres@localhost:5433/suivi_sportif_personnel"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False