from flask_restplus import Resource
from libs.restplus import api_restplus

ns = api_restplus.namespace(
    'status', description='Status method')

@ns.route('/status')
class StatusRessource(Resource):
    # @jwt_required()
    def get(self):
        return {'message': 'Status Ok'}, 200
