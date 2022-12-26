from dependency_injector.wiring import Provide
from jose import JWTError

from src.hexagon.events.user_events import UserRegistered
from src.hexagon.gateways.message_bus import MessageBus
from src.hexagon.gateways.repositories.instances_repository import InstancesRepository
from src.hexagon.gateways.repositories.users_repository import UsersRepository
from src.hexagon.models.user import User
from src.hexagon.services import jwt
from src.hexagon.services.hashing import hash_str
from src.hexagon.use_cases.instance_exceptions import InstanceDoesNotExist
from src.hexagon.use_cases.user_commands import RegisterUserCommand, ActivateUserCommand
from src.hexagon.use_cases.user_exceptions import UserAlreadyActivated, UserDoesNotExist, InvalidActivationToken
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
    message_bus.publish(UserRegistered(user_id=user.id, email=user.email, instance_id=user.instance_id))


def activate_user(activate_user_command: ActivateUserCommand):
    _verify_token(activate_user_command)

    user = users_repository.get(activate_user_command.user_id)
    if not user:
        raise UserDoesNotExist(activate_user_command.user_id)

    if user.activated:
        raise UserAlreadyActivated(activate_user_command.user_id)

    user.activate()
    users_repository.update(user)


def _verify_token(activate_user_command):
    try:
        decoded_jwt = jwt.decode_jwt(activate_user_command.token)
    except JWTError:
        raise InvalidActivationToken(activate_user_command.user_id)
    if decoded_jwt["sub"] != activate_user_command.user_id:
        raise InvalidActivationToken(activate_user_command.user_id)
