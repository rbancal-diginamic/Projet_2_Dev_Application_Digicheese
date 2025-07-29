from datetime import datetime
from sqlmodel import SQLModel, Field


class CommandeBase(SQLModel):
    """Base pour les schémas et models de l'entité Commande"""
    c_date_commande: datetime | None = Field(default=None, nullable=True)
    c_timbre_client: float | None = Field(default=None, nullable=True)
    c_timbre_commande: float | None = Field(default=None, nullable=True)
    c_nombre_colis: int = Field(default=1)
    c_cheque_client: float | None = Field(default=None, nullable=True)
    c_commentaire: str | None = Field(default=None, max_length=255, nullable=True)
    c_barchive: int = Field(default=0)
    c_bstock: int = Field(default=0)
