from sqlmodel import Field, Relationship
from typing import List
from src.models.bases import roleutilisateur, utilisateur
from ..bases.role import RoleBase

class RoleDB(RoleBase, table = True):
    __tablename__ = "d_role"
    r_id: int | None = Field(default=None, primary_key=True)

    r_utilisateurs: List["utilisateur"] = Relationship(backpopulates="u_role", link_model=roleutilisateur)