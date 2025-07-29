from sqlmodel import SQLModel, Field


class ClientBase(SQLModel):
    """Base pour les schémas et models de l'entité Client"""
    c_genre: str | None = Field(default=None, max_length=8, nullable=True)
    c_nom: str = Field(max_length=40, index=True)
    c_prenom: str = Field(max_length=30)
    c_adresse_1: str | None = Field(default=None, max_length=50, nullable=True)
    c_adresse_2: str | None = Field(default=None, max_length=50, nullable=True)
    c_adresse_3: str | None = Field(default=None, max_length=50, nullable=True)
    c_telephone: str | None = Field(default=None, max_length=13, nullable=True)
    c_email: str | None = Field(default=None, max_length=255, nullable=True)
    c_portable: str | None = Field(default=None, max_length=13, nullable=True)
    c_newsletter: int | None = Field(default=None, nullable=True)
