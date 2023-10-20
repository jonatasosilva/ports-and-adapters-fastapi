from uuid import uuid4

from src.application.entities import User
from src.application.repository import UserRepository


class UserRepositoryInMemory(UserRepository):
    def __init__(self) -> None:
        self.users = []

    def create(self, user: User) -> str:
        user_id = str(uuid4())
        user.id = user_id
        self.users.append(user)
        return user_id

    def get(self, user_id: str) -> User:
        return next(filter(lambda u: u.id == user_id, self.users))
