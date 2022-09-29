from flask_restplus import Resource
from libs.restplus import api_restplus

ns = api_restplus.namespace(
    'plot', description='Plot method')

@ns.route('/')
class PlotRessource(Resource):
    # @jwt_required()
    def get(self):
        return {'message': 'Plot Ok'}, 200
