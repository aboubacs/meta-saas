from src.hexagon.events.user_events import UserRegistered


def test_user_registered_should_send_activation_email(message_bus, email_gateway, instance):
    message_bus.publish(UserRegistered(user_id="1", email="test-user@email.com", instance_id=instance.id))
    assert email_gateway.emails_sent
    assert email_gateway.emails_sent[0]["to"] == "test-user@email.com"
    assert email_gateway.emails_sent[0]["subject"] == "Activate your account"