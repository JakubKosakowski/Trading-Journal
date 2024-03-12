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
        except psycopg2.errors.SyntaxError as err:
            raise(err)
        return self.cursor.fetchone()[0]
    
    def update(self, table, columns, new_values, ident_column, ident_value):
        try:
            command_set_new_values = ''
            if isinstance(columns, list) and isinstance(new_values, list):
                for i in range(len(columns)):
                    command_set_new_values += f" {columns[i]} = '{new_values[i]}'" if isinstance(new_values[i], str) else f' {columns[i]} = {new_values[i]}'
                    command_set_new_values += ',' if i < len(columns)-1 else ''
                command_returning = f'RETURNING {columns[0]};'.replace("'", "")
            else:
                raise(Exception("Column and new value have to be the same type!"))
            self.cursor.execute(f'UPDATE {table} SET{command_set_new_values} WHERE {ident_column} = {ident_value} {command_returning}')   
        except IndexError as err:
            raise(err)
        except TypeError as err:
            raise(err)
        except psycopg2.errors.SyntaxError as err:
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