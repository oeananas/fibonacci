import os


class BaseConfig:
    """ Base config class. This fields will use by production and development server """
    FLASK_APP = 'app.py'
    DEBUG = True
    TESTING = True


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False


config = {
    'base': 'config.BaseConfig',
    'production': 'config.ProductionConfig',
    'development': 'config.DevelopmentConfig',
}


def configure_app(app):
    config_name = os.environ.get('CONFIGURATION', 'production')
    app.config.from_object(config[config_name])
    app.config.from_pyfile('config.py', silent=True)
    return app
