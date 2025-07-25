from sqlmodel import Session

from ..models.db_models.commande_db import CommandeDB
from ..models.schemas.commandes.commande_post import CommandePost
from ..repositories.sql_alchemy_commande_repository import SQLAlchemyCommandeRepository


class CommandeService:
    def __init__(self, session: Session):
        self.repository = SQLAlchemyCommandeRepository(session)

    def __traitement(self, commande: dict) -> dict:
    #    commande['c_nom'] = commande["c_nom"].upper()
    #    commande['c_prenom'] = commande["c_prenom"].capitalize()
        return commande


    def create_commande(self, commande: CommandePost) -> CommandeDB:
        commande = commande.model_dump()
        commande = self.__traitement(commande)
        return self.repository.add(commande)

    def get_commande_by_id(self, c_id: int | None = None) -> CommandeDB:
        return self.repository.get_by_id(c_id)

    def get_commande_by_name(self, name: str) -> CommandeDB:
        pass

    def get_commandes(self) -> list[CommandeDB]:
        return self.repository.get_all()

    def update_commande(self, c_id: int | None = None) -> CommandeDB:
        pass

    def delete_commande(self, c_id: int | None = None) -> bool:
        commande = self.repository.get_by_id(c_id)
        if commande:
            self.repository.delete(commande)
            return True
        return False