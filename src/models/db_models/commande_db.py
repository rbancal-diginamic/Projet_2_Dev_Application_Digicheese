from sqlmodel import Field
from ..bases.commande import CommandeBase


class CommandeDB(CommandeBase, table=True):
    __tablename__ = "d_commande"
    c_id: int | None = Field(default=None, primary_key=True)
    # FIXME : Décommenter après avoir créer les autres tables !
    # c_fk_ville_id: int | None = Field(default=None, foreign_key="d_communes.id", nullable=True)
    # c_fk_client_id : int | None = Field(default=None, foreign_key="d_client.id", nullable=True)
    # c_fk_conditionnement : int | None = Field(default=None, foreign_key="d_conditionnement.id", nullable=True) 




        


