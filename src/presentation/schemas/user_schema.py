from typing import Annotated

from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator

from src.domain.models.user_model import UserModel

UserTortoiseSchema = pydantic_model_creator(
    UserModel, exclude=["updated_at", "created_at", "id"]
)
UserTortoiseListSchema = pydantic_queryset_creator(
    UserModel, exclude=["password", "id"]
)


UserRequestSchema = Annotated[UserTortoiseSchema, "Schema para um único usuário"]
UserResponseSchema = Annotated[
    UserTortoiseListSchema, "Schema para uma lista de usuários"
]
