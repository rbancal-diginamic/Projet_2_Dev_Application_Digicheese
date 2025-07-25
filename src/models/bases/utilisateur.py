from datetime import date
from sqlalchemy import Column, String
from sqlmodel import SQLModel, Field


class UtilisateurBase(SQLModel):
    u_nom: str | None = Field(default=None, max_length=50, nullable=True)
    u_prenom: str | None = Field(default=None, max_length=50, nullable=True)
    u_username: str | None = Field(default=None, max_length=50, nullable=True)
    u_date_inscription: date | None = Field(default=None, nullable=True)