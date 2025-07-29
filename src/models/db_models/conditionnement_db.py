from sqlmodel import Field
from ..bases.conditionnement import ConditionnementBase

class ConditionnementDB(ConditionnementBase, table=True):
    """Schéma de la table Conditionnement représentée en base de données"""

    __tablename__ = "d_conditionnement"
    
    c_id: int | None = Field(default=None, primary_key=True)
    # FIXME : Décommenter après avoir créer les autres tables !
    #objets: List["ObjetCond"] = Relationship(back_populates="condit")
