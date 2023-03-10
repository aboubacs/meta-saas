import abc
from typing import Optional

from src.hexagon.models.user import User


class UsersRepository(abc.ABC):
    @abc.abstractmethod
    def get(self, user_id: str) -> Optional[User]:
        ...

    @abc.abstractmethod
    def get_by_email(self, email: str) -> Optional[User]:
        ...

    @abc.abstractmethod
    def add(self, user: User) -> None:
        ...

    @abc.abstractmethod
    def update(self, user: User) -> None:
        ...


class UsersRepositoryExceptions(Exception):
    pass


class UserIdAlreadyExists(UsersRepositoryExceptions):
    def __init__(self, user_id: str):
        super().__init__(f"User with id {user_id} already exists")


class UserEmailTaken(UsersRepositoryExceptions):
    def __init__(self, email: str):
        super().__init__(f"User with email {email} already exists")
