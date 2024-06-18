import psycopg2
from config import config
from src.utils import Logger
import os

class Database:
    """ A class used to operate on database tables

    Attributes
    ----------
    logger: Logger
        Application logger
    connection: connection
        Handles the connection to a PostgreSQL database instance
    cursor: curson
        Read-only attribute describing the result of a query

    Methods
    -------
    create_db(params)
        Create database if application is started for the first time
    delete(table=None, condition=None)
        Delete record from table according to condition
    select(table="test", columns="*", conditions="", order_by="")
        Get selected columns from table
    insert(values, table="test")
        Insert new record into table
    update(table=None, columns=None, new_values=None, ident_column=None, ident_value=None)
        Update table record according to selected parameters
    get_table_columns_names(table)
        Get all columns names from selected table
    run_queries(params)
        Run queries storage in config/trading_journal_queries.sql file
    """

    def __init__(self):
        """Initializes the instance of Database class"""

        # Get params from database.ini file
        params = config()
        self.logger = Logger(__name__)

        # Create connection and cursor
        self.connection = psycopg2.connect(f"user={params['user']} password={params['password']}")
        self.cursor = self.connection.cursor()

        # Check if database exists
        self.cursor.execute(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{params['dbname']}'")
        exists = self.cursor.fetchone()
        self.connection.close()
        if not exists: # If database doesn't exist: create database and run queries from .sql file
            self.create_db(params)
            self.run_queries(params)

        self.connection = psycopg2.connect(**params)
        self.cursor = self.connection.cursor()

    def select(self, table="test", columns="*", conditions="", order_by=""):
        """Create SELECT query 

        Arguments
        ---------
            table (str, optional): Table from database. Defaults to "test".
            columns ([str, list], optional): one or many columns, which we want to return. Defaults to "*".
            conditions (str, optional): condition for WHERE statement. Defaults to "".
            order_by (str, optional): columns for ORDER BY statement. Defaults to "".

        Returns
        -------
            list: List of all record returned by SELECT query
        """

        try:
            values = ', '.join(columns) if isinstance(columns, list) else columns if ', ' in columns else columns.replace(' ', ', ') # Create list of selected columns
            command = f'SELECT {values} FROM {table}' # Create basic SELECT FROM query
            if conditions != '': # Check if condition is selected
                command += f' WHERE {conditions}'
            if order_by != '': # Check if order_by is selected
                command += f' ORDER BY {order_by}'
            command += ';'
            self.cursor.execute(command) # Execute query
            return self.cursor.fetchall() # Return all records
        except Exception as e:
            self.connection.rollback()
            self.logger.logger.error(f"An error occurred: {e}")
    
    def insert(self, values, table="test"):
        """Insert new record into table

        Arguments
        ---------
            values (list): List of values inserted as new record
            table (str, optional): Name of table from database. Defaults to "test".

        Returns
        -------
            int: New record id number
        """

        try:
            command_table_part = f"INSERT INTO {table}{tuple(self.get_table_columns_names(table))}".replace("'", "") # Create INSERT INTO query
            command_value_part = f"VALUES{tuple(values)} RETURNING test_ident;" # Create VALUES RETURNING query
            self.logger.logger.debug(f'{command_table_part} {command_value_part}')
            self.cursor.execute(f'{command_table_part} {command_value_part}') # Connect and run both queries
            self.connection.commit()
            return self.cursor.fetchone()[0] # Return id of new record
        except Exception as e:
            self.connection.rollback()
            self.logger.logger.error(f"An error occurred: {e}")
    
    def update(self, table=None, columns=None, new_values=None, ident_column=None, ident_value=None):
        """Update existed record from table

        Arguments
        ---------
            table (str, optional): Name of table. Defaults to None.
            columns ([str, list], optional): Column name or list of columns names. Defaults to None.
            new_values ([[str, int], list], optional): New value or list of new values for record. Defaults to None.
            ident_column ([str, int], optional): Identification column. Defaults to None.
            ident_value ([srt, int], optional): Identification value. Defaults to None.

        Raises
        ------
            Exception: One of parameters is None!
            Exception: Column and new value have to be the same type!

        Returns
        -------
            int: Id of updated record
        """

        try:
            if any(value is None for value in locals().values()): # Check if all parameters are given
                raise Exception('One of parameters is None!')    
            command_set_new_values = ''
            if isinstance(columns, list) and isinstance(new_values, list): # Check if columns and new_values are the same type
                for i in range(len(columns)): # Create list of all new SET values
                    command_set_new_values += f" {columns[i]} = '{new_values[i]}'" if isinstance(new_values[i], str) else f' {columns[i]} = {new_values[i]}'
                    command_set_new_values += ',' if i < len(columns)-1 else ''
                command_returning = f'RETURNING {columns[0]};'.replace("'", "") # Create RETURNING statement
            else:
                raise Exception("Column and new value have to be the same type!")
            self.cursor.execute(f'UPDATE {table} SET{command_set_new_values} WHERE {ident_column} = {ident_value} {command_returning}') # Execute UPDATE query
            return self.cursor.fetchone()[0] # Return id of updated record
        except Exception as e:
            self.connection.rollback()
            self.logger.logger.error(f"An error occurred: {e}")

    
    def delete(self, table=None, condition=None):
        """Delete record from table

        Arguments
        ---------
            table (str, optional): Name of table in database. Defaults to None.
            condition (str, optional): Condition for WHERE statement. Defaults to None.

        Raises
        ------
            Exception: One of parameters is None!

        Returns
        -------
            int: Id of deleted record
        """

        try:
            if any(value is None for value in locals().values()): # Check if any parameter was None
                raise Exception('One of parameters is None!') 
            self.cursor.execute(f'DELETE FROM {table} WHERE {condition} RETURNING id;') # Execute DELETE query
            return self.cursor.fetchone()[0] # Return id of deleted record
        except Exception as e:
            self.connection.rollback()
            self.logger.logger.error(f"An error occurred: {e}")
        

    def get_table_columns_names(self, table):
        """Get list of all columns names in table

        Arguments
        ---------
            table (str): Name of table in database

        Returns:
            list: List of columns names
        """
        
        self.cursor.execute(f'SELECT * FROM {table}')
        return [desc[0] for desc in self.cursor.description][1:]
    
    def create_db(self, params):
        connection = psycopg2.connect(f"user={params['user']} password={params['password']}")
        connection.autocommit = True
        with connection.cursor() as cur:
            cur.execute(f"CREATE DATABASE {params['dbname']};")
        connection.close()

    def run_queries(self, params):
        self.connection = psycopg2.connect(**params)
        self.cursor = self.connection.cursor()
        
        with open('config/trading_journal_queries.sql', 'r') as f:
            queries = f.read()

        self.cursor.execute(queries)
        self.connection.commit()

        self.connection.close()
    
    # def delete(self, checked_value, checked_column="id", table="test"):
    #     self.cursor.execute(f'SELECT price FROM test')
    #     try:
    #         self.cursor.execute(f'DELETE FROM {table} WHERE {checked_column} = {checked_value}')
    #     except:
    #         print("error")