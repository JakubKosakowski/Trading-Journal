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
            command = f'SELECT {values} FROM {table};' if conditions == '' else f'SELECT {values} FROM {table} WHERE {conditions};'
            print(command)
            self.cursor.execute(command)
        except psycopg2.errors.UndefinedColumn as err:
            raise(err)
        except psycopg2.errors.InFailedSqlTransaction as err:
            raise(err) 
        return self.cursor.fetchall()
    
    def insert(self, table, values):
        try:
            command_table_part = f"INSERT INTO {table}{tuple(self.get_table_columns_names(table))}".replace("'", "")
            command_value_part = f"VALUES{tuple(values)} RETURNING test_ident;"
            self.cursor.execute(f'{command_table_part} {command_value_part}');
        except psycopg2.errors.DatabaseError as err:
            raise(err)
        return self.cursor.fetchone()[0]
    

    def get_table_columns_names(self, table):
        self.cursor.execute(f'SELECT * FROM {table}')
        return [desc[0] for desc in self.cursor.description][1:]
    
    # def delete(self, checked_value, checked_column="id", table="test"):
    #     self.cursor.execute(f'SELECT price FROM test')
    #     try:
    #         self.cursor.execute(f'DELETE FROM {table} WHERE {checked_column} = {checked_value}')
    #     except:
    #         print("error")