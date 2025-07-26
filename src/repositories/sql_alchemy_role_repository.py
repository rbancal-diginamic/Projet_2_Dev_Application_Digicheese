from typing import Optional, List
from sqlmodel import Session, select

from ..models.db_models.role_db import RoleDB
from ..repositories.abstract_repository import AbstractRepository


class SQLAlchemyRoleRepository(AbstractRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, role_id: RoleDB.r_id) -> Optional[RoleDB]:
        statement = select(RoleDB)
        statement.where(RoleDB.r_id == role_id)
        
        role_db = self.session.exec(statement).first()
        if role_db:
            return [RoleDB.model_validate(r) for r in role_db]
        return None

    def get_by_name(self, role_nom: RoleDB.r_nom) -> Optional[RoleDB]:
        statement = select(RoleDB)
        statement.where(RoleDB.r_nom == role_nom)

        role_db = self.session.exec(statement).first()
        if role_db:
            return [RoleDB.model_validate(r) for r in role_db]
        return None

    def get_all(self) -> List[RoleDB]:
        statement = select(RoleDB)
        role_db = self.session.exec(statement).all()
        return [RoleDB.model_validate(r) for r in role_db]