from abc import ABC, abstractmethod
from src.application.entities import User


class UserRepository(ABC):
    @abstractmethod
    def create(user: User) -> str:
        pass
