
from flask import Flask
import connexion


app  = connexion.App(__name__, specification_dir='swagger/')
import pdb; pdb.set_trace()
app.add_api('user_password.yaml')
application = app.app

# @app.route('/')
def getUserDetails(self):
    return "Say hello to all"


# app.run(host='192.168.1.8', port=4000)

# @app.route('/bye')
# def Saybye():
#     return "Bye see you again"

