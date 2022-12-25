import pytest

from src.hexagon.gateways.repositories.users_repository import UserIdAlreadyExists
from src.hexagon.use_cases.instance_exceptions import InstanceDoesNotExist
from src.hexagon.use_cases.user_commands import RegisterUserCommand
from src.hexagon.use_cases.user_use_cases import register_user


def test_should_register_a_user_in_an_instance(instance, users_repository):
    register_user(RegisterUserCommand(instance_id=instance.id, id="1", email="test-user@email.com"))
    user = users_repository.get("1")
    assert user.id == "1"
    assert user.email == "test-user@email.com"
    assert user.instance_id == instance.id


def test_should_raise_if_user_id_exists(instance, users_repository):
    register_user(RegisterUserCommand(instance_id=instance.id, id="1", email="test-user@email.com"))
    with pytest.raises(UserIdAlreadyExists):
        register_user(RegisterUserCommand(instance_id=instance.id, id="1", email="test-user@email.com"))


def test_should_raise_if_instance_does_not_exist(users_repository):
    with pytest.raises(InstanceDoesNotExist):
        register_user(RegisterUserCommand(instance_id="2", id="1", email="test-user@email.com"))