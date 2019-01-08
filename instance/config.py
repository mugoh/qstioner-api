import os


class BaseConfig:
    DEBUG = False
    TESTING = False
    #SECRET_KEY = os.environ.get('SECRET_KEY')
    CSRF_ENABLED = True
    BUNDLE_ERRORS = True
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access']
    #JWT_SECRET_KET = os.environ.get('JWT_SECRET_KEY')
    JWT_SECRET_KEY = b'\xc2;F]l\x046t\xfe\x08'
    SECRET_KEY = b'\xc2;F]l\x0490u&6t\xfe\x08'


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False


class TestingConfig(BaseConfig):
    TESTING = True
    DEBUG = True


APP_CONFIG = {'development': DevelopmentConfig,
              'testing': TestingConfig,
              'production': ProductionConfig
              }
