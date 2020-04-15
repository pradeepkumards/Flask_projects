
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