from dataclasses import dataclass

from src.application.repository import UserRepository


@dataclass
class Input:
    id: str


@dataclass
class Output:
    name: str


class GetUser:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def execute(self, input: Input) -> Output:
        user = self.user_repository.get(input.id)
        return Output(user.name)
