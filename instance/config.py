import os


class BaseConfig:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY',
                                b'\xc2;F]l\x046t\xfe\x08'
                                )
    CSRF_ENABLED = True
    JWT_SECRET_KET = os.environ.get('JWT_SECRET_KEY',
                                    b'\xa3$\x0bm\xae\xbbmd\x12\x8f'
                                    )


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
