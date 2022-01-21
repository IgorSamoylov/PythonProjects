import psycopg2
from psycopg2 import OperationalError

try:
    connection = psycopg2.connect(database="postgres", user="postgres",
                              password="password", host="localhost",
                              port="5432")
except OperationalError as e:
    print(e)


connection.autocommit = True

cursor = connection.cursor()

#query = "CREATE DATABASE python_database"
#cursor.execute(query)

# SERIAL primary key в PostgreSQL обеспечивает последовательное создание новых id
# для всех новых записей
query = """
CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  age INTEGER,
  gender TEXT,
  nationality TEXT
)
"""
cursor.execute(query)

#Такой запрос изменяет таблицу, добавляя новую колонку
query = "ALTER TABLE users ADD email VARCHAR(255)"
cursor.execute(query)

#   Так в PostgreSQL меняется тип данных в колонке
# Для преобразования TEXT в INTEGER нужно дополнительно указать в конце запроса USING email::integer
query = """ ALTER TABLE users
                    ALTER COLUMN email TYPE TEXT """
cursor.execute(query)


# Удалить колонку
query = """ALTER TABLE users
                  DROP COLUMN email"""
cursor.execute(query)

