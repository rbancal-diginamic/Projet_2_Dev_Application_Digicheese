from sqlmodel import Field
from ..bases.client import ClientBase


class ClientDB(ClientBase, table=True):
    __tablename__ = "d_client"
    c_id: int | None = Field(default=None, primary_key=True)
    # FIXME : Décommenter après avoir créer les autres tables !
    # c_fk_ville_id: int | None = Field(default=None, foreign_key="d_communes.id", nullable=True)