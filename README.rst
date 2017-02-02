Flakon
======


Flask helper for building JSON web services.

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
