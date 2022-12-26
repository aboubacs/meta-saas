from typing import Optional

from src.hexagon.gateways.repositories.organizations_repository import OrganizationsRepository, OrganizationIdAlreadyExists
from src.hexagon.models.organization import Organization


class InMemoryOrganizationsRepository(OrganizationsRepository):
    def __init__(self):
        self.organizations = {}

    def get(self, organization_id: str) -> Optional[Organization]:
        return self.organizations.get(organization_id)

    def add(self, organization: Organization) -> None:
        if organization.id in self.organizations:
            raise OrganizationIdAlreadyExists(organization.id)
        self.organizations[organization.id] = organization

    def update(self, organization: Organization) -> None:
        self.organizations[organization.id] = organization

