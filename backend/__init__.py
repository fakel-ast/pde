import logging
import os

from flask import Flask, send_from_directory, request, render_template
from flask_cors import CORS
from peewee import MySQLDatabase
from playhouse.flask_utils import FlaskDB
from flask_mail import Mail

from backend.apps.users.mixins import CustomAnonymousUserMixin
from backend.cfg import DefaultConfig, build, logs, templates, media
from backend.functions import csrf_token


class MyFlaskDB(FlaskDB):
    def connect_db(self):
        self.database.connect(reuse_if_open=True)


# обработчик БД
pw = MyFlaskDB()

# Email
mail = Mail()


def init_app(configuration=DefaultConfig):
    """Фабрика создания приложения"""
    app = Flask(__name__.split('.')[0], template_folder=templates, static_folder=build)
    # для подключения api при разработке
    app.config.from_object(configuration)
    initialize_extensions(app)
    application_routes(app)
    register_blueprints(app)
    application_settings(app)
    application_context_processor(app)
    return app


def initialize_extensions(app):
    """Инициализация расширений"""
    if not app.config.get('IS_TESTING', False):
        app.config['DATABASE'] = MySQLDatabase(
            app.config.get('DB_NAME'),
            user=app.config.get('DB_USER'),
            password=app.config.get('DB_PASS'),
            host=app.config.get('DB_HOST'),
            port=app.config.get('DB_PORT')
        )
        pw.init_app(app)
    mail.init_app(app)


def register_blueprints(app_name):
    from backend.database import models
    from backend.database.models import BaseModel

    if app_name.debug:
        pass
        pw.database.create_tables(BaseModel.__subclasses__())

    from backend.apps.api import api
    app_name.register_blueprint(api, url_prefix='/api/v1/')

    if app_name.debug:
        CORS(app_name, supports_credentials=True)


def application_settings(app):
    # логирование
    if not app.debug:
        from logging.handlers import RotatingFileHandler
        os.makedirs(os.path.join(logs), exist_ok=True)
        app.logger = logging.getLogger()
        handler = RotatingFileHandler(
            os.path.join(logs, 'errors.log'), maxBytes=5242880, backupCount=20, encoding='utf-8'
        )
        handler.setFormatter(app.config['LOG_FORMAT'])
        handler.setLevel(logging.WARNING)
        app.logger.addHandler(handler)
        app.logger.setLevel(logging.WARNING)


def application_context_processor(app):
    @app.context_processor
    def utility_processor():
        return dict(
            csrf_token=csrf_token,
        )


def application_routes(app):
    """Глобальные маршруты"""

    @app.route('/', defaults={'path': ''})
    @app.route('/<language>/', defaults={'path': ''})
    @app.route('/<language>/greenhouses/<greenhouse_slug>', defaults={'path': ''})
    def index(path, *args, **kwargs):
        return render_template('index.html')

    @app.route('/build/<path:path>')
    def static_dist(path):
        # тут пробрасываем статику
        return send_from_directory(build, path)

    @app.route('/assets/<path:path>')
    def static_assets(path):
        return send_from_directory(os.path.join(build, 'assets'), path)

    @app.route('/fonts/<path:path>')
    def static_fonts(path):
        return send_from_directory(os.path.join(build, 'fonts'), path)

    @app.route('/media/<path:path>')
    def send_media_files(path):
        return send_from_directory(media, path)

    @app.route('/robots.txt')
    @app.route('/favicon.ico')
    def file_robot():
        """Маршрут выдачи файлов для роботов и фавиконов"""
        return send_from_directory(os.path.join(build), request.path[1:], as_attachment=True)
