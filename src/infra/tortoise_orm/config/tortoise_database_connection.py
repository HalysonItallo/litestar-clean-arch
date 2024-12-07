from tortoise import Tortoise
from tortoise.connection import connections

from src.infra.contracts.database_connection import DatabaseConnection


class TortoiseDatabaseConnection(DatabaseConnection):
    _tortoise_orm_config = {
        "connections": {
            "default": "sqlite://database.db",
        },
        "apps": {
            "models": {
                "models": [
                    "src.domain.models",
                ],
                "default_connection": "default",
            },
        },
    }

    async def init_database(self) -> None:
        await Tortoise.init(config=self._tortoise_orm_config)
        await Tortoise.generate_schemas()

    async def shutdown_database(self) -> None:
        await connections.close_all()
