from sqlmodel import SQLModel, Field


class DepartementBase(SQLModel):
    code_departement: str = Field(max_length=3)
    nom_departement: str = Field(default=None, max_length=50, nullable=True)