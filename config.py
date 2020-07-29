import os
import redis


class BaseConfig:
    """ Base config class. This fields will use by production and development server. """
    FLASK_APP = 'app.py'


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False


config = {
    'production': 'config.ProductionConfig',
    'development': 'config.DevelopmentConfig',
}


def configure_app(app):
    """ Setting app configuration. """

    config_name = os.environ.get('CONFIGURATION', 'production')
    app.config.from_object(config[config_name])
    app.config.from_pyfile('config.py', silent=True)
    return app


def is_redis_available():
    """ Checking availability of redis service. """

    rs = redis.Redis('redis://redis:6379')
    try:
        rs.client_list()
        return True
    except redis.ConnectionError:
        return False


def get_cache_config(app):
    """ Getting cache configuration. If redis is not available, use simple cache type. """

    if not is_redis_available():
        return {
            'CACHE_TYPE': 'simple'
        }
    return {
        'CACHE_TYPE': 'redis',
        'CACHE_REDIS_URL': 'redis://redis:6379/0'
    }
