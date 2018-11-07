import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'This-is-a-very-secret-key')
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URI = "postgres://postgres:admin@localhost:5432/store_manager_db"

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    DATABASE_URI = "postgres://postgres:admin@localhost:5432/store_manager_test_db"

class ProductionConfig(Config):
    DEBUG = False
    DATABASE_URI ='postgres://akhgvtysmhhqdx:d712e55fb1572068657cca43da19638b5676f338ef2313c1fdcb880b37e51c13@ec2-54-225-98-131.compute-1.amazonaws.com:5432/d1bp4lvbptrsc4'

set_config = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY