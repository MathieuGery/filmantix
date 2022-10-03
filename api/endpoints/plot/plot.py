from flask_restplus import Resource
from libs.restplus import api_restplus
from database.postgres import DatabasePostgres
from libs.plot import create_today_plot

ns = api_restplus.namespace(
    'plot', description='Plot method')

@ns.route('/')
class PlotRessource(Resource):
    # Get Today Plot
    def get(self):
        db = DatabasePostgres()
        plot = db.get_today_plot()
        del db
        for item in plot.get("plot_obsucred"):
            item["score"] = 0
        return {'plot': plot}, 200

@ns.route('/create')
class PlotCreateRessource(Resource):
    # Create Today Plot FOR TESTING PURPOSE ONLY
    def get(self):
        create_today_plot()
        return {'plot': "Created Plot"}, 200