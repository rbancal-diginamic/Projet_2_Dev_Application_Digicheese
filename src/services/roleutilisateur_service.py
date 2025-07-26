from sqlmodel import Session

from ..models.db_models.roleutilisateur_db import RoleUtilisateurDB
from ..models.schemas.RoleUtilisateur.roleutilisateur_post import RoleUtilisateurPost
from ..repositories.sql_alchemy_roleutilisateur_repository import SQLAlchemyRoleUtilisateurRepository

class RoleUtilisateurService:
    def __init__(self, session: Session):
        self.repository = SQLAlchemyRoleUtilisateurRepository(session)

    def __traitement(self, roleutilisateur: dict) -> dict:
        roleutilisateur['r_nom'] = roleutilisateur["r_nom"].capitalize()
        return roleutilisateur

    def create_roleutilisateur(self, roleutilisateur: RoleUtilisateurPost) -> RoleUtilisateurDB:
        roleutilisateur = roleutilisateur.model_dump()
        roleutilisateur = self.__traitement(roleutilisateur)
        return self.repository.add(roleutilisateur)
    
    def get_roleutilisateurs(self, session: Session) -> list[RoleUtilisateurDB]:
        return self.repository.get_all(session)

    def get_roleutilisateur_by_id(self, r_id: int | None = None) -> RoleUtilisateurDB:
        return self.repository.get_by_id(r_id)

    def get_roleutilisateur_by_name(self, name: str) -> RoleUtilisateurDB:
        return self.repository.get_by_name(name)

    def get_roleutilisateur_by_username(self, username: str) -> RoleUtilisateurDB:
        return self.repository.get_by_username(username)

    def update_roleutilisateur(self, r_id: int | None = None) -> RoleUtilisateurDB:
        roleutilisateur = self.repository.get_by_id(r_id)
        if roleutilisateur:
            self.repository.update(roleutilisateur)
            return True
        return False

    def delete_roleutilisateur(self, r_id: int | None = None) -> bool:
        roleutilisateur = self.repository.get_by_id(r_id)
        if roleutilisateur:
            self.repository.delete(roleutilisateur)
            return True
        return False