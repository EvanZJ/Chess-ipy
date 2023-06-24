from abc import ABC, abstractmethod

class CommandHandler(ABC):
    @abstractmethod
    def handle(self, command : list[str]) -> bool:
        pass