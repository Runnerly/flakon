Flakon
======

**DISCLAIMER** This repository is part of Runnerly, an application made for
the Python Microservices Development. It was made for educational
purpose and not suitable for production. It's still being updated.
If you find any issue or want to talk with the author, feel free to
open an issue in the issue tracker.

Flask helper for building JSON web services.

Installation::

    $ pip install flakon


Features so far:

- a JsonBlueprint: like a Blueprint but everything is jsonified
- a SwaggerBlueprint: like JsonBlueprint but you can pass a swagger spec
  and user @operation('operationId') instead of @route
- uses Konfig to load an INI file for updating app.config


Example of usage::

    from flakon import SwaggerBlueprint, JsonBluePrint, create_app


    api = SwaggerBlueprint('Swagger API', 'swagger' ,
                           swagger_spec='openapi.yaml')

    @api.operation('getUserIds')
    def get_user_ids():
        return {'one': 2}

    other_api = JsonBlueprint('api', __name__)

    @other_api.route('/')
    def some():
        return {'here': 1}


    app = create_app(blueprints=[api, other_api])
