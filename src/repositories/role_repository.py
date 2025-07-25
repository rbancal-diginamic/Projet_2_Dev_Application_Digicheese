from typing import Optional, List
from sqlmodel import Session, select

from ..models.db_models.role_db import RoleDB
from ..repositories.abstract_repository import AbstractRepository


class SQLAlchemyRoleRepository(AbstractRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, role: dict) -> RoleDB:
        role_db = RoleDB(**role)
        self.session.add(role_db)
        self.session.commit()
        return role_db

    def get_by_id(self, role_id: RoleDB.r_codrole) -> Optional[RoleDB]:
        statement = select(RoleDB).where(RoleDB.r_codrole == role_id)
        role_db = self.session.exec(statement).first()
        if role_db:
            return role_db
        return None

    def get_by_name(self, role_nom: RoleDB.r_librole) -> Optional[RoleDB]:
        statement = select(RoleDB).where(RoleDB.r_librole == role_nom)
        role_db = self.session.exec(statement).first()
        if role_db:
            return role_db
        return None

    def get_all(self) -> List[RoleDB]:
        role_db = self.session.query(RoleDB).all()
        return [RoleDB.model_validate(r) for r in role_db]

    def update(self, role: dict) -> None:
        role_db = self.session.query(RoleDB).get(role_db.r_codrole)
        if role_db:
            # FIXME : Contrôler la bonne exécution de l'update !
            RoleDB(**role.model_dump())
            self.session.commit()

    def delete(self, role_id: RoleDB.r_codrole) -> None:
        role_db = self.session.query(RoleDB).get(role_id)
        if role_db:
            self.session.delete(role_db)
            self.session.commit()