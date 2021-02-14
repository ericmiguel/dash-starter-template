from flask import Flask
from importlib import import_module
from .dashboards import dashapp1
from .dashboards import dashapp2

def register_blueprints(app):
    for module_name in ['base', 'api']:
        module = import_module('app.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)

def create_app(config=None):
    app = Flask(__name__, static_folder='./static')
    if config:
        app.config.from_object(config)
    register_blueprints(app)
    app = dashapp1.dashapp.instanciate(app)
    app = dashapp2.dashapp.instanciate(app)
    return app
