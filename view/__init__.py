'''
view
@author:blb
@time 23-3-22
'''
from flask import Flask
from view.toolcenter import toolcenter
from flask.ext.login import LoginManager
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)

    jwt = JWTManager(app)
    app.register_blueprint(blueprint=toolcenter, url_prefix = "/tools")

    return app