from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType
# from Flask_projects.Encrypt_project.password_encryption.settings.config import DevelopmentEnvironmentConfig as dev
from Flask_projects.Encrypt_project.password_encryption.settings import config
import datetime
# db_uri = 'mysql://prad:prad@192.168.1.6:3306/UserPass'
db_uri = config.DB_URL

Base = declarative_base()
engine_db = create_engine(db_uri, connect_args={'connect_timeout': 100})
User_session = sessionmaker(bind=engine_db)
Session = User_session()

class MYtest():
    x = "apple"

class UserModel(Base):
    __tablename__ = 'user_pass_enc'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(200))
    role = Column(String(200))
    enc_password = Column(String(200))
    created_on = Column(DateTime, default=datetime.datetime.utcnow)
    updated_on = Column(DateTime, default=datetime.datetime.utcnow)

class AdminModel(Base):
    __tablename__ = 'admin_users'
    id = Column(Integer, primary_key=True)
    admin_user = Column(String(200))
    admin_password = Column(String(200))
    created_on = Column(DateTime, default=datetime.datetime.utcnow)
    updated_on = Column(DateTime, default=datetime.datetime.utcnow)