from waitress import serve
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from flask import Flask, Blueprint
from libs.restplus import api_restplus
from paste.translogger import TransLogger
from libs.config import config
from endpoints.status.status import ns as status
from endpoints.testModel.testModel import ns as testModel

app = Flask(__name__)
app.config.from_mapping(config.get())
# JWTManager(app)

def initialize_app(flask_app):
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api_restplus.init_app(blueprint)
    flask_app.register_blueprint(blueprint)
    
def main():
    initialize_app(app)
    serve(TransLogger(app), host='0.0.0.0', port=app.config['WAITRESS_PORT'], url_scheme=app.config['WAITRESS_HTTP_SCHEME'])

if __name__ == "__main__":
    main()
