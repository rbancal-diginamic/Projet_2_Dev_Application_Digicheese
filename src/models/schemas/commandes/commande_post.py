from ...bases.commande import CommandeBase


class CommandePost(CommandeBase):
    
    # FIXME : Décommenter après avoir créer les autres tables !
    # c_fk_client_id : int | None = Field(default=None, foreign_key="d_client.id", nullable=True)
    # c_fk_conditionnement : int | None = Field(default=None, foreign_key="d_conditionnement.id", nullable=True) 
    pass