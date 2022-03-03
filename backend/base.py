import os
import sys
from functools import wraps

import jwt
from flask import json, request, abort, render_template, current_app
from flask.views import MethodView
from threading import Thread

from flask_login import login_user
from flask_mail import Message

from backend import mail
from backend.functions import csrf_protect, validate_json, get_ip
from backend.cfg import DefaultConfig

CONFIG = DefaultConfig


class MyMethodView(MethodView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = self.get_data(*args, **kwargs)
        self.schema = {}
        self.ip = ''

    def get_data(self, *args, **kwargs):
        if request.method.lower() == 'post':
            data = json.loads(json.dumps(request.get_json(force=True, cache=False), ensure_ascii=False))
            if type(data) == str:
                return json.loads(data)
            return data
        elif request.method.lower() == 'get':
            return request.args

    def post(self, *args, **kwargs):
        from code_skill import app
        if not app.debug:
            if not self.data.get('csrf-token') or not csrf_protect(self.data.get('csrf-token')):
                abort(403)

        if self.schema:
            if not app.debug:
                self.schema['properties']['csrf-token'] = {"type": "string", "pattern": "^.{10,}$"}
            self.data = validate_json(self.schema, self.data)

        self.ip = get_ip()


class ModalMixin:

    def send_email_form(
            self, model_object, subject, params: dict,
            template_name: str, recipients: list = None, country: str = 'ru',
            translate_parts: str = None, *args, **kwargs
    ):
        """Отложенная отправка письма c уведомлением"""
        try:
            from code_skill import app
            translate = {}

            with app.app_context():
                msg = Message(
                    subject=f'GreenDi: {subject if not translate.get(subject) else translate.get(subject)}',
                    sender=app.config['MAIL_SENDER'],
                    recipients=recipients or [app.config['MAIL_RECIPIENT_PREORDER']],
                    html=render_template(template_name, **params),
                )
                mail.send(msg)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            current_app.logger.error(f'Ошибка отправки письма (in: {format(exc_tb.tb_lineno)}): {e}')

    def send_async_email_form(
            self, model_object, subject: str, params: dict,
            template_name: str, recipients: list = [], *args, **kwargs
    ):
        try:
            # async send email
            Thread(
                target=self.send_email_form,
                kwargs={
                    'model_object': model_object, 'subject': subject, 'params': params,
                    'template_name': template_name, 'recipients': recipients,
                },
            ).start()
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            current_app.logger.error(f'Ошибка отправки асинхронного письма: {e} in {format(exc_tb.tb_lineno)}')
        return True

    def send_async_translate_email_form(
            self, model_object, subject: str, params: dict,
            template_name: str, recipients: list = [], country: str = 'ru',
            translate_parts: list = None, *args, **kwargs
    ):
        try:
            # async send email
            Thread(
                target=self.send_email_form,
                kwargs={
                    'model_object': model_object, 'subject': subject, 'params': params,
                    'template_name': template_name, 'recipients': recipients, 'country': country,
                    'translate_parts': translate_parts
                }
            ).start()
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            current_app.logger.error(f'Ошибка отправки асинхронного письма: {e} in {format(exc_tb.tb_lineno)}')
        return True


def user_required(func):
    @wraps(func)
    def decorator(*args, **kwargs):

        from backend.database.models import User
        from code_skill import app

        if not app.debug:
            token = request.headers.get('Authorization', '').split(' ')[-1]
            if token:
                try:
                    data = jwt.decode(token, app.config.get('SECRET_KEY', ''), algorithms=["HS256"])
                    user = User.select().where(User.id == data.get('user_id', '')).first()
                    if user:
                        login_user(user)
                        return func(*args, **kwargs)
                except jwt.ExpiredSignatureError:
                    return {'errors': True, 'message': 'Token expired'}, 401
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    current_app.logger.error(f'Ошибка проверки jwt токена: {e} in {format(exc_tb.tb_lineno)}')
                    return {'errors': True, 'message': 'Not valid token'}, 401
            return {'errors': True, 'message': 'Not valid token'}, 401
        else:
            return func(*args, **kwargs)
    return decorator
