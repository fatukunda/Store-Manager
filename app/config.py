import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'This-is-a-very-secret-key')
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    # DATABASE_URI = "postgres://postgres:admin@localhost:5432/store_manager_db"

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    # DATABASE_URI = "postgres://postgres:admin@localhost:5432/store_manager_test_db"

class ProductionConfig(Config):
    DEBUG = False


set_config = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY