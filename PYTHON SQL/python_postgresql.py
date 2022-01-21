import psycopg2
from psycopg2 import OperationalError


class PythonPostgresql:
    def __init__(self, database="postgres", user="postgres",
                 password="password", host="localhost",
                 port="5432"):

        self.database = database
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        
        self.connection = None

    def connect_sql(self):
        try:
            self.connection = psycopg2.connect(database=self.database, user=self.user,
                                               password=self.password, host=self.host,
                                               port=self.port)
            print("Connection to PostgreSQL DB successful")
        except OperationalError as e:
            print(f"The error '{e}' occurred")
        self.connection.autocommit = True

    def get_connection(self):
        return self.connection

    def execute_query(self, sql_query: str):
        cursor = self.connection.cursor()
        try:
            cursor.execute(sql_query)
            print("Query executed successfully")
        except OperationalError as e:
            print(f"The error '{e}' occurred")
