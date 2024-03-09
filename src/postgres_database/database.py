import psycopg2
from config import config

class Database:
    def __init__(self):
        params = config()
        print(params)
        self.connection = psycopg2.connect(**params)
        self.cursor = self.connection.cursor()

    def select(self, table="test", columns="*"):
        values = ','.join(columns) if isinstance(columns, list) else columns
        self.cursor.execute(f'SELECT {values} FROM {table}')
        return self.cursor.fetchall()