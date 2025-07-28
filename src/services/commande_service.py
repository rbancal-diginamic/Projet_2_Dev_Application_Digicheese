from sqlmodel import Session

from src.models.schemas.commandes.commande_patch import CommandePatch
from ..models.db_models.commande_db import CommandeDB
from ..models.schemas.commandes.commande_post import CommandePost
from ..repositories.sql_alchemy_commande_repository import SQLAlchemyCommandeRepository


class CommandeService:
    def __init__(self, session: Session):
        self.repository = SQLAlchemyCommandeRepository(session)

    def create_commande(self, commande: CommandePost) -> CommandeDB:
        commande = commande.model_dump()
        return self.repository.add(commande)

    def get_commande_by_id(self, c_id: int | None = None) -> CommandeDB |None:
        return self.repository.get_by_id(c_id)

    def get_commandes(self) -> list[CommandeDB]:
        return self.repository.get_all()

    def update_commande(self, commande_id: int, commande_body: CommandePatch) -> CommandeDB | None :
        commande = commande_body.model_dump()
        return self.repository.update(commande_id, commande)

    def delete_commande(self, c_id: int | None = None) -> bool:
        commande = self.repository.get_by_id(c_id)
        if commande:
            self.repository.delete(commande)
            return True
        return False