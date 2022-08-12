from marshmallow import fields, validates_schema, ValidationError, validates
from flask_marshmallow.fields import AbsoluteURLFor

from models import User
from config.extentions import ma


class UserSchema(ma.SQLAlchemyAutoSchema):
    image = AbsoluteURLFor('uploaded_file', filename='<image>')
    confirm_password = fields.Str(load_only=True, required=True)
    password = fields.Str(load_only=True, required=True)
    
    class Meta:
        model = User
        include_fk = True
        load_instance = True

    @validates_schema
    def validate_confirm_password(self, data, **kwargs):
        if not data["password"] == data["confirm_password"]:
            raise ValidationError("password and confirm password does not match!")

    @validates('email')
    def validate_email(self, value):
        if User.query.filter_by(email=value).first():
            raise ValidationError("This email already exists!")

    @validates('username')
    def validate_username(self, value):
        if User.query.filter_by(username=value).first():
            raise ValidationError("This username already exists!")