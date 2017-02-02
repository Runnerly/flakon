import os
from flask import Flask
from konfig import Config

from flakon.blueprints import SwaggerBlueprint, JsonBlueprint   # NOQA


def create_app(name=__name__, blueprints=None, settings=None, openapi=None):
    app = Flask(name)

    # load configuration
    settings = os.environ.get('FLASK_SETTINGS', settings)
    if settings is not None:
        app.config_file = Config(settings)
        app.config.update(app.config_file.get_map('flask'))

    # register blueprints
    if blueprints is not None:
        for bp in blueprints:
            app.register_blueprint(bp)

    # register openapi
    if openapi is not None:
        app.register_blueprint(SwaggerBlueprint(openapi))

    return app
