# /instance/config.py

import os


class Config(object):
    """Parent configuration class."""
    DEBUG = False
    TESTING = False
    DATABASE_URI = "postgres://admin:admin@localhost:5432/store-manager-db"


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DATABASE_URI = "postgres://admin:admin@localhost:5432/store-manager-test-db"
    DEBUG = True

class ProductionConfig(Config):
    """Configurations for Production."""
    DATABASE_URI = "postgres://admin:admin@localhost:5432/store-manager-db"
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}