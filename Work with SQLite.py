import sqlite3

conn = sqlite3.Connection("SQL/Programs/hotel.db")

cursor = conn.cursor()

for item in cursor.execute("SELECT * FROM guests3"):
    print(item)

conn.close()

