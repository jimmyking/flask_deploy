from flask import Flask
from app import create_app
from flask.ext.script import Manager,Shell,Command

app = create_app('config.cfg')
manager = Manager(app)

@app.route('/')
def index():
	return 'Flask deploy'

if __name__ == '__main__':
	manager.run()

