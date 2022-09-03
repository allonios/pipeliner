from abc import ABCMeta, abstractmethod
from typing import Any


class BaseReader(metaclass=ABCMeta):
    """
    A base class for readers
    """

    @abstractmethod
    def read(self) -> Any:
        """
        A abstract method that defines reading logic.
        :return:
        """
        ...


class DefaultReader(BaseReader):
    """
    A reader used to return a default value, used when the reading logic is too
    trivial to be wrapped in a reader, or there is an external source for the
    data being read.
    """

    def __init__(self, default_value: Any) -> None:
        self.default_value = default_value

    def read(self) -> Any:
        return self.default_value
