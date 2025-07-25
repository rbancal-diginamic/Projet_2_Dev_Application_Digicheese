from sqlmodel import Field
from ...bases.client import ClientBase


class ClientPost(ClientBase):
    
    # FIXME : Décommenter après avoir créer les autres tables !
    # c_fk_ville_id: int | None = Field(default=None, foreign_key="d_communes.id", nullable=True)
    pass