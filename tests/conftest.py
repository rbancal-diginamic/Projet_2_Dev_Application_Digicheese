##################
# Modules import #
##################

import pytest
from fastapi.testclient import TestClient
from sqlmodel import create_engine, Session, SQLModel

###############
# SRC imports #
###############

from src.main import app
from src.database import get_db
from src.models import ClientDB

############
# Fixtures #
############

@pytest.fixture(scope="session")
def test_db():
    """
    Crée une base de données SQLite en fichier pour vérifier.
    Initialise les tables, et insère un permet d'insérer des données par défaut.
    """
    db_url = "sqlite:///./test.db"
    engine = create_engine(db_url, echo=False)
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)
    
    with Session(engine) as session:
        john_doe = ClientDB(c_prenom="John", c_nom="Doe", c_adresse_1="123 Cheese St")
        session.add(john_doe)
        session.commit()

        # Retourne la session de test
        yield session

@pytest.fixture(scope="function")
def client(test_db):
    """Crée un client FastAPI qui utilise la session de test en override."""
    def override_get_db():
        yield test_db
        
    # Ecrase la connexion à l'ancienne base de données par la nouvelle
    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()