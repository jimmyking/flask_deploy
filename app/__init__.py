from flask import Flask

DEFAULT_APP_NAME = 'app'

def create_app(config=None):
	app = Flask(DEFAULT_APP_NAME)
	app.config.from_pyfile(config)
	#config_logging(app)
	return app

def config_logging(app):
	pass