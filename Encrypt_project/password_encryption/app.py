
from flask import Flask
import connexion
from flask_injector import FlaskInjector
from Flask_projects.Encrypt_project.password_encryption.service import configure
from connexion.resolver import RestyResolver

# app  = connexion.FlaskApp(__name__, port=4000, host='192.168.1.7',specification_dir='swagger/')
app  = connexion.FlaskApp(__name__, port=4000, specification_dir='swagger/')
app.add_api('user_password.yaml', resolver=RestyResolver("api"))
flask_injector = FlaskInjector(app=app.app)
# , modules=[configure]
