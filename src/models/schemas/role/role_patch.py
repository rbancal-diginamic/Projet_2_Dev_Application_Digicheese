from sqlmodel import Field
from ...bases.role import RoleBase


class RolePatch(RoleBase):
    nom: str | None = Field(default=None, max_length=25, nullable=True)