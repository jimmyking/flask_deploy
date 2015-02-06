from flask import Flask,current_app
from app import create_app
from flask.ext.script import Manager,Shell,Command

app = create_app('config.cfg')
manager = Manager(app)

@app.route('/')
def index():
    current_app.logger.info("hello index")
    current_app.logger.error("error index")
    return 'Flask deploy'

if __name__ == '__main__':
    manager.run()

