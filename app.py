from litestar import Litestar
from litestar.openapi import OpenAPIConfig
from litestar.openapi.plugins import SwaggerRenderPlugin, YamlRenderPlugin

from src.infra.tortoise_orm.config.tortoise_database_connection import (
    TortoiseDatabaseConnection,
)
from src.routes import user_router

database = TortoiseDatabaseConnection()

app = Litestar(
    [user_router],
    on_startup=[database.init_database],
    on_shutdown=[database.shutdown_database],
    openapi_config=OpenAPIConfig(
        title="Litestart-Test",
        version="1.0.0",
        root_schema_site="swagger",
        render_plugins=[
            SwaggerRenderPlugin(path="/docs"),
            YamlRenderPlugin(path="/spec"),
        ],
    ),
)
