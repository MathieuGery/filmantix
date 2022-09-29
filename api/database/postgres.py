import psycopg2
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

    def get_db_connection(self):
        cur = self.conn.cursor()
        cur.execute('CREATE TABLE books (id serial PRIMARY KEY,'
                                 'title varchar (150) NOT NULL,'
                                 'author varchar (50) NOT NULL,'
                                 'pages_num integer NOT NULL,'
                                 'review text,'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )
        # cur.execute('ALTER TABLE books ADD caca integer;')
        
        self.conn.commit()
        cur.close()
        return self.conn

    def create_plot(self, data):
        cur = self.conn.cursor()
        cur.execute('INSERT INTO plots (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('Anna Karenina',
             'Leo Tolstoy',
             864,
             'Another great classic!')
            )
        self.conn.commit()
        cur.close()
    
    def list(self):
        cur = self.conn.cursor()
        cur.execute("SELECT id, title, author, pages_num, review, to_char(date_added, 'YYY-MM-DD') FROM plots;")
        books = cur.fetchall()
        return books