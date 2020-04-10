
from flask import Flask
from flask_injector import inject
from password_encryption.service.provider import Users_details
import connexion



@inject
def Users(user_provider: Users_details) -> list:
#def Users():
    import pdb; pdb.set_trace()
    #return Users_details.get({"name": "sd"})
    return Users_details.get()



