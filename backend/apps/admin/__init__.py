"""API внешних систем и форм"""

from flask import Blueprint, jsonify
from werkzeug.exceptions import HTTPException

admin = Blueprint('admin', __name__)


def __init():
    from backend.apps.admin import urls


__init()


@admin.errorhandler(HTTPException)
def error_handler(e):
    """Обработка основных ошибок"""
    return jsonify(status='Error', status_code=e.code, message=e.name), e.code
