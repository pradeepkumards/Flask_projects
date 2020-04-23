from flask_injector import inject
from Flask_projects.Encrypt_project.password_encryption.service.provider import Users_details, Users_create, Login
from Flask_projects.Encrypt_project.password_encryption.utils.security import ApiSecurity

@inject
def login(login: Login) -> dict:
    print("Inside the users!!!")
    # return login.verify_token(login.request.args.get("userid"))
    return login.verify_token()

@inject
def AdminUser(admin_user_login: Login) -> list:
    print ("adding admin users")
    return admin_user_login.create_admin_user()

@inject
def Users(user_provider: Users_details) -> list:
    print("Inside the users!!!")
    return user_provider.get()


@inject
def User(username, user_provider: Users_details) -> list:
    print("Inside the user!!!")
    return user_provider.get_username(username)


@inject
def User_create(user_add: Users_create) -> list:
    return user_add.post()

@inject
def user_encrypt(user_enc: Users_create) -> list:
    return user_enc.pass_enc()

@inject
def user_decrypt(username, user_enc: Users_create) -> list:
    return user_enc.pass_dec(username)