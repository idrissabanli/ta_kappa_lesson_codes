import os
import datetime
import redis
from app import app
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager


class RedisConfig:
    CHANNEL_NAME = 'events'

    @property
    def client(self):
        return redis.Redis(host='localhost', port=6379, db=0)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:12345@localhost:5433/tech'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'kjndfdjsbnf'
app.config['SECURITY_PASSWORD_SALT'] = 'kjndfdjsbnf'
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(seconds=30)
jwt = JWTManager(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager()
ma = Marshmallow(app)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
app.config['MEDIA_ROOT'] = os.path.join(BASE_DIR, 'media')
