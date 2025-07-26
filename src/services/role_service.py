from sqlmodel import Session

from ..models.db_models.role_db import RoleDB
from ..models.schemas.role.role_post import RolePost
from ..repositories.sql_alchemy_role_repository import SQLAlchemyRoleRepository


class RoleService:
    def __init__(self, session: Session):
        self.repository = SQLAlchemyRoleRepository(session)

    def get_role_by_id(self, r_id: int | None = None) -> RoleDB:
        return self.repository.get_by_id(r_id)

    def get_role_by_name(self, r_nom: str) -> RoleDB:
        return self.repository.get_by_name(r_nom)

    def get_role(self, session: Session) -> list[RoleDB]:
        return self.repository.get_all(session)