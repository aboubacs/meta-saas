from typing import Optional

from src.hexagon.gateways.repositories.users_repository import UsersRepository, UserIdAlreadyExists, UserEmailTaken
from src.hexagon.models.user import User


class InMemoryUsersRepository(UsersRepository):
    def __init__(self):
        self.users = {}

    def get(self, user_id: str) -> Optional[User]:
        return self.users.get(user_id)

    def get_by_email(self, email: str) -> Optional[User]:
        for user in self.users.values():
            if user.email == email:
                return user
        return None

    def add(self, user: User) -> None:
        if user.id in self.users:
            raise UserIdAlreadyExists(user.id)
        for user in self.users.values():
            if user.email == user.email:
                raise UserEmailTaken(user.email)
        self.users[user.id] = user

    def update(self, user: User) -> None:
        self.users[user.id] = user

