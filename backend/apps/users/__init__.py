"""API внешних систем и форм"""

from flask import Blueprint, jsonify
from werkzeug.exceptions import HTTPException

users = Blueprint('users', __name__)


# def init():
#     from app.apps.users import urls
#
#
# init()


@users.errorhandler(HTTPException)
def error_handler(e):
    """Обработка основных ошибок"""
    return jsonify(status='Error', status_code=e.code, message=e.name), e.code