from typing import Optional

from src.hexagon.gateways.repositories.organization_accounts_repository import OrganizationAccountsRepository, \
    OrganizationAccountAlreadyExists
from src.hexagon.models.organization_account import OrganizationAccount


class InMemoryOrganizationAccountsRepository(OrganizationAccountsRepository):
    def __init__(self):
        self.organizations = []

    def get(self, organization_id: str, user_id: str) -> Optional[OrganizationAccount]:
        for organization in self.organizations:
            if organization.organization_id == organization_id and organization.user_id == user_id:
                return organization

    def add(self, organization_account: OrganizationAccount) -> None:
        for organization in self.organizations:
            if organization.organization_id == organization_account.organization_id and organization.user_id == organization_account.user_id:
                raise OrganizationAccountAlreadyExists(organization_account.organization_id, organization_account.user_id)
        self.organizations.append(organization_account)

    def update(self, organization_account: OrganizationAccount) -> None:
        for organization in self.organizations:
            if organization.organization_id == organization_account.organization_id and organization.user_id == organization_account.user_id:
                self.organizations.remove(organization)
                self.organizations.append(organization_account)
