import os


class BaseConfig():
    pass


class ProductionEnvironmentConfig(BaseConfig):
    DEBUG = False


class DevelopmentEnvironmentConfig(BaseConfig):
    DEBUG = True


class TestEnvironmentConfig(BaseConfig):
    DEBUG = True


DB_URL = os.getenv("DB_URL")

ADMIN_USER_PASS = os.getenv("ADMIN_USER_PASS")

SEC_KEY = os.getenv("SEC_KEY")
SEC_PASS = os.getenv("SEC_PASS")
SEC_ITER = os.getenv("SEC_ITER")
SEC_SALT = os.getenv("SEC_SALT")
