from typing import Optional, List
from sqlmodel import Session, select

from ..models.db_models.utilisateur_db import UtilisateurDB
from ..repositories.abstract_repository import AbstractRepository


class SQLAlchemyUtilisateurRepository(AbstractRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, utilisateur: dict) -> UtilisateurDB:
        utilisateur_db = UtilisateurDB(**utilisateur)
        self.session.add(utilisateur_db)
        self.session.commit()
        return utilisateur_db

    def get_all(self) -> List[UtilisateurDB]:
        statement = select(UtilisateurDB)
        utilisateur_db = self.session.exec(statement).all()
        return [UtilisateurDB.model_validate(u) for u in utilisateur_db]

    def get_by_id(self, utilisateur_id: UtilisateurDB.u_id) -> Optional[UtilisateurDB]:
        statement = select(UtilisateurDB).where(UtilisateurDB.u_id == utilisateur_id)
        
        utilisateur_db = self.session.exec(statement).first()
        if utilisateur_db:
            return utilisateur_db
        return None

    def get_by_name(self, utilisateur_nom: UtilisateurDB.u_nom) -> Optional[UtilisateurDB]:
        statement = select(UtilisateurDB).where(UtilisateurDB.u_nom == utilisateur_nom)

        utilisateur_db = self.session.exec(statement).first()
        if utilisateur_db:
            return utilisateur_db
        return None

    def get_by_username(self, utilisateur_username: UtilisateurDB.u_username) -> Optional[UtilisateurDB]:
        statement = select(UtilisateurDB).where(UtilisateurDB.u_username == utilisateur_username)

        utilisateur_db = self.session.exec(statement).first()
        if utilisateur_db:
            return utilisateur_db
        return None

    def update(self, utilisateur_id: int, utilisateur_body: dict) -> UtilisateurDB | None:
        statement = select(UtilisateurDB).where(UtilisateurDB.u_id == utilisateur_id)

        utilisateur_db = self.session.exec(statement).first()
        if utilisateur_db:
            for key, value in utilisateur_body.items():
                setattr(utilisateur_db, key, value)
            self.session.commit()
            self.session.refresh(utilisateur_db)
            return utilisateur_db
        return None

    def delete(self, utilisateur_id: UtilisateurDB.u_id) -> bool:
        statement = select(UtilisateurDB).where(UtilisateurDB.u_id == utilisateur_id)

        utilisateur_db = self.session.exec(statement).first()
        if utilisateur_db:
            self.session.delete(utilisateur_db)
            self.session.commit()
            return True
        return False