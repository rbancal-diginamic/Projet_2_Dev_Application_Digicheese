from abc import ABC, abstractmethod
from typing import Optional, List
from sqlmodel import SQLModel


class AbstractRepository(ABC):
    @abstractmethod
    def add(self, objet: dict) -> None:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[SQLModel]:
        pass

    @abstractmethod
    def get_all(self) -> List[SQLModel] | None:
        pass

    @abstractmethod
    def update(self, objet: dict) -> None:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass