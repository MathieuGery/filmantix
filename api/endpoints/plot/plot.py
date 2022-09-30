from flask_restplus import Resource
from libs.restplus import api_restplus
from database.postgres import DatabasePostgres

ns = api_restplus.namespace(
    'plot', description='Plot method')

@ns.route('/')
class PlotRessource(Resource):
    # Get Today Plot
    def get(self):
        db = DatabasePostgres()
        plot = db.get_all_plots()
        del db
        return {'plot': plot}, 200
