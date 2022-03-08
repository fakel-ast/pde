import os
import sys
import uuid
from datetime import datetime, timedelta
from functools import wraps

import jwt
from flask import json, request, abort, render_template, current_app, session
from flask.views import MethodView
from threading import Thread

from flask_login import login_user
from flask_mail import Message
from peewee import fn
from playhouse.shortcuts import model_to_dict

from backend import mail
from backend.database.models import User, Session
from backend.functions import csrf_protect, validate_json, get_ip, get_current_user
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
            if not app.debug or 'csrf-token' in self.data:
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
            session_token = session.get('session_token') or ''
            if session_token:
                try:
                    user = User.select(
                        User
                    ).join(Session).where(
                        Session.session == session_token
                    ).objects().first()

                    if user:
                        login_user(user)
                        return func(*args, **kwargs)
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    current_app.logger.error(f'Ошибка session token: {e} in {format(exc_tb.tb_lineno)}')
            return {'errors': True, 'message': 'Not valid session token'}, 403
        else:
            user = User.select(
                User
            ).where(
                User.username == 'fakel_ast'
            ).first()

            if user:
                login_user(user)
            return func(*args, **kwargs)

    return decorator


def auth_user(user: User, *args, **kwargs):
    try:
        login_user(user, remember=True)

        # save refresh token in session
        session_token = uuid.uuid4()
        session['session_token'] = session_token
        # Save token in bd. Or replace if this user_id exists
        Session \
            .insert(session=session_token, user_id=user.id) \
            .on_conflict('replace') \
            .execute()
        return {'errors': False, 'user': get_current_user()}

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        current_app.logger.error(f'{e} in {format(exc_tb.tb_lineno)}')
        return {'errors': True, 'message': f'Code error'}, 500
