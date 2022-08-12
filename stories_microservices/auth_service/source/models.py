from flask import url_for, render_template
from flask_login import UserMixin
from slugify import slugify
from config.extentions import db, login_manager
from publisher import Publish
from utils import generate_confirmation_token

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


class SaveMixin(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)

    updated_at = db.Column(db.DateTime, server_default=db.func.now())
    created_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class User(UserMixin, SaveMixin):
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(300), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    is_active = db.Column(db.Boolean(), default=False)
    image = db.Column(db.String(255), nullable=True)
    bio = db.Column(db.Text, nullable=True)

    def send_confirmation_mail(self):
        token = generate_confirmation_token(email=self.email)
        confirm_url = url_for('confirm_email', token=token, _external=True)
        html = render_template('confirmation_mail.html', confirm_url=confirm_url)
        subject = "Please confirm your email"
        data = {
            'body': html,
            'subject': subject,
            'subtype': 'html',
            'recipients': [self.email,]
        }
        Publish(data=data, event_type='send_mail')
