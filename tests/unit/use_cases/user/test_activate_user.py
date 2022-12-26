import pytest

from src.hexagon.models.user import User
from src.hexagon.services import jwt
from src.hexagon.use_cases.user_commands import ActivateUserCommand
from src.hexagon.use_cases.user_exceptions import InvalidActivationToken, UserAlreadyActivated
from src.hexagon.use_cases.user_use_cases import activate_user


@pytest.fixture(autouse=True)
def unactivated_user(users_repository, instance):
    user = User(id="1", email="test-email@email.com", instance_id=instance.id, activated=False,
                hashed_password="hashed-password")
    users_repository.add(user)
    return user


def test_should_activate_user_if_token_is_valid(unactivated_user, users_repository):
    activate_user(ActivateUserCommand(user_id=unactivated_user.id, token=jwt.encode_jwt(unactivated_user.id)))
    assert users_repository.get(unactivated_user.id).activated is True


def test_should_raise_if_token_is_invalid(unactivated_user, users_repository):
    with pytest.raises(InvalidActivationToken):
        activate_user(ActivateUserCommand(user_id=unactivated_user.id, token="invalid-token"))
    assert users_repository.get(unactivated_user.id).activated is False


def test_should_raise_if_user_is_already_activated(unactivated_user, users_repository):
    unactivated_user.activate()
    users_repository.update(unactivated_user)
    with pytest.raises(UserAlreadyActivated):
        activate_user(ActivateUserCommand(user_id=unactivated_user.id, token=jwt.encode_jwt(unactivated_user.id)))
    assert users_repository.get(unactivated_user.id).activated is True