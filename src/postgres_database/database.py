import psycopg2
from config import config
from src.utils import Logger
import inspect

class Database:
    def __init__(self):
        params = config()
        self.logger = Logger(__name__)
        self.connection = psycopg2.connect(**params)
        self.cursor = self.connection.cursor()

    def select(self, table="test", columns="*", conditions="", order_by=""):
        try:
            values = ', '.join(columns) if isinstance(columns, list) else columns if ', ' in columns else columns.replace(' ', ', ')
            command = f'SELECT {values} FROM {table}'
            if conditions != '':
                command += f' WHERE {conditions}'
            if order_by != '':
                command += f' ORDER BY {order_by}'
            command += ';'
            self.cursor.execute(command)
            return self.cursor.fetchall()
        except Exception as e:
            self.connection.rollback()
            self.logger.logger.error(f"An error occurred: {e}")
    
    def insert(self, values, table="test"):
        try:
            command_table_part = f"INSERT INTO {table}{tuple(self.get_table_columns_names(table))}".replace("'", "")
            command_value_part = f"VALUES{tuple(values)} RETURNING test_ident;"
            self.logger.logger.debug(f'{command_table_part} {command_value_part}')
            self.cursor.execute(f'{command_table_part} {command_value_part}');
            self.connection.commit()
            return self.cursor.fetchone()[0]
        except Exception as e:
            self.connection.rollback()
            self.logger.logger.error(f"An error occurred: {e}")
    
    def update(self, table=None, columns=None, new_values=None, ident_column=None, ident_value=None):
        try:
            if any(value is None for value in locals().values()):
                raise Exception('One of parameters is None!')    
            command_set_new_values = ''
            if isinstance(columns, list) and isinstance(new_values, list):
                for i in range(len(columns)):
                    command_set_new_values += f" {columns[i]} = '{new_values[i]}'" if isinstance(new_values[i], str) else f' {columns[i]} = {new_values[i]}'
                    command_set_new_values += ',' if i < len(columns)-1 else ''
                command_returning = f'RETURNING {columns[0]};'.replace("'", "")
            else:
                raise Exception("Column and new value have to be the same type!")
            self.cursor.execute(f'UPDATE {table} SET{command_set_new_values} WHERE {ident_column} = {ident_value} {command_returning}')   
            return self.cursor.fetchone()[0]
        except Exception as e:
            self.connection.rollback()
            self.logger.logger.error(f"An error occurred: {e}")

    
    def delete(self, table=None, condition=None):
        try:
            if any(value is None for value in locals().values()):
                raise Exception('One of parameters is None!') 
            self.cursor.execute(f'DELETE FROM {table} WHERE {condition} RETURNING id;')
            return self.cursor.fetchone()[0]
        except Exception as e:
            self.connection.rollback()
            self.logger.logger.error(f"An error occurred: {e}")
        

    def get_table_columns_names(self, table):
        self.cursor.execute(f'SELECT * FROM {table}')
        return [desc[0] for desc in self.cursor.description][1:]
    
    # def delete(self, checked_value, checked_column="id", table="test"):
    #     self.cursor.execute(f'SELECT price FROM test')
    #     try:
    #         self.cursor.execute(f'DELETE FROM {table} WHERE {checked_column} = {checked_value}')
    #     except:
    #         print("error")