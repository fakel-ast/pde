import logging
import os
from distutils.util import strtobool


basedir = os.path.abspath(os.path.dirname(__file__))
templates = os.path.join(basedir, 'templates')
logs = os.path.join(basedir, 'logs')
build = os.path.join(basedir, 'build')
media = os.path.join(basedir, 'media')


class DefaultConfig(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', '124;e6ef6a1231239258$c8$c4a1!56#8')

    IS_TESTING = os.environ.get('IS_TESTING', False)

    DB_NAME = os.environ.get('DB_NAME', 'code_skill')
    DB_USER = os.environ.get('DB_USER', 'code_skill')
    DB_PASS = os.environ.get('DB_PASS', '')
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_PORT = os.environ.get('DB_PORT', 3306)

    LOG_FORMAT = logging.Formatter(
        '[%(asctime)s] %(levelname)s %(message)s [%(filename)s:%(lineno)d %(funcName)s]', '%d/%m %H:%M:%S'
    )

    PATH_TO_TASK_CATEGORIES_IMAGES = os.path.join('media', 'task_categories').replace('\\', '/')
