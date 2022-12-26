from collections import defaultdict
from typing import Type, Callable

from src.hexagon.gateways.message_bus import MessageBus


class InMemoryMessageBus(MessageBus):
    def __init__(self):
        self.messages = []
        self.handlers = defaultdict(list)

    def register_handler(self, message_type: Type, handler: Callable):
        self.handlers[message_type].append(handler)

    def publish(self, message):
        self.messages.append(message)
        if type(message) in self.handlers:
            for handler in self.handlers[type(message)]:
                handler(message)

    def clear(self):
        self.messages = []
