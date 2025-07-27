from datetime import date
from sqlalchemy import Column, String
from sqlmodel import SQLModel, Field


class CommandeBase(SQLModel):
    
    c_datcdee: date | None = Field(default=None, nullable=True)
    c_timbre_client: float | None = Field(default=None, nullable=True)
    c_timbre_commande: float | None = Field(default=None, nullable=True)
    c_nombre_colis: int = Field(default=1)
    c_cheque_client: float | None = Field(default=None, nullable=True)
    c_commentaire: str | None = Field(default=None, max_length=255, nullable=True)
    c_barchive: int = Field(default=0)
    c_bstock: int = Field(default=0)
    