# -*- coding: utf-8 -*-
__version__ = '0.1'

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

from project.config import config

toolbar = DebugToolbarExtension()


def create_app(config_name=None):
    import os
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'default')

    app = Flask('project')
    app.config.from_object(config[config_name])

    toolbar.init_app(app)

    from project.controllers.printer import printer_bp
    app.register_blueprint(printer_bp)

    return app
