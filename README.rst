Flakon
======


Flask helper for building JSON web services.

Features so far:

- if a view returns a dict object, it's jsonified
- All 4xx and 50x responses are jsonified as well
- uses Konfig to load an INI file for updating app.config


Usage::

    from flaskon import create_app

    app = create_app()

