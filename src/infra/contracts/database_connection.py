from abc import ABC, abstractmethod


class DatabaseConnection(ABC):
    @abstractmethod
    async def init_database(self) -> None:
        pass

    async def shutdown_database(self) -> None:
        pass
