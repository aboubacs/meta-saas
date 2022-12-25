from dependency_injector.wiring import Provide

from src.hexagon.gateways.repositories.instances_repository import InstancesRepository
from src.hexagon.gateways.repositories.users_repository import UsersRepository
from src.hexagon.models.user import User
from src.hexagon.use_cases.instance_exceptions import InstanceDoesNotExist
from src.hexagon.use_cases.user_commands import RegisterUserCommand
from src.infrastructure.container import Container

instances_repository: InstancesRepository = Provide[Container.instances_repository]
users_repository: UsersRepository = Provide[Container.users_repository]


def register_user(register_user_command: RegisterUserCommand):
    instance = instances_repository.get(register_user_command.instance_id)
    if not instance:
        raise InstanceDoesNotExist(register_user_command.instance_id)
    user = User(
        id=register_user_command.id,
        instance_id=register_user_command.instance_id,
        email=register_user_command.email
    )
    users_repository.add(user)
