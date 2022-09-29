from flask_restplus import Resource
from libs.restplus import api_restplus
from database.postgres import DatabasePostgres

ns = api_restplus.namespace(
    'plot', description='Plot method')

@ns.route('/')
class PlotRessource(Resource):
    def get(self):
        db = DatabasePostgres()
        db.create_plot()
        res = db.get_all_plots()
        del db
        return {'message': res}, 200
