from abc import ABC, abstractmethod
from src.application.entities import User


class UserRepository(ABC):
    @abstractmethod
    def create(self, user: User) -> str:
        pass

    @abstractmethod
    def get(self, user_id: str) -> User:
        pass
