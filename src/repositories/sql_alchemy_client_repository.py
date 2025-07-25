from typing import List
from sqlmodel import Session, select

from ..models.db_models.client_db import ClientDB
from ..repositories.abstract_repository import AbstractRepository


class SQLAlchemyClientRepository(AbstractRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, client: dict) -> ClientDB:
        client_db = ClientDB(**client)
        self.session.add(client_db)
        self.session.commit()
        self.session.refresh(client_db)
        return client_db

    def get_by_id(self, client_id: ClientDB.c_id) -> ClientDB | None:
        statement = select(ClientDB)
        statement.where(ClientDB.c_id == client_id)

        client_db = self.session.exec(statement).first()
        if client_db:
            return client_db
        return None

    def get_by_name(self, client_nom: ClientDB.c_nom) -> ClientDB | None:
        statement = select(ClientDB)
        statement.where(ClientDB.c_nom == client_nom)

        client_db = self.session.exec(statement).first()
        if client_db:
            return client_db
        return None

    def get_all(self) -> List[ClientDB]:
        statement = select(ClientDB)
        clients_db = self.session.exec(statement).all()
        return [ClientDB.model_validate(client) for client in clients_db]

    def update(self, client_id: int, client_body: dict) -> ClientDB | None:
        statement = select(ClientDB)
        statement.where(ClientDB.c_id == client_id)

        client_db = self.session.exec(statement).first()
        if client_db:
            for key, value in client_body.items():
                setattr(client_db, key, value)
            self.session.commit()
            self.session.refresh(client_db)
            return client_db
        return None

    def delete(self, client_id: ClientDB.c_id) -> bool:
        statement = select(ClientDB)
        statement.where(ClientDB.c_id == client_id)

        client_db = self.session.exec(statement).first()
        if client_db:
            self.session.delete(client_db)
            self.session.commit()
            return True
        return False
