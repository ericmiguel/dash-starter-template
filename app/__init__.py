from flask import Flask
from importlib import import_module
from . import dashboards

def register_blueprints(app):
    for module_name in ['base']:
        module = import_module('app.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)

def create_app(config=None):
    app = Flask(__name__, static_folder='./static')
    if config:
        app.config.from_object(config)
    register_blueprints(app)
    app = dashboards.Dash_App1.Add_Dash(app)
    return app
