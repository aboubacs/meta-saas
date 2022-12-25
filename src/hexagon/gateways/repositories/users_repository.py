import abc
from typing import Optional

from src.hexagon.models.user import User


class UsersRepository(abc.ABC):
    @abc.abstractmethod
    def get(self, user_id: str) -> Optional[User]:
        pass

    @abc.abstractmethod
    def add(self, user: User) -> None:
        pass

    @abc.abstractmethod
    def update(self, user: User) -> None:
        pass


class UsersRepositoryErrors(Exception):
    pass


class UserIdAlreadyExists(UsersRepositoryErrors):
    def __init__(self, user_id: str):
        super().__init__(f"User with id {user_id} already exists")