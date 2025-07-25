from sqlmodel import Session

from ..models.db_models.utilisateur_db import UtilisateurDB
from ..models.schemas.utilisateur.utilisateur_post import UtilisateurPost
from ..repositories.sql_alchemy_utilisateur_repository import SQLAlchemyUtilisateurRepository


class UtilisateurService:
    def __init__(self, session: Session):
        self.repository = SQLAlchemyUtilisateurRepository(session)

    def __traitement(self, utilisateur: dict) -> dict:
        utilisateur['u_nom'] = utilisateur["u_nom"].upper()
        utilisateur['u_prenom'] = utilisateur["u_prenom"].capitalize()
        return utilisateur

    def create_utilisateur(self, utilisateur: UtilisateurPost) -> UtilisateurDB:
        utilisateur = utilisateur.model_dump()
        utilisateur = self.__traitement(utilisateur)
        return self.repository.add(utilisateur)

    def get_utilisateur_by_id(self, u_id: int | None = None) -> UtilisateurDB:
        return self.repository.get_by_id(u_id)

    def get_utilisateur_by_name(self, name: str) -> UtilisateurDB:
        pass

    def get_utilisateur_by_username(self, username: str) -> UtilisateurDB:
        pass

    def get_utilisateurs(self, session: Session) -> list[UtilisateurDB]:
        return self.repository.get_all(session)

    def update_utilisateur(self, u_id: int | None = None) -> UtilisateurDB:
        pass

    def delete_utilisateur(self, u_id: int | None = None) -> bool:
        utilisateur = self.repository.get_by_id(u_id)
        if utilisateur:
            self.repository.delete(utilisateur)
            return True
        return False