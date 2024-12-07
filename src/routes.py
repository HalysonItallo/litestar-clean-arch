from litestar import Router

from src.presentation.controllers.user_controller import UserController

user_router = Router(route_handlers=[UserController], path="/")
