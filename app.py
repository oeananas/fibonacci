import os
from flask import Flask
from flask_caching import Cache
from dotenv import load_dotenv
from config import configure_app

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


app = configure_app(Flask(__name__))

if app.config['TESTING']:
    cache_conf = {
        'CACHE_TYPE': 'simple'
    }
else:
    cache_conf = {
        'CACHE_TYPE': 'redis',
        'CACHE_REDIS_URL': 'redis://redis:6379/0'
    }

cache = Cache(app, config=cache_conf)

from fib import controllers

if __name__ == '__main__':
    app.run()
