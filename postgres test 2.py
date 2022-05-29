import psycopg2

con = psycopg2.connect(host="localhost", port="5432", user="postgres",
                 password="password", dbname="postgres")
con.autocommit = False

cursor = con.cursor()

query = """INSERT INTO cats VALUES(7, 'Кот Барсик', 1)"""

cursor.execute(query)

con.commit()



def readDB():
    cursor = con.cursor()
    cursor.execute("SELECT * FROM cats")
    for row in cursor:
        print(row)
        
    
readDB()


con.close()
