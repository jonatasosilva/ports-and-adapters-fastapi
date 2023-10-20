from dataclasses import dataclass

from src.application.repository import UserRepository
from src.application.entities import User


@dataclass
class Input:
    name: str


@dataclass
class Output:
    id: str


class CreateUser:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def execute(self, input: Input) -> Output:
        user = User(input.name)
        user_id = self.user_repository.create(user)
        return Output(user_id)
