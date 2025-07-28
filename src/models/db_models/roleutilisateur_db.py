from sqlmodel import Field
from ..bases.roleutilisateur import RoleUtilisateurBase


class RoleUtilisateurDB(RoleUtilisateurBase, table=True):
    __tablename__ = "d_utilisateur_role"
    r_id: int | None = Field(default=None, primary_key=True)