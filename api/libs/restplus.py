import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restplus import Api

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': "Type in the *'Value'* input box below: **'Bearer &lt;JWT&gt;'**, where JWT is the token"
    }
}

api_restplus = Api(version='1.0', title='Filmantix API',
          description='Awesome backend',
          ordered=False)

# @api_restplus.errorhandler
# def default_error_handler(e):
#     message = f"An unhandled exception occurred. {e}"
#     logger.info(message)
