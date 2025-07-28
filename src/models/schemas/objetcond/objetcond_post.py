from sqlmodel import Field
from ...bases.objetcond import ObjetCondBase

class ObjetCondPost(ObjetCondBase):

     # FIXME : Décommenter après avoir créer les autres tables !
    #codobj: int | None = Field(default=None, foreign_key="t_objet.codobj", nullable=True)
    #codcond: int | None = Field(default=None, foreign_key="t_conditionnement.idcondit", nullable=True)
    
    #objets: Objet | None = Relationship(back_populates="condit")
    #condit: Conditionnement | None = Relationship(back_populates="objets")
    pass