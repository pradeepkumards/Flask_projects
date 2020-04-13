from flask_injector import inject
from Flask_projects.Encrypt_project.password_encryption.service.provider import Users_details


@inject
def Users(user_provider: Users_details) -> list:
    print("Inside the users!!!")
    return user_provider.get()


@inject
def User(username, user_provider: Users_details) -> list:
    print("Inside the user!!!")
    return user_provider.get_username(username)


@inject
def User_create(user_provider: Users_details) -> list:

    return user_provider.create()
