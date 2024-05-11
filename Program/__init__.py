from flask import Flask

from Program.common.extends import init_exts


def create_app():
    # 实例化flask
    app = Flask(__name__)
    # 设置唯一密钥
    app.secret_key = 'yzu_wxapp'
    # 配置mysql数据库
    db_uri = 'mysql+pymysql://root:123456@localhost:3306/yzu_wxapp'
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # 初始化插件
    init_exts(app=app)
    return app


from Program.resource import UserResource
from Program.resource import SuggestionResource
from Program.models import user
from Program.models import suggestion