import psycopg2

connection = psycopg2.connect(host="localhost", port="5432", dbname="postgres",
                              user="postgres", password="password")

cursor = connection.cursor()

cursor.execute("SELECT * FROM cats WHERE id=%s", (4,))

for row in cursor:
    print(row)

connection.close()
