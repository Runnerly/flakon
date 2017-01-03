import os
from flask import Flask, jsonify, abort
from werkzeug.exceptions import HTTPException
from konfig import Config



def _error_handling(error):
    if isinstance(error, HTTPException):
        result = {'code': error.code, 'description': error.description,
                  'message': str(error)}
    else:
        description = abort.mapping[500].description
        result = {'code': 500, 'description': description,
                  'message': str(error)}

    resp = jsonify(result)
    resp.status_code = result['code']
    return resp


class JsonFlask(Flask):
    def make_response(self, rv):
        if isinstance(rv, dict):
            rv = jsonify(rv)
        return super(JsonFlask, self).make_response(rv)


def create_app(name=__name__, blueprints=None, settings=None):
    app = JsonFlask(name)

    # load configuration
    settings = os.environ.get('FLASK_SETTINGS', settings)
    app.config_file = Config(settings)
    app.config.update(app.config_file.get_map('flask'))

    # set error handling in JSON
    for code in abort.mapping:
        app.register_error_handler(code, _error_handling)

    # register blueprints
    if blueprints is not None:
        for bp in blueprints:
            app.register_blueprint(bp)

    return app
