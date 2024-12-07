from typing import Self

from tortoise import Model

from src.domain.models.user_model import UserModel
from src.domain.repositories.user_repository import UserRepository
from src.presentation.schemas import UserSchema


class UserRepositoryImp(UserRepository):
    def __init__(self, model: Model):
        self.user_model: UserModel = model
        super().__init__()

    async def create_user(self, user: UserSchema) -> UserSchema:
        user = self.user_model.create(**user)
        await user.save()
        await user.refresh_from_db()
        return user

    async def get_users(self) -> list[UserModel]:
        users = await UserModel.all()
        return users

    @classmethod
    async def factory_user_repository(cls, user_model: UserModel) -> Self:
        return cls(user_model)
