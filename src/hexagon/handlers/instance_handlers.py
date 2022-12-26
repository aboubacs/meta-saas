import uuid

from dependency_injector.wiring import Provide

from src.hexagon.events.instance_events import InstanceCreated
from src.hexagon.gateways.repositories.roles_repository import RolesRepository
from src.hexagon.models.role import Role
from src.infrastructure.container import Container

roles_repository: RolesRepository = Provide[Container.roles_repository]


def create_default_roles(instance_created_event: InstanceCreated) -> None:
    roles_repository.add(Role(id=str(uuid.uuid4()), instance_id=instance_created_event.instance_id, name="owner"))
    roles_repository.add(Role(id=str(uuid.uuid4()), instance_id=instance_created_event.instance_id, name="admin"))
    roles_repository.add(Role(id=str(uuid.uuid4()), instance_id=instance_created_event.instance_id, name="member"))
    roles_repository.add(Role(id=str(uuid.uuid4()), instance_id=instance_created_event.instance_id, name="billing_manager"))