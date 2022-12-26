import abc
from typing import Optional

from src.hexagon.models.organization import Organization


class OrganizationsRepository(abc.ABC):
    @abc.abstractmethod
    def get(self, organization_id: str) -> Optional[Organization]:
        ...

    @abc.abstractmethod
    def add(self, organization: Organization) -> None:
        ...

    @abc.abstractmethod
    def update(self, organization: Organization) -> None:
        ...


class OrganizationsRepositoryExceptions(Exception):
    pass


class OrganizationIdAlreadyExists(OrganizationsRepositoryExceptions):
    def __init__(self, organization_id: str):
        super().__init__(f"Organization with id {organization_id} already exists")