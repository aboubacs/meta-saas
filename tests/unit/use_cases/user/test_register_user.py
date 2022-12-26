import pytest

from src.hexagon.events.user_events import UserRegistered
from src.hexagon.gateways.repositories.users_repository import UserIdAlreadyExists, UserEmailTaken
from src.hexagon.use_cases.instance_exceptions import InstanceDoesNotExist
from src.hexagon.use_cases.user_commands import RegisterUserCommand
from src.hexagon.use_cases.user_use_cases import register_user


@pytest.fixture
def command(instance):
    return RegisterUserCommand(instance_id=instance.id, id="1", email="test-user@email.com", password="azer1234")


def test_should_register_a_user_in_an_instance(command, instance, users_repository):
    register_user(command)
    user = users_repository.get("1")
    assert user.id == "1"
    assert user.email == "test-user@email.com"
    assert user.instance_id == instance.id
    assert user.hashed_password is not None
    assert user.activated is False


def test_should_raise_if_user_id_exists(command, instance, users_repository):
    register_user(command)
    with pytest.raises(UserIdAlreadyExists):
        register_user(command)


def test_should_raise_if_instance_does_not_exist(users_repository, command):
    command.instance_id = "unknown"
    with pytest.raises(InstanceDoesNotExist):
        register_user(command)


def test_should_raise_if_email_is_taken(command, users_repository):
    register_user(command)
    command.id = "2"
    with pytest.raises(UserEmailTaken):
        register_user(command)


def test_should_emit_user_created_event(message_bus, command):
    register_user(command)
    assert message_bus.messages
    assert isinstance(message_bus.messages[0], UserRegistered)
    assert message_bus.messages[0].id == "1"
    assert message_bus.messages[0].email == "test-user@email.com"
    assert message_bus.messages[0].instance_id == command.instance_id
