from app import app
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate



app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:12345@localhost/tech'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager()
