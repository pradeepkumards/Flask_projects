from flask import Request
from flask_injector import inject
from Flask_projects.Encrypt_project.password_encryption.utils.db_connection import connect_database, get_all, get_user, add_data_to_table
from Flask_projects.Encrypt_project.password_encryption.models.password_enc import UserModel, Session

class Users_details:
    @inject
    def __init__(self, request: Request):
        self.request = request

    def get(self, **kwargs):
        print(self.request)
        conn = connect_database("mysql://prad:prad@192.168.1.5:3306/logindb")
        user_list = get_all('login_app_users', conn)
        user_role = []
        for i in user_list:
            u_r = (i[1], i[-1])
            user_role.append(u_r)
        return dict(user_role)

    def get_username(self, user_name, **kwargs):
        print(self.request)
        conn = connect_database("mysql://prad:prad@192.168.1.5:3306/UserPass")
        user_list = get_user(user_name, 'user_pass_enc', conn)
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
        # data_value = [("apple", "admin_role", "iuweciwue"), ("apple", "admin_role", "iuweciswue"),
        #               ("apple", "user_role", "iuweciwaue")]
        data_value = self.request.args()
        data_objs = []
        for i in data_value:
            data_objs.append(UserModel(user_name=i[0], role=i[1], enc_password=i[2]))
        add_data_to_table(Session, data_objs)
        return "post success"