from typing import Optional

from src.hexagon.gateways.repositories.users_repository import UsersRepository, UserIdAlreadyExists
from src.hexagon.models.user import User


class InMemoryUsersRepository(UsersRepository):
    def __init__(self):
        self.users = {}

    def get(self, user_id: str) -> Optional[User]:
        return self.users.get(user_id)

    def add(self, user: User) -> None:
        if user.id in self.users:
            raise UserIdAlreadyExists(user.id)
        self.users[user.id] = user

    def update(self, user: User) -> None:
        self.users[user.id] = user

