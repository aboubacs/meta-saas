import abc
from typing import Optional

from src.hexagon.models.organization_account import OrganizationAccount


class OrganizationAccountsRepository(abc.ABC):
    @abc.abstractmethod
    def get(self, organization_id: str, user_id: str) -> Optional[OrganizationAccount]:
        ...

    @abc.abstractmethod
    def add(self, organization_account: OrganizationAccount) -> None:
        ...

    @abc.abstractmethod
    def update(self, organization_account: OrganizationAccount) -> None:
        ...


class OrganizationAccountsRepositoryExceptions(Exception):
    pass


class OrganizationAccountAlreadyExists(OrganizationAccountsRepositoryExceptions):
    def __init__(self, organization_id: str, user_id: str):
        super().__init__(
            f"OrganizationAccount with organization_id {organization_id} and user_id {user_id} already exists")
