from dependency_injector.wiring import Provide

from src.hexagon.events.organization_events import OrganizationCreated
from src.hexagon.gateways.repositories.organization_accounts_repository import OrganizationAccountsRepository
from src.hexagon.gateways.repositories.roles_repository import RolesRepository
from src.hexagon.models.organization_account import OrganizationAccount
from src.infrastructure.container import Container

organization_accounts_repository: OrganizationAccountsRepository = Provide[Container.organization_accounts_repository]
roles_repository: RolesRepository = Provide[Container.roles_repository]

def create_owner_organization_account(organization_created_event: OrganizationCreated) -> None:
    owner_role = roles_repository.get_by_name(instance_id=organization_created_event.instance_id, name="owner")
    organization_account = OrganizationAccount(
        organization_id=organization_created_event.organization_id,
        user_id=organization_created_event.owner_user_id,
        role_id=owner_role.id,
    )
    organization_accounts_repository.add(organization_account)
