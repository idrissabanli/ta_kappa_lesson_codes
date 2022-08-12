import os
from app import app
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:12345@localhost:5432/tech'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager()
ma = Marshmallow(app)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
app.config['MEDIA_ROOT'] = os.path.join(BASE_DIR, 'media')
