from litestar import Controller, Response, get, post, status_codes
from litestar.di import Provide

from src.domain.models.user_model import UserModel
from src.infra.tortoise_orm.repositories.user_repository_imp import UserRepositoryImp
from src.presentation.schemas import UserListSchema, UserSchema


def get_user_model():
    return UserModel()


def get_user_repository(user_model: UserModel):
    return UserRepositoryImp(user_model)


class UserController(Controller):
    path = "/users"

    dependencies = {
        "user_model": Provide(get_user_model, sync_to_thread=False),
        "user_repository": Provide(get_user_repository, sync_to_thread=False),
    }

    @get()
    async def get_all_users(
        self,
        user_repository: UserRepositoryImp,
    ) -> UserListSchema:
        try:
            users = []

            if not users:
                return Response(status_code=200, content=[])

            return UserListSchema.from_queryset(user_repository.get_users())
        except Exception as err:
            print(str(err))
            return Response(status_code=status_codes.HTTP_500_INTERNAL_SERVER_ERROR)

    @post()
    async def create_user(
        self,
        data: UserSchema,
        user_repository: UserRepositoryImp,
    ) -> UserSchema:
        try:
            user = await user_repository.create_user(data)

            if not user:
                return Response(
                    status_code=status_codes.HTTP_422_UNPROCESSABLE_ENTITY,
                )

            user_serialized = await UserSchema.from_tortoise_orm(user)

            return user_serialized.model_dump()
        except Exception as err:
            print(str(err))
            return Response(status_code=status_codes.HTTP_500_INTERNAL_SERVER_ERROR)
