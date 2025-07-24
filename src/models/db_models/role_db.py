from sqlmodel import Field
from ..bases.role import RoleBase

class RoleDB(RoleBase, table = True):
    __tablename__ = "t_role"
    r_codrole: int | None = Field(default=None, primary_key=True)