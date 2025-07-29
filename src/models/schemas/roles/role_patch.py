from sqlmodel import Field
from ...bases.role import RoleBase


class RolePatch(RoleBase):
    """Schéma Role pour modification en base de données"""
    nom: str | None = Field(default=None, max_length=25, nullable=True)