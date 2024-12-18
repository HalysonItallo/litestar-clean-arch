from dataclasses import dataclass
from typing import Annotated

from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator

from src.domain.models.user_model import UserModel

UserTortoiseSchema = pydantic_model_creator(
    UserModel, exclude=["updated_at", "created_at", "id"]
)
UserTortoiseListSchema = pydantic_queryset_creator(
    UserModel, exclude=["password", "id"]
)


@dataclass
class UserSchema:
    name: str
    email: str
    password: str
    confirm_password: str


# UserSchema = Annotated[UserTortoiseSchema, "Schema para um único usuário"]
UserListSchema = Annotated[UserTortoiseListSchema, "Schema para uma lista de usuários"]
