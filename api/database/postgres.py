import psycopg2
from psycopg2.extras import RealDictCursor
import json
from libs.config import config
class DatabasePostgres():
    def __init__(self):
        self.conn = psycopg2.connect(host=config['POSTGRES_HOST'].get(),
                                database=config['POSTGRES_DB'].get(),
                                user=config['POSTGRES_USER'].get(),
                                password=config['POSTGRES_PASSWORD'].get())

    def __del__(self):
        self.conn.close()

    def create_plot(self, data):
        cur = self.conn.cursor()
        cur.execute('INSERT INTO plots (title, day_num, nb_found, title_obsucred, title_non_obsucred, plot_obsucred, plot_non_obsucred, plot, link, poster, origin_country, director, release_date, runtime)'
            'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
            (data.get("title"),
             0,
             0,
             json.dumps(data.get("title_obsucred")),
             json.dumps(data.get("title_non_obsucred")),
             json.dumps(data.get("plot_obsucred")),
             json.dumps(data.get("plot_non_obsucred")),
             data.get("plot"),
             data.get("link"),
             data.get("poster"),
             data.get("origin_country"),
             data.get("director"),
             data.get("release_date"),
             data.get("runtime"))
            )
        self.conn.commit()
        cur.close()
    
    def get_all_plots(self):
        cur = self.conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT id, title, day_num, nb_found, plot_obsucred, plot_non_obsucred, plot, link, poster, origin_country, director, release_date, runtime, to_char(date_added, 'YYY-MM-DD') FROM plots;")
        plots = cur.fetchall()
        return plots

    def get_last_plot(self):
        cur = self.conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT id, title, day_num, nb_found, title_obsucred, title_non_obsucred, plot_obsucred, plot_non_obsucred, plot, link, poster, origin_country, director, release_date, runtime, to_char(date_added, 'YYY-MM-DD') FROM plots;")
        plots = cur.fetchall()
        id = 0
        res = None
        for plot in plots:
            if (plot.get("id") > id):
                id = plot.get("id")
                res = plot
        return res

    def get_today_plot(self):
        cur = self.conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT id, day_num, nb_found, title_obsucred, plot_obsucred, to_char(date_added, 'YYY-MM-DD') FROM plots;")
        plots = cur.fetchall()
        id = 0
        for plot in plots:
            if (plot.get("id") > id):
                id = plot.get("id")
                res = plot
        return res
