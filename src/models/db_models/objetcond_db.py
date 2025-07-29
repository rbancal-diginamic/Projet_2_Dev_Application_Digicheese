from sqlmodel import Field, SQLModel


class ObjetCondDB(SQLModel, table=True):
    """Schéma de la table ObjetCond représentée en base de données"""
    
    __tablename__ = "d_rel_cond"
    
    o_id: int | None = Field(default=None, primary_key=True, index=True)
    # FIXME : Décommenter après avoir créer les autres tables !
    #codobj: int | None = Field(default=None, foreign_key="t_objet.codobj", nullable=True)
    #codcond: int | None = Field(default=None, foreign_key="t_conditionnement.idcondit", nullable=True)
    
    #objets: Objet | None = Relationship(back_populates="condit")
    #condit: Conditionnement | None = Relationship(back_populates="objets")
