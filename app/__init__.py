#encoding=utf-8
from flask import Flask
import logging
from logging.handlers import SMTPHandler

DEFAULT_APP_NAME = 'app'

def create_app(config=None):
    app = Flask(DEFAULT_APP_NAME)
    app.config.from_pyfile(config)
    config_logging(app)
    return app

def config_logging(app):
    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]')
    ADMINS = ['jinming@1872.net']
    MAIL_HANDLER_CREDENTIALS = ('jinming@1872.net','jinming')
    error_mail_handler = SMTPHandler('smtp.exmail.qq.com','jinming@1872.net',ADMINS,'部署应用出现错误了~~',MAIL_HANDLER_CREDENTIALS)
    error_mail_handler.setLevel(logging.ERROR)
    error_mail_handler.setFormatter(formatter)
    app.logger.addHandler(error_mail_handler)

