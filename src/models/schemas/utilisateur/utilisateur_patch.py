from sqlmodel import Field
from ...bases.utilisateur import UtilisateurBase


class UtilisateurPatch(UtilisateurBase):
    u_nom: str | None = Field(default=None, max_length=50, index=True, nullable=True)
    u_prenom: str | None = Field(default=None, max_length=50, nullable=True)