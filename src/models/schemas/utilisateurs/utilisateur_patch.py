from sqlmodel import Field
from ...bases.utilisateur import UtilisateurBase


class UtilisateurPatch(UtilisateurBase):
    u_username: str | None = Field(default=None, max_length=50, nullable=True)