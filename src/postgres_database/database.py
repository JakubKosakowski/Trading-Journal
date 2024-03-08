import psycopg2
from config import config

class Database:
    def __init__(self):
        params = config()
        print(params)
        self.connection = psycopg2.connect(**params)
        self.cursor = self.connection.cursor()