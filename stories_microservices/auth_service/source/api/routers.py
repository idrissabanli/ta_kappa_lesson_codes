from flask import request, send_from_directory, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from marshmallow import ValidationError
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from app import app
from utils import save_image, confirm_token
from schemas.user_schema import UserSchema
from models import User



@app.route('/api/auth/register', methods=['POST'])
def register():
    image = request.files.get('image', None)
    user_data = dict(request.form) or request.get_json(silent=True) or dict()
    user_data['image'] = save_image(image) if image else None
    try:
        user = UserSchema().load(user_data)
        user.password = generate_password_hash(user_data.get('password'))
        user.save()
        user.send_confirmation_mail()
        return UserSchema().jsonify(user), 201
    except ValidationError as err:
        return err.messages, 400

@app.route('/media/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['MEDIA_ROOT'], filename)

@app.route('/confirmation/<token>')
def confirm_email(token):
    email = confirm_token(token)
    if not email:
        return jsonify(mesaage='The confirmation link is invalid or has expired.'), 200
    user = User.query.filter_by(email=email).first_or_404()
    if user.is_active:
        return jsonify(mesaage='Account already confirmed. Please login.'), 200
    user.is_active = True
    user.save()
    # user.send_data_post_service() normalda burda olmalidir!
    return jsonify(mesaage='You have confirmed your account. Thanks!'), 200


@app.route("/api/auth/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = User.query.filter_by(username=username).first()
    if not user or check_password_hash(password, user.password) or not user.is_active:
        return jsonify({"msg": "Username or password incorrect!"}), 401

    access_token = create_access_token(identity=user.id)
    refresh_token = create_refresh_token(identity=user.id)
    return jsonify(access_token=access_token, refresh_token=refresh_token), 200

@app.route("/protected")
@jwt_required()
def protected():
    identity = get_jwt_identity()
    user = User.query.filter_by(id=identity).first()
    print(user.username)
    return jsonify(identity=identity)

@app.route("/refresh")
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    return jsonify(access_token=access_token)
