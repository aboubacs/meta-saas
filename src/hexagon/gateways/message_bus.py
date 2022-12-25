import abc
from typing import Type, Callable


class MessageBus(abc.ABC):
    @abc.abstractmethod
    def publish(self, message) -> None:
        ...

    @abc.abstractmethod
    def register(self, message_type: Type, handler: Callable) -> None:
        ...
