import os
from sqlmodel import create_engine, Session, SQLModel
from dotenv import load_dotenv


load_dotenv()

# Configuration de la base de données
DB_CONFIG = {
    "connector": os.getenv("DB_CONNECTOR"),
    "username": os.getenv("DB_USERNAME"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "database": os.getenv("DB_NAME"),
}

# URL de connexion à la base de données
DATABASE_URL = f"{DB_CONFIG['connector']}://{DB_CONFIG['username']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"

# Moteur de base de données
engine = create_engine(DATABASE_URL, echo=False)

# déclaration d'une base qui permet après de créer un modèle et de mapper avec SqlModel
def get_db():
    """
    Fonction génératrice pour fournir une session de base de données.
    Laisse ouverte la session pour les opérations de base de données et la ferme après utilisation.
    """
    db = Session(engine, autoflush=False, autocommit=False)
    try:
        yield db
    finally:
        db.close()
        
# Il est possible de créer des fonctions utilitaires pour supprimer et recréer la base de données
# Attention à ne pas essayer de se connecter à la base de données pendant cette opération (DATABASE_URL)