from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType

db_uri = 'mysql://prad:prad@192.168.1.6:3306/UserPass'

Base = declarative_base()
engine_db = create_engine(db_uri, connect_args={'connect_timeout': 100})
User_session = sessionmaker(bind=engine_db)
Session = User_session()


class UserModel(Base):
    __tablename__ = 'user_pass_enc'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(200))
    role = Column(String(200))
    enc_password = Column(String(200))
