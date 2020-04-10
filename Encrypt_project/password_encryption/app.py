
from flask import Flask
import connexion

"""
class GetUserDetails():

    def get_user():
        return "Say hello to all today!!!---"

class CreateUpdateUsers():

    def create_user():
        return "creating user"


    def update_user():
        return "update user"


    def delete_user():
        return "delete user"
"""

app  = connexion.FlaskApp(__name__, port=4000, host='192.168.1.7',specification_dir='swagger/')
app.add_api('user_password.yaml')


