import logging
import os
from distutils.util import strtobool


basedir = os.path.abspath(os.path.dirname(__file__))
templates = os.path.join(basedir, 'templates')
logs = os.path.join(basedir, 'logs')
build = os.path.join(basedir, 'build')
translation = os.path.join(basedir, 'translation')
media = os.path.join(basedir, 'media')
orig = os.path.join(basedir, 'orig')


class DefaultConfig(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', '124;e6ef6a1231239258$c8$c4a1!56#8')

    IS_TESTING = os.environ.get('IS_TESTING', False)

    DB_NAME = os.environ.get('DB_NAME', 'grd')
    DB_USER = os.environ.get('DB_USER', 'grd')
    DB_PASS = os.environ.get('DB_PASS', '')
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_PORT = os.environ.get('DB_PORT', 3366)

    LOG_FORMAT = logging.Formatter(
        '[%(asctime)s] %(levelname)s %(message)s [%(filename)s:%(lineno)d %(funcName)s]', '%d/%m %H:%M:%S'
    )

    DEFAULT_LANGUAGE = 'ru'

    FULL_PATH_TO_MEDIA = media
    FULL_PATH_TO_ORIG = orig

    FULL_PATH_TO_GREENHOUSE_MEDIA_PHOTO = os.path.join(media, 'greenhouses')
    FULL_PATH_TO_GREENHOUSE_ORIG_PHOTO = os.path.join(orig, 'greenhouses')

    FULL_PATH_TO_GREENHOUSE_SLIDER_MEDIA_PHOTO = os.path.join(media, 'greenhouse_slider')
    FULL_PATH_TO_GREENHOUSE_SLIDER_ORIG_PHOTO = os.path.join(orig, 'greenhouse_slider')

    FULL_PATH_TO_ADDITIONAL_MEDIA_PHOTO = os.path.join(media, 'additional')
    FULL_PATH_TO_ADDITIONAL_ORIG_PHOTO = os.path.join(orig, 'additional')

    FULL_PATH_TO_SHAPE_TYPE_MEDIA_PHOTO = os.path.join(media, 'shape_types')
    FULL_PATH_TO_SHAPE_TYPE_ORIG_PHOTO = os.path.join(orig, 'shape_types')

    PATH_TO_GREENHOUSE_PHOTO = os.path.join('media', 'greenhouses').replace('\\', '/')
    PATH_TO_ADDITIONS_PHOTO = os.path.join('media', 'additions').replace('\\', '/')
    PATH_TO_SHAPE_TYPE_PHOTO = os.path.join('media', 'shape_types').replace('\\', '/')
    PATH_TO_GREENHOUSE_SLIDER = os.path.join('media', 'greenhouse_slider').replace('\\', '/')
    PATH_TO_VARIANT_EXECUTION = os.path.join('media', 'variant_execution').replace('\\', '/')
    PATH_TO_GREENHOUSE_FEATURES = os.path.join('media', 'features').replace('\\', '/')
    PATH_TO_HINT = os.path.join('media', 'hints').replace('\\', '/')
    PATH_TO_ATTRIBUTE_CATEGORY_HINT = os.path.join(PATH_TO_HINT, 'attribute_categories').replace('\\', '/')
    PATH_TO_GREENHOUSE_HINT = os.path.join(PATH_TO_HINT, 'greenhouses').replace('\\', '/')
    PATH_TO_COUNTRY_FLAG = os.path.join('media', 'countries').replace('\\', '/')

    NAME_CONFIGURATION_DIR = 'configuration'

    # Email
    MAIL_SENDER = os.environ.get('EMAIL_SENDER', 'noreply@zavodteplic.ru')
    MAIL_RECIPIENT_PREORDER = os.environ.get('EMAIL_RECIPIENT_PREORDER', 'web@zavodteplic.ru')
    MAIL_RECIPIENT_ORDER = os.environ.get('EMAIL_RECIPIENT_ORDER', 'web@zavodteplic.ru')
    MAIL_RECIPIENT_SING_UP_ON_PRESENTATION = os.environ.get(
        'EMAIL_RECIPIENT_SING_UP_ON_PRESENTATION', 'web@zavodteplic.ru'
    )
    MAIL_SERVER = os.environ.get('EMAIL_SERVER', 'smtp.yandex.ru')
    MAIL_USERNAME = os.environ.get('EMAIL_USERNAME', 'noreply@zavodteplic.ru')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD', 'tbRGQpN7M5')
    MAIL_PORT = os.environ.get('EMAIL_PORT', 465)
    MAIL_USE_SSL = os.environ.get('EMAIL_USE_SSL', True)

    VALID_EXTENSION_FOR_MEDIA_COMPRESS = [
        '.png',
        '.jpg',
        '.jpeg'
    ]

