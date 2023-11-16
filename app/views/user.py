from flask import Blueprint, render_template, request, jsonify, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from app.services import user

user_bp = Blueprint('user_bp', __name__, url_prefix='/user')


@user_bp.route('/status/<status_id>', methods=['PATCH'])
@jwt_required()
def update_status(status_id):
    identity = get_jwt_identity()
    user.update_user_status(username=identity, status_id=status_id)
    return 'success'


@user_bp.route('/user-details')
@jwt_required()
def user_details():
    identity = get_jwt_identity()
    user_data = user.get_user_details(username=identity)
    if not user_data:
        return "User Not Found", 404
    return jsonify(user_data)


@user_bp.route('/all')
@jwt_required()
def get_all_users():
    identity = get_jwt_identity()
    users = user.get_all_users(username=identity)
    if not users:
        return "User Not Found", 404
    return jsonify(users)