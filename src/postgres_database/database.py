import psycopg2
from config import config

class Database:
    def __init__(self):
        params = config()
        self.connection = psycopg2.connect(**params)
        self.cursor = self.connection.cursor()

    def select(self, table="test", columns="*", conditions=""):
        try:
            values = ', '.join(columns) if isinstance(columns, list) else columns if ', ' in columns else columns.replace(' ', ', ')
            command: str = f'SELECT {values} FROM {table} WHERE {conditions};' if conditions != '' else f'SELECT {values} FROM {table};'
            self.cursor.execute(command)
        except psycopg2.errors.UndefinedColumn as err:
            raise(err)
        except psycopg2.errors.UndefinedFunction as err:
            raise(err) 
        return self.cursor.fetchall()
    
    # def delete(self, checked_value, checked_column="id", table="test"):
    #     self.cursor.execute(f'SELECT price FROM test')
    #     try:
    #         self.cursor.execute(f'DELETE FROM {table} WHERE {checked_column} = {checked_value}')
    #     except:
    #         print("error")