from src.hexagon.events.organization_events import OrganizationCreated
from src.hexagon.events.user_events import UserRegistered
from src.hexagon.gateways.message_bus import MessageBus
from src.hexagon.handlers.emailing import send_activation_email
from src.hexagon.handlers.organization_account_handlers import create_owner_organization_account

EVENT_HANDLERS = {
    UserRegistered: [send_activation_email],
    OrganizationCreated: [create_owner_organization_account],
}


def wire(message_bus: MessageBus):
    for event_cls, handlers in EVENT_HANDLERS.items():
        for handler in handlers:
            message_bus.register_handler(event_cls, handler)
