from abc import ABC, abstractmethod


class Command(ABC):
    """
    Base class for all commands.

    Every command must implement:

    execute()
        Performs the operation.

    undo()
        Reverses the operation.
    """

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass