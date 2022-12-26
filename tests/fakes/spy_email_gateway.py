from src.hexagon.gateways.email_gateway import EmailGateway


class SpyEmailGateway(EmailGateway):
    def __init__(self):
        self.emails_sent = []

    def send_email(self, to, subject, body):
        self.emails_sent.append({"to": to, "subject": subject, "body": body})