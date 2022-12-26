import pytest

from src.hexagon.models.user import User
from src.hexagon.services.hashing import hash_str
from src.hexagon.services.jwt import decode_jwt
from src.hexagon.use_cases.user_commands import LoginWithPasswordCommand
from src.hexagon.use_cases.user_exceptions import InvalidCredentials
from src.hexagon.use_cases.user_use_cases import login_with_password


@pytest.fixture
def password():
    return "password"


@pytest.fixture
def user(users_repository, instance, password):
    user = User(id="1", email="test-email@email.com", instance_id=instance.id, activated=True,
                hashed_password=hash_str(password))
    users_repository.add(user)
    return user


def test_login_with_password_should_return_jwt_if_credentials_are_valid(user, password):
    jwt = login_with_password(LoginWithPasswordCommand(email=user.email, password=password))
    assert jwt is not None


def test_login_with_password_should_raise_if_email_is_unknown(password):
    with pytest.raises(InvalidCredentials):
        login_with_password(LoginWithPasswordCommand(email="unknown@email.com", password=password))


def test_login_with_password_should_raise_if_password_is_invalid(user):
    with pytest.raises(InvalidCredentials):
        login_with_password(LoginWithPasswordCommand(email=user.email, password="invalid-password"))


def test_login_with_password_should_return_a_valid_token(user, password):
    jwt = login_with_password(LoginWithPasswordCommand(email=user.email, password=password))
    assert jwt is not None
    decoded_jwt = decode_jwt(jwt)
    assert decoded_jwt["sub"] == user.id