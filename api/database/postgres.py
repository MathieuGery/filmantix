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

    def create_plot(self):
        cur = self.conn.cursor()
        cur.execute('INSERT INTO plots (movie, day_num, nb_found, plot_obsucred, plot)'
            'VALUES (%s, %s, %s, %s, %s)',
            ('Movie Name',
             2,
             864,
             '{"Plot obsucred": "plot"}',
             'plot not obsucred')
            )
        self.conn.commit()
        cur.close()
    
    def get_all_plots(self):
        cur = self.conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT id, movie, day_num, nb_found, plot_obsucred, plot, to_char(date_added, 'YYY-MM-DD') FROM plots;")
        books = cur.fetchall()
        return books