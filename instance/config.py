import os


class Config(object):
    """Parent configuration class, general settings we want all environments to have by default.  

    Other environment classes will inherit from here and can be used to set settings unique to them.
    """
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


class DevelopmentConfig(Config):
    """ Configurations for development. """
    DEBUG = True


class TestingConfig(Config):
    """ Configurations for testing, with a seprate test database. """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/test_db'
    DEBUG = True


class StagingConfig(Config):
    """ Configurations for staging. """
    DEBUG = True


class ProductionConfig(Config):
    """ Configurations for production. """
    DEBUG = True
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig
}
