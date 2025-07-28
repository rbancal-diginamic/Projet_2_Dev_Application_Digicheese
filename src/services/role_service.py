from sqlmodel import Session

from ..models.db_models.role_db import RoleDB
from ..models.schemas.roles.role_post import RolePost
from ..models.schemas.roles.role_patch import RolePatch
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
    
    def create_role(self, role_body: RolePost) -> RoleDB:
        role = role_body.model_dump()
        return self.repository.add(role)
    
    def update_role(self, role_id: int, role_body: RolePatch) -> RoleDB | None:
        role = role_body.model_dump()
        return self.repository.update(role_id, role)
    
    def delete_role(self, r_id: int | None = None) -> bool:
        role = self.repository.get_by_id(r_id)
        if role:
            self.repository.delete(role)
            return True
        return False