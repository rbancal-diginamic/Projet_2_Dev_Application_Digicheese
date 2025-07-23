from typing import Optional, List
from sqlalchemy.orm import Session
from repositories.client_repository import ClientRepository
from models.schemas.client import Client
from models.db_models.client_db import ClientDB


class SQLAlchemyClientRepository(ClientRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, client: Client) -> None:
        client_db = ClientDB(**client.dict())
        self.session.add(client_db)
        self.session.commit()

    def return_client_by_parameter(self, client_db: ClientDB, parameter: int | str | bool) -> Client | None:
        client_db = self.session.query(client_db).get(parameter)
        if client_db:
            return Client(
                id=client_db.c_id,
                genre=client_db.genre,
                nom=client_db.c_nom,
                prenom=client_db.c_prenom,
                adresse_1=client_db.c_adresse_1,
                adresse_2=client_db.c_adresse_2,
                adresse_3=client_db.c_adresse_3,
                ville_id=client_db.c_ville_id,
                telephone=client_db.c_telephone,
                email=client_db.c_email,
                portable=client_db.c_portable,
                newsletter=client_db.c_newsletter
            )
        return None

    def get_by_id(self, client_id: Client.id) -> Optional[Client] | None:
        return self.return_client_by_parameter(ClientDB, client_id)

    def get_by_name(self, client_nom: Client.nom) -> Optional[Client] | None:
        return self.return_client_by_parameter(ClientDB, client_nom)

    def get_all(self) -> List[Client]:
        clients_db = self.session.query(ClientDB).all()
        return [Client.from_orm(c) for c in clients_db]

    def update(self, client: Client) -> None:
        client_db = self.session.query(ClientDB).get(client.id)
        if client_db:
            client_db.c_id = client_db.c_id,
            client_db.c_genre = client_db.genre,
            client_db.c_nom = client_db.c_nom,
            client_db.c_prenom = client_db.c_prenom,
            client_db.c_adresse_1 = client_db.c_adresse_1,
            client_db.c_adresse_2 = client_db.c_adresse_2,
            client_db.c_adresse_3 = client_db.c_adresse_3,
            client_db.c_ville_id = client_db.c_ville_id,
            client_db.c_telephone = client_db.c_telephone,
            client_db.c_email = client_db.c_email,
            client_db.c_portable = client_db.c_portable,
            client_db.c_newsletter = client_db.c_newsletter
            self.session.commit()

    def delete(self, client_id: Client.id) -> None:
        client_db = self.session.query(ClientDB).get(client_id)
        if client_db:
            self.session.delete(client_db)
            self.session.commit()