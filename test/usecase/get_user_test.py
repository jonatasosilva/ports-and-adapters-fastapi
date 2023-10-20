from src.application.usecase import CreateUser
from src.application.usecase import CreateUserInput
from src.application.usecase import GetUser
from src.application.usecase import GetUserInput
from src.infra.repository import UserRepositoryInMemory


def test_deve_criar_um_usuario():
    create_user_input = CreateUserInput("Jonatas")
    user_repository = UserRepositoryInMemory()
    create_user_usecase = CreateUser(user_repository)
    create_user_output = create_user_usecase.execute(create_user_input)
    get_user_usecase = GetUser(user_repository)
    get_user_input = GetUserInput(create_user_output.id)
    get_user_output = get_user_usecase.execute(get_user_input)
    assert get_user_output.name == create_user_input.name
