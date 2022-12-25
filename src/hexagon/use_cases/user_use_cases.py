from dependency_injector.wiring import Provide

from src.hexagon.events.user_events import UserRegistered
from src.hexagon.gateways.message_bus import MessageBus
from src.hexagon.gateways.repositories.instances_repository import InstancesRepository
from src.hexagon.gateways.repositories.users_repository import UsersRepository
from src.hexagon.models.user import User
from src.hexagon.services.hashing import hash_str
from src.hexagon.use_cases.instance_exceptions import InstanceDoesNotExist
from src.hexagon.use_cases.user_commands import RegisterUserCommand
from src.infrastructure.container import Container

instances_repository: InstancesRepository = Provide[Container.instances_repository]
users_repository: UsersRepository = Provide[Container.users_repository]
message_bus: MessageBus = Provide[Container.message_bus]


def register_user(register_user_command: RegisterUserCommand):
    instance = instances_repository.get(register_user_command.instance_id)
    if not instance:
        raise InstanceDoesNotExist(register_user_command.instance_id)

    user = User(
        id=register_user_command.id,
        instance_id=register_user_command.instance_id,
        email=register_user_command.email,
        hashed_password=hash_str(register_user_command.password.get_secret_value()),
    )
    users_repository.add(user)
    message_bus.publish(UserRegistered(id=user.id, email=user.email, instance_id=user.instance_id))
