from dependency_injector.wiring import Provide, inject

from src.hexagon.events.user_events import UserRegistered
from src.hexagon.gateways.email_gateway import EmailGateway
from src.infrastructure.container import Container

email_gateway: EmailGateway = Provide[Container.email_gateway]


def send_activation_email(user_registered: UserRegistered):
    email_gateway.send_email(to=user_registered.email, subject="Activate your account", body="")