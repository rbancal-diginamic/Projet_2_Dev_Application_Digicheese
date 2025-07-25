from sqlmodel import Field
from ...bases.client import ClientBase


class ClientPatch(ClientBase):
    c_nom: str | None = Field(default=None, max_length=40, index=True, nullable=True)
    c_prenom: str | None = Field(default=None, max_length=30, nullable=True)
    c_fk_ville_id: int | None = Field(default=None, foreign_key="d_communes.id", nullable=True)
