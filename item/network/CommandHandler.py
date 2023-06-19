from abc import ABC, abstractmethod

class CommandHandler(ABC):
    @abstractmethod
    def Handle(self, command : str) -> bool:
        pass