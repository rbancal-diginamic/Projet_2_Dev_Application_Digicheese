from sqlmodel import Field
from ...bases.commande import CommandeBase


class CommandePatch(CommandeBase):
    c_nombre_colis: int | None = Field(default=None, nullable=True)
    c_barchive: int | None = Field(default=None, nullable=True)
    c_bstock: int | None = Field(default=None, nullable=True)

    # FIXME : Décommenter après avoir créer les autres tables !
    # c_fk_client_id : int | None = Field(default=None, foreign_key="d_client.id", nullable=True)
    # c_fk_conditionnement : int | None = Field(default=None, foreign_key="d_conditionnement.id", nullable=True)
