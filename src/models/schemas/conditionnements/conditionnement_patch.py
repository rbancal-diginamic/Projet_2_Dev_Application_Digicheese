from decimal import Decimal
from sqlmodel import Field
from ...bases.conditionnement import ConditionnementBase


class ConditionnementPatch(ConditionnementBase):
    """Schéma Conditionnement pour modification en base de données"""
    
    c_libelle: str | None = Field(default=None, max_length=50, nullable=True)
    c_poids: int | None = Field(default=None, nullable=True)
    c_prix: Decimal = Field(default=Decimal("0.0000"), nullable=False)
    c_ordre_impression: int | None = Field(default=None, nullable=True)
    
    # FIXME : Décommenter après avoir créer les autres tables !
    #objets: List["ObjetCond"] = Relationship(back_populates="condit")