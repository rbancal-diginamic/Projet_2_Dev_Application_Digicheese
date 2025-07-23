from abc import ABC, abstractmethod
from typing import Optional, List

from models.db_models.client_db import ClientDB


class ClientRepository(ABC):
    @abstractmethod
    def add(self, client: ClientDB) -> None:
        pass

    @abstractmethod
    def get_by_id(self, client_id: int) -> Optional[ClientDB]:
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> Optional[ClientDB]:
        pass

    @abstractmethod
    def get_all(self) -> List[ClientDB]:
        pass

    @abstractmethod
    def update(self, client: ClientDB) -> None:
        pass

    @abstractmethod
    def delete(self, client_id: int) -> None:
        pass