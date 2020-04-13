from injector import singleton
from flask import Request
from Flask_projects.Encrypt_project.password_encryption.service.provider import Users_details

def configure(binder):
    binder.bind(Users_details, to=Users_details, scope=singleton)
    binder.bind(Request, to=Request, scope=singleton)