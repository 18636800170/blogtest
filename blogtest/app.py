from flask import Flask

from blogtest.models import db


def create_app(config=None):
    app = Flask(__name__)  # type:Flask
    # 导入配置文件
    app.config.from_object("blogtest.configs.default.DefaultConfig")
    app.config.from_object(config)
    # 注册数据库
    db.init_app(app)

    return app
