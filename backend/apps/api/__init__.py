"""API внешних систем и форм"""

from flask import Blueprint, jsonify
from werkzeug.exceptions import HTTPException

api = Blueprint('api', __name__)


def __init():
    from backend.apps.api import urls


__init()


@api.errorhandler(HTTPException)
def error_handler(e):
    """Обработка основных ошибок"""
    return jsonify(status='Error', status_code=e.code, message=e.name), e.code