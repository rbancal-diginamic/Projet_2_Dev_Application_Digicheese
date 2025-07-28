from sqlmodel import Field
from ..bases.utilisateur import UtilisateurBase


class UtilisateurDB(UtilisateurBase, table=True):
    __tablename__ = "d_utilisateur"
    u_id: int | None = Field(default=None, primary_key=True)