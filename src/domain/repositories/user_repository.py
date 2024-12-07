from abc import ABC, abstractmethod

from src.presentation.schemas import UserListSchema, UserSchema


class UserRepository(ABC):
    @abstractmethod
    async def create_user(self, user: UserSchema) -> UserSchema:
        pass

    @abstractmethod
    async def get_users(self) -> UserListSchema:
        pass
