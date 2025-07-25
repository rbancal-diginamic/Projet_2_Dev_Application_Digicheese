from abc import ABC, abstractmethod
from typing import Optional, List
from sqlmodel import SQLModel


class AbstractRepository(ABC):
    @abstractmethod
    def add(self, objet: SQLModel) -> SQLModel:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> SQLModel | None:
        pass

    @abstractmethod
    def get_all(self) -> List[SQLModel]:
        pass

    @abstractmethod
    def update(self, id: int, objet: SQLModel) -> SQLModel | None:
        pass

    @abstractmethod
    def delete(self, id: int) -> bool:
        pass