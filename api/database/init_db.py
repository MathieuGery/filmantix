import psycopg2
from confuse import Configuration

config = Configuration('HUB-API', __name__)
config.set_file('config/config.yaml')

conn = psycopg2.connect(host=config['POSTGRES_HOST'].get(),
                                database=config['POSTGRES_DB'].get(),
                                user=config['POSTGRES_USER'].get(),
                                password=config['POSTGRES_PASSWORD'].get())

cur = conn.cursor()
cur.execute('CREATE TABLE plots (id serial PRIMARY KEY,'
                                'title varchar (150) NOT NULL,'
                                'day_num integer,'
                                'nb_found integer,'
                                'plot_obsucred jsonb NOT NULL,'
                                'plot_non_obsucred jsonb NOT NULL,'
                                'plot text NOT NULL,'
                                'link text NOT NULL,'
                                'poster text NOT NULL,'
                                'origin_country text NOT NULL,'
                                'director text NOT NULL,'
                                'release_date text NOT NULL,'
                                'runtime integer NOT NULL,'
                                'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                )
conn.commit()
cur.close()
conn.close()