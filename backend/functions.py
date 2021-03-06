import uuid
from datetime import datetime, timedelta

import jsonschema
from flask import request, abort, current_app, session, json
from flask_login import current_user
from peewee import fn


def csrf_protect(val):
    """Проверка CSRF токена"""
    csrf = session.get('csrf_token', None)
    csrf_expiration = session.get('csrf_expiration', None)
    if not csrf or csrf != val or not (csrf_expiration and csrf_expiration > datetime.utcnow().timestamp()):
        return False
    return True


def csrf_token():
    """Генерация CSRF токена"""
    csrf_expiration = session.get('csrf_expiration', None)
    if not (csrf_expiration and csrf_expiration > datetime.utcnow().timestamp()) or 'csrf_token' not in session:
        session['csrf_token'] = str(uuid.uuid4().hex)
        session['csrf_expiration'] = (datetime.utcnow() + timedelta(minutes=15)).timestamp()
    return session['csrf_token']


def validate_json(schema, data=dict(), is_abort=True):
    """Проверка данных с помощью json схемы"""
    # noinspection PyBroadException
    try:
        jsonschema.validate(data, schema)
        return data
    except Exception as e:
        current_app.logger.error('Исключение во время проверки JSON схемы ' + format(e))
        if is_abort:
            abort(400)
        return None


def utc(dt=None, delta='+3:00'):
    """Вычисление текущей даты с часовым поясом"""
    dt = dt if dt else datetime.utcnow()
    sign = delta[0]
    hours, minutes = delta[1:].split(':')
    return dt + timedelta(hours=int(f'{sign}{hours}'), minutes=int(f'{sign}{minutes}'))


def get_ip():
    """Getting really user ip"""
    try:
        return request.access_route[-1]
    except Exception as e:
        return request.remote_addr


def is_json(d):
    try:
        if type(d) == dict:
            return {'errors': False, 'value': d}
        return {'errors': False, 'value': json.loads(d)}
    except Exception as e:
        return {'errors': True, 'value': d}


def recursive_parse(dict_for_parse):
    json_d = is_json(dict_for_parse)
    dict_for_parse = json_d['value']
    if type(dict_for_parse) == dict:
        for key, value in dict_for_parse.items():
            dict_for_parse[key] = recursive_parse(value)
    elif type(dict_for_parse) == list:
        for value in dict_for_parse:
            value = recursive_parse(value)
    return dict_for_parse


def get_current_user(*args, **kwargs):
    """Model select for get current user"""
    from backend.base import CONFIG
    from backend.database.models import User
    user = User.select(
        User.id,
        User.username,
        fn.CONCAT(
            CONFIG.PATH_TO_USER_AVATAR, '/',
            User.id, '/', User.avatar
        ).alias('avatar'),
        User.fio,
        User.is_teacher,
        User.last,
        User.online,
        User.email,
    ).where(
        User.id == current_user.id
    ).dicts().first()

    return user
