import psycopg2
import python_postgresql

pp = python_postgresql.PythonPostgresql()

pp.connect_sql()

query = """
INSERT INTO users(name, age, gender, nationality)
        VALUES ('BARSIK', 10, 'M', 'cat');  

"""

pp.execute_query(query)


users_list = [
    ("James", 25, "male", "USA"),
    ("Leila", 32, "female", "France"),
    ("Brigitte", 35, "female", "England"),
    ("Mike", 40, "male", "Denmark"),
    ("Elizabeth", 21, "female", "Canada"),
]

# в качестве VALUES в выражении INSERT INTO можно использовать кортежи напрямую
for user in users_list:
    query = f"INSERT INTO users (name, age, gender, nationality) VALUES {user}"
    pp.execute_query(query)

# Объект cursor из psycopg2 сам является iterable и позволяет в себе вернуть запрос результата SELECT
connection = pp.get_connection()
cursor = connection.cursor()
cursor.execute("SELECT  * FROM users ")
print(type(cursor))

# Получаем записи из cursor, каждая строка - в виде кортежа
for record in cursor:
    print(record, " ",  type(record))

# Удалить записи с id от 1 до 5
for n in range(1, 6):
    query = f"DELETE FROM users WHERE id={n}"
    pp.execute_query(query)

# Такой запрос удаляет сразу все записи, соответствующие указанному условию
query = " DELETE FROM users WHERE name='BARSIK' "
pp.execute_query(query)
    
# Такой запрос удаляет все записи
query = " DELETE FROM users *"
pp.execute_query(query)

query = " "



