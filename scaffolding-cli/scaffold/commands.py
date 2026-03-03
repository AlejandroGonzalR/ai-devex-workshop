import abc

from typing import TypeVar, Dict

T = TypeVar('T')


class ParametersBag(abc.ABC):
    __bag: Dict

    def __init__(self, bag: Dict = {}) -> None:
        self.__bag = bag

    def all(self) -> Dict:
        return self.__bag

    def get(self, key: str) -> T:
        return self.__bag[key] if key in self.__bag else None

    def set(self, key: str, value: T) -> T:
        self.__bag[key] = value


class Step(abc.ABC):
    __params = ParametersBag

    def __init__(self, params: ParametersBag) -> None:
        self.__params = params

    @classmethod
    @abc.abstractmethod
    def execute(cls) -> None:
        pass

    @property
    def params(self):
        return self.__params
