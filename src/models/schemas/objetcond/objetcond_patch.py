from sqlmodel import Field
from ...bases.objetcond import ObjetCondBase

class ObjetCondDBPatch(ObjetCondBase):
   
   
    o_quantite_objet_debut: int = Field(default=0)
    o_quantite_objet_fin: int = Field(default=0)

    # FIXME : Décommenter après avoir créer les autres tables !
    #o_codobj: int | None = Field(default=None, foreign_key="t_objet.codobj", nullable=True)
    #o_codcond: int | None = Field(default=None, foreign_key="t_conditionnement.idcondit", nullable=True)
    
    #objets: Objet | None = Relationship(back_populates="condit")
    #condit: Conditionnement | None = Relationship(back_populates="objets")

    #o_idrelcond: int | None = Field(default=None, primary_key=True, index=True)


 
    