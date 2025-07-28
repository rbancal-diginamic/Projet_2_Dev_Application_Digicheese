from typing import Optional, List
from sqlmodel import Session, select

from ..models.db_models.roleutilisateur_db import RoleUtilisateurDB
from ..repositories.abstract_repository import AbstractRepository


class SQLAlchemyRoleUtilisateurRepository(AbstractRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, roleutilisateur: dict) -> RoleUtilisateurDB:
        roleutilisateur_db = RoleUtilisateurDB(**roleutilisateur)
        self.session.add(roleutilisateur_db)
        self.session.commit()
        return roleutilisateur_db

    def get_all(self) -> List[RoleUtilisateurDB]:
        statement = select(RoleUtilisateurDB)
        roleutilisateur_db = self.session.exec(statement).all()
        return [RoleUtilisateurDB.model_validate(r) for r in roleutilisateur_db]

    def get_by_id(self, roleutilisateur_id: RoleUtilisateurDB.r_id) -> Optional[RoleUtilisateurDB]:
        statement = select(RoleUtilisateurDB)
        statement.where(RoleUtilisateurDB.r_id == roleutilisateur_id)
        
        roleutilisateur_db = self.session.exec(statement).first()
        if roleutilisateur_db:
            return roleutilisateur_db
        return None

    # def get_by_name(self, utilisateur_nom: RoleUtilisateurDB.r_nom) -> Optional[RoleUtilisateurDB]:
    #     statement = select(RoleUtilisateurDB)
    #     statement.where(RoleUtilisateurDB.r_nom == utilisateur_nom)

    #     roleutilisateur_db = self.session.exec(statement).first()
    #     if roleutilisateur_db:
    #         return roleutilisateur_db
    #     return None

    # def get_by_username(self, utilisateur_username: RoleUtilisateurDB.r_username) -> Optional[RoleUtilisateurDB]:
    #     statement = select(RoleUtilisateurDB)
    #     statement.where(RoleUtilisateurDB.r_username == utilisateur_username)

    #     roleutilisateur_db = self.session.exec(statement).first()
    #     if roleutilisateur_db:
    #         return roleutilisateur_db
    #     return None

    def update(self, roleutilisateur_id: int, roleutilisateur_body: dict) -> RoleUtilisateurDB | None:
        statement = select(RoleUtilisateurDB)
        statement.where(RoleUtilisateurDB.r_id == roleutilisateur_id)

        roleutilisateur_db = self.session.exec(statement).first()
        if roleutilisateur_db:
            for key, value in roleutilisateur_body.items():
                setattr(roleutilisateur_db, key, value)
            self.session.commit()
            self.session.refresh(roleutilisateur_db)
            return roleutilisateur_db
        return None

    def delete(self, roleutilisateur_id: RoleUtilisateurDB.r_id) -> bool:
        statement = select(RoleUtilisateurDB)
        statement.where(RoleUtilisateurDB.r_id == roleutilisateur_id)

        roleutilisateur_db = self.session.exec(statement).first()
        if roleutilisateur_db:
            self.session.delete(roleutilisateur_db)
            self.session.commit()
            return True
        return False