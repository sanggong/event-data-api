from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

db = SQLAlchemy()


def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}:3306/{}'.format(config.RDS['USER'],
                                                                                      config.RDS['PASSWORD'],
                                                                                      config.RDS['URL'],
                                                                                      config.RDS['NAME'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app
