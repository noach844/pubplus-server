import datetime

from flask import Blueprint, render_template, request, jsonify, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from app.models import LoginPayload, RegisterPayload
from app.services import auth

auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth')


@auth_bp.route('/login', methods=["POST"])
def login():
    request_data = request.get_json()
    payload = LoginPayload(**request_data)
    access_token, refresh_token = auth.auth_user(username=payload.username, password=payload.password)
    if not access_token:
        return "Bad username or password", 401
    response = make_response("success")

    access_expiration_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
    refresh_expiration_time = datetime.datetime.utcnow() + datetime.timedelta(days=1)

    response.set_cookie("access_token_cookie", value=access_token,expires=access_expiration_time, secure=True, samesite='None')
    response.set_cookie("refresh_token_cookie", value=refresh_token,expires=refresh_expiration_time , secure=True, samesite='None')

    return response


@auth_bp.route('/register', methods=["POST"])
def register():
    request_data = request.get_json()
    payload = RegisterPayload(**request_data)
    if not auth.create_user(payload):
        return "Error Creating User", 500
    return "success", 200


@auth_bp.route("/refresh")
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    access_token = auth.refresh_token(identity=identity)
    response = make_response(jsonify(access_token=access_token))
    response.set_cookie("access_token_cookie", value=access_token, httponly=True, secure=True)
    return response