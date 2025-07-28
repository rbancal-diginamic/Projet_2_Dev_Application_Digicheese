from sqlmodel import Field, Relationship
from typing import List
from src.models.bases.utilisateur import UtilisateurBase
from src.models.db_models.roleutilisateur_db import RoleUtilisateurDB
from ..bases.role import RoleBase

class RoleDB(RoleBase, table = True):
    __tablename__ = "d_role"
    r_id: int | None = Field(default=None, primary_key=True)

    r_utilisateurs: List["UtilisateurBase"] = Relationship(back_populates="u_role", link_model=RoleUtilisateurDB)