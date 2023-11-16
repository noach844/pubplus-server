import datetime

from flask import Blueprint, render_template, request, jsonify, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from app.services import status

status_bp = Blueprint('status_bp', __name__, url_prefix='/status')


@status_bp.route('/')
def get_all_statuses():
    status_list = status.all_statuses()
    if not status_list:
        return None
    return jsonify(status_list)

