
# from Flask_projects.Encrypt_project.password_encryption.utils.db import connect_database


from Flask_projects.Encrypt_project.password_encryption.models.password_enc import Base

import datetime
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime
engine = create_engine('mysql://prad:prad@192.168.1.6:3306/UserPass', echo = True)
meta = MetaData()

students = Table(
   'admin_users', meta,
   Column('id', Integer, primary_key = True),
   Column('admin_user', String(200)),
   Column('admin_password', String(1000)),
   Column('created_on', DateTime, default=datetime.datetime.utcnow),
   Column('updated_on', DateTime, default=datetime.datetime.utcnow),

)
meta.create_all(engine)

