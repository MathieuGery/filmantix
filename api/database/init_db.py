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
                                'movie varchar (150) NOT NULL,'
                                'day_num integer NOT NULL,'
                                'nb_found integer NOT NULL,'
                                'plot_obsucred jsonb,'
                                'plot text,'
                                'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                )
conn.commit()
cur.close()
conn.close()