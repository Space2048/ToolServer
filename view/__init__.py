'''
view
@author:blb
@time 23-3-22
'''
from flask import Flask
from view.toolcenter import toolcenter

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        return '<!DOCTYPE html><html><head><style>body {    background-color: #ff0000 }</style></head><body><h1 align="center">Please leave quickly</h1></body></html>'

    app.register_blueprint(blueprint=toolcenter, url_prefix = "/tools")

    return app