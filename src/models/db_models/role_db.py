from sqlmodel import Field, Relationship
from typing import List, TYPE_CHECKING

from ..bases.role import RoleBase

from .roleutilisateur_db import RoleUtilisateurDB

if TYPE_CHECKING:
    from ..db_models import UtilisateurDB


class RoleDB(RoleBase, table=True):
    __tablename__ = "d_role"
    r_id: int | None = Field(default=None, primary_key=True)

    r_utilisateurs: List["UtilisateurDB"] = Relationship(back_populates="u_roles", link_model=RoleUtilisateurDB)
