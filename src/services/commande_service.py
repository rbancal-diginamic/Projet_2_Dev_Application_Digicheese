from datetime import datetime
from sqlmodel import Session

from src.models.schemas.commandes.commande_patch import CommandePatch
from ..models.db_models.commande_db import CommandeDB
from ..models.schemas.commandes.commande_post import CommandePost
from ..repositories.sql_alchemy_commande_repository import SQLAlchemyCommandeRepository


class CommandeService:
    def __init__(self, session: Session):
        self.repository = SQLAlchemyCommandeRepository(session)

    def __traitement(self, commande: dict) -> dict:
        commande['c_date_commande'] = datetime.fromisoformat(str(commande['c_date_commande']))
        return commande

    def create_commande(self, commande: CommandePost) -> CommandeDB:
        commande_dict = commande.model_dump()
        commande_traitee = self.__traitement(commande_dict)
        return self.repository.add(commande_traitee)

    def get_commande_by_id(self, c_id: int | None = None) -> CommandeDB | None:
        return self.repository.get_by_id(c_id)

    def get_commandes(self) -> list[CommandeDB]:
        return self.repository.get_all()

    def update_commande(self, commande_id: int, commande_body: CommandePatch) -> CommandeDB | None:
        commande_dict = commande_body.model_dump(exclude_unset=True)
        if 'c_date_commande' in commande_dict and commande_dict['c_date_commande']:
            commande_dict['c_date_commande'] = datetime.fromisoformat(str(commande_dict['c_date_commande']))
        return self.repository.update(commande_id, commande_dict)

    def delete_commande(self, c_id: int | None = None) -> bool:
        return self.repository.delete(c_id)
