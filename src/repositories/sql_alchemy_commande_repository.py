from typing import Optional, List
from sqlmodel import Session, select

from ..models.db_models.commande_db import CommandeDB
from .abstract_repository import AbstractRepository


class SQLAlchemyCommandeRepository(AbstractRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, commande: dict) -> CommandeDB:
        commande_db = CommandeDB(**commande)
        self.session.add(commande_db)
        self.session.commit()
        return commande_db

    def get_by_id(self, commande_id: CommandeDB.c_id) -> Optional[CommandeDB]:
        statement = select(CommandeDB).where(CommandeDB.c_id == commande_id)
        commande_db = self.session.exec(statement).first()
        if commande_db:
            return commande_db
        return None

    def get_by_name(self, commande_nom: CommandeDB.c_nom) -> Optional[CommandeDB]:
        statement = select(CommandeDB).where(CommandeDB.c_nom == commande_nom)
        commande_db = self.session.exec(statement).first()
        if commande_db:
            return commande_db
        return None

    def get_all(self) -> List[CommandeDB]:
        commandes_db = self.session.query(CommandeDB).all()
        return [CommandeDB.model_validate(c) for c in commandes_db]

    def update(self, commande: dict) -> None:
        commande_db = self.session.query(CommandeDB).get(commande.id)
        if commande_db:
            # FIXME : Contrôler la bonne exécution de l'update !
            CommandeDB(**commande.model_dump())
            self.session.commit()

    def delete(self, commande_id: CommandeDB.c_id) -> None:
        commande_db = self.session.query(CommandeDB).get(commande_id)
        if commande_db:
            self.session.delete(commande_db)
            self.session.commit()