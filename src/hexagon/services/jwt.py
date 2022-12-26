from datetime import datetime, timedelta

from dependency_injector.wiring import Provide
from jose import jwt

from src.infrastructure.container import Container

ALGORITHM: str = Provide[Container.config.jwt_algorithm]
JWT_SECRET_KEY: str = Provide[Container.config.jwt_secret_key]


def encode_jwt(subject: str, expires_delta_in_minutes: int = 60, **kwargs) -> str:
    utcnow = datetime.utcnow()
    return _do_encode_jwt(
        {
            "sub": subject,
            "exp": utcnow + timedelta(minutes=expires_delta_in_minutes),
            "nbf": utcnow,
            **kwargs,
        }
    )


def decode_jwt(token: str, subject=None) -> dict:
    return jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM], subject=subject)


def _do_encode_jwt(payload: dict) -> str:
    return jwt.encode(payload, JWT_SECRET_KEY, algorithm=ALGORITHM)
