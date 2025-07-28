from sqlmodel import Field
from ..bases.conditionnement import ConditionnementBase

class ConditionnementDB(ConditionnementBase, table=True):
    """Table représentant les conditionnements disponibles pour les objets."""

    __tablename__ = "d_conditionnement"
    
    c_id: int | None = Field(default=None, primary_key=True)
    # FIXME : Décommenter après avoir créer les autres tables !
    #objets: List["ObjetCond"] = Relationship(back_populates="condit")
