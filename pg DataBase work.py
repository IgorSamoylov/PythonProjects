import psycopg2
from psycopg2 import OperationalError

try:
    connection = psycopg2.connect(database="postgres", user="postgres",
                                 password="password", host="localhost",
                                 port="5432")
except OperationalError as e:
    print(e)

cursor = connection.cursor()
#connection.autocommit = True

ids = [1, 2, 3, 4]

query = "SELECT * FROM cats WHERE id= %(id)s"

for _id in ids:
    cursor.execute(query, {'id' : _id})
    for rec in cursor:
        print(rec)

query = "SELECT * FROM intel WHERE id=%s"
# Подстановочный аргумент должен быть Iterable, если это кортеж с 1 элементом,
# то согласно синтаксису Питона должна быть запятая для правильной интерпретации как кортежа
cursor.execute(query, (1,)) 
print(*cursor) # Получить значение из объекта cursor можно только ПОСЛЕ выполнения execute

cursor.close()
connection.close()
