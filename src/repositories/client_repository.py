from abc import ABC, abstractmethod
from typing import Optional, List
from models.db_models.client_db import ClientDB
from models.schemas.clients.client_patch import ClientPatch
from models.schemas.clients.client_post import ClientPost


class ClientRepository(ABC):
    @abstractmethod
    def add(self, client: ClientPost) -> None:
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
    def update(self, client: ClientPatch) -> None:
        pass

    @abstractmethod
    def delete(self, client_id: int) -> None:
        pass
