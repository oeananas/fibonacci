import os
from flask import Flask
from flask_caching import Cache
from dotenv import load_dotenv
from config import configure_app, get_cache_config

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

app = configure_app(Flask(__name__))
cache = Cache(app, config=get_cache_config(app))

from fib import controllers

if __name__ == '__main__':
    app.run()
