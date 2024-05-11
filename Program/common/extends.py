# extends.py 用于注册flask的插件

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_cors import CORS
from flask_redis import FlaskRedis

db = SQLAlchemy()
migrate = Migrate()
api = Api()
redis_store = FlaskRedis()


def init_exts(app):
    CORS(app)
    db.init_app(app=app)
    migrate.init_app(app=app, db=db)
    api.init_app(app=app)
    redis_store.init_app(app=app)
