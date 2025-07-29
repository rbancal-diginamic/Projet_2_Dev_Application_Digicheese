from decimal import Decimal
from sqlmodel import SQLModel, Field


class ObjetBase(SQLModel):
    """Base pour les schémas et models de l'entité Objet"""
    o_libelle: str | None = Field(default=None, max_length=50, nullable=True)
    o_taille: str | None = Field(default=None, max_length=50, nullable=True)
    o_prix_unitaire : Decimal | None = Field(default=Decimal("0.0000"), nullable=False)
    o_poids: Decimal = Field(default=Decimal("0.0000"), nullable=False)
    o_indisponible: int = Field(default=0)
    o_ordre_impression: int = Field(default=0)
    o_odre_affichage: int = Field(default=0)
    o_carte_pub: int = Field(default=0)
    o_points: int = Field(default=0)
    o_ordre_affichage: int = Field(default=0)
    
    # condit: List["ObjetCond"] = Relationship(back_populates="objets")
