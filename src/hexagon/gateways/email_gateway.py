import abc


class EmailGateway(abc.ABC):
    @abc.abstractmethod
    def send_email(self, to, subject, body):
        ...
