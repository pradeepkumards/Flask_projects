from sqlalchemy import create_engine
from Flask_projects.Encrypt_project.password_encryption.models.password_enc import UserModel


def connect_database(db_uri):
    engine_db = create_engine(db_uri, connect_args={'connect_timeout': 100})
    connect_db = engine_db.connect()
    return connect_db


def add_data_to_table(session, data):
    # add_all/bulk_insert_mappings/bulk_save_objects
    session.bulk_save_objects(data)
    session.commit()


def get_all_users(session):
    query = session.query(UserModel)
    return session.execute(query).fetchall()


def get_a_user(session, username):
    query = session.query(UserModel).filter_by(user_name=username)
    return session.execute(query).fetchall()


def session_close(session):
    session.close()

# This is without using models
# def get_all(table_name, db_conn):
#     metadata = sqlalchemy.MetaData()
#     login_users = sqlalchemy.Table(table_name, metadata, autoload_with=db_conn.engine)
#     query = sqlalchemy.select([login_users])
#     result = db_conn.execute(query).fetchall()
#     return result
#
# def get_user(user_name, table_name, db_conn):
#     metadata = sqlalchemy.MetaData()
#     login_users = sqlalchemy.Table(table_name, metadata, autoload_with=db_conn.engine)
#     query = sqlalchemy.select([login_users]).where(login_users.columns.user_name == user_name)
#     result = db_conn.execute(query).fetchall()
#     return result
# # c = connect_database("mysql://prad:prad@192.168.1.5:3306/logindb")
# # get_all(c)
