from sqlmodel import Field
from ...bases.objet import ObjetBase


class ObjetPatch(ObjetBase):
    """Schéma Objet pour modification en base de données"""
    o_indisponible: int = Field(nullable=True)
    o_ordre_impression: int = Field(nullable=True)
    o_odre_affichage: int = Field(nullable=True)
    o_carte_pub: int = Field(nullable=True)
    o_points: int = Field(nullable=True)
    o_ordre_affichage: int = Field(nullable=True)
    # FIXME : Décommenter après avoir créer les autres tables !
    # condit: List["ObjetCond"] = Relationship(back_populates="objets")
