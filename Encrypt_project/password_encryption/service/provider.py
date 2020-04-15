from flask import Request
from flask_injector import inject
from Flask_projects.Encrypt_project.password_encryption.utils.db import connect_database, get_a_user, \
    get_all_users, add_data_to_table
from Flask_projects.Encrypt_project.password_encryption.models.password_enc import UserModel, Session, AdminModel
import ast
import jwt
from passlib.hash import pbkdf2_sha256


class Login:
    @inject
    def __init__(self, request: Request):
        self.request = request

    def generate_token(self):
        pass

    def verify_token(self):
        pass

    def create_admin_user(self):
        data_value = ast.literal_eval(self.request.data.decode("UTF-8"))
        data_objs = []
        for i in data_value:
            data_objs.append(AdminModel(admin_user=i.get("admin_user"),
                                       admin_password=i.get("admin_password")))
        add_data_to_table(Session, data_objs)
        return "creating admin user"


class Users_details:
    @inject
    def __init__(self, request: Request):
        self.request = request

    def get(self, **kwargs):
        print(self.request)
        # conn = connect_database("mysql://prad:prad@192.168.1.5:3306/logindb")
        user_list = get_all_users(Session)
        print(user_list)
        user_role = []
        for i in user_list:
            u_r = (i[1], i[-1])
            user_role.append(u_r)
        return dict(user_role)

    def get_username(self, user_name, **kwargs):
        print(self.request)
        user_list = get_a_user(Session, self.request.view_args.get("username"))
        user_role = []
        for i in user_list:
            u_r = (i[1], i[-1])
            user_role.append(u_r)
        return dict(user_role)


class Users_create:
    @inject
    def __init__(self, request: Request):
        self.request = request

    def post(self, **kwargs):
        data_value = ast.literal_eval(self.request.data.decode("UTF-8"))
        data_objs = []
        for i in data_value:
            data_objs.append(UserModel(user_name=i.get("user_name"),
                                       role=i.get("role"),
                                       enc_password=i.get("enc_password")))
        add_data_to_table(Session, data_objs)
        return "post success"
