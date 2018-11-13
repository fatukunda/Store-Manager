import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'This-is-a-very-secret-key')
    DEBUG = False
    JWT_SECRET_KEY = 'Code-Benders'


class DevelopmentConfig(Config):
    DEBUG = True
    # DATABASE_URI = "postgres://postgres:admin@localhost:5432/store_manager_db"

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    # DATABASE_URI = "postgres://postgres:admin@localhost:5432/store_manager_test_db"

class ProductionConfig(Config):
    DEBUG = False
    # DATABASE_URI ='postgres://plwlxtobexznlo:752178d58b5ffaebe1e11a9000136b77d76035f5dea0d2c82926236f2dcd2385@ec2-184-73-199-189.compute-1.amazonaws.com:5432/dektsfu001hn6g'


set_config = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY