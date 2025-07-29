from sqlmodel import Session

from src.models.schemas.utilisateurs.utilisateur_patch import UtilisateurPatch

from ..models.db_models.utilisateur_db import UtilisateurDB
from ..models.schemas.utilisateurs.utilisateur_post import UtilisateurPost
from ..repositories.sql_alchemy_utilisateur_repository import SQLAlchemyUtilisateurRepository


class UtilisateurService:
    """Service to do treatments on Utilisateur entities before commit in database."""
    def __init__(self, session: Session):
        self.repository = SQLAlchemyUtilisateurRepository(session)

    def __traitement(self, utilisateur: UtilisateurPost | UtilisateurPatch) -> dict:
        utilisateur_traitement = utilisateur.model_dump()
        utilisateur_traitement['u_nom'] = utilisateur_traitement["u_nom"].upper()
        utilisateur_traitement['u_prenom'] = utilisateur_traitement["u_prenom"].capitalize()
        utilisateur_traitement['u_username'] = utilisateur_traitement["u_username"].lower()
        return utilisateur_traitement

    def create_utilisateur(self, utilisateur_body: UtilisateurPost) -> UtilisateurDB:
        utilisateur = self.__traitement(utilisateur_body)
        return self.repository.add(utilisateur)
    
    def get_utilisateurs(self) -> list[UtilisateurDB]:
        return self.repository.get_all()

    def get_utilisateur_by_id(self, u_id: int | None = None) -> UtilisateurDB | None:
        return self.repository.get_by_id(u_id)

    def get_utilisateur_by_name(self, name: str) -> UtilisateurDB | None:
        return self.repository.get_by_name(name)

    def get_utilisateur_by_username(self, username: str) -> UtilisateurDB | None:
        return self.repository.get_by_username(username)

    def update_utilisateur(self, u_id: int, utilisateur_body: UtilisateurPatch) -> UtilisateurDB | None:
        utilisateur = utilisateur_body.model_dump(exclude_unset=True)
        return self.repository.update(u_id, utilisateur)

    def delete_utilisateur(self, u_id: int | None = None) -> bool:
        return self.repository.delete(u_id)