from sqlmodel import SQLModel, Field


class RoleBase(SQLModel):
    """Base pour les schémas et models de l'entité Role"""
    r_nom: str | None = Field(default=None, max_length=25, nullable=True)