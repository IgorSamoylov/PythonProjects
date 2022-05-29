import psycopg2

con = psycopg2.connect(host="localhost", port="5432", user="postgres",
                 password="password", dbname="demo")
cursor = con.cursor()


query = """SELECT table_name FROM information_schema.tables
WHERE table_schema NOT IN ('information_schema','pg_catalog'); """

#query = "SELECT datname,usename,client_addr,client_port FROM pg_stat_activity;"

query = """SELECT flight_no, actual_departure, airport_name FROM flights
JOIN airports_data ON flights.departure_airport = airports_data.airport_code
WHERE actual_departure > '2017-07-24 %s:00' AND actual_departure < '2017-07-24 %s:00'

"""
time = 16

result = {}
while time < 17:
    cursor.execute(query, (time, time + 1))
    result[time] = []
    for row in cursor:
        result[time].append(row) # jsonb из Postgres автоматически конвертируется в Python dict
    time += 1
    
for hour in result:
    print(f"Час: {hour}")
    for n, flight in enumerate(result[hour]):
          print(f"Полет {n}: {flight[0]} {flight[1]} {flight[2]['ru']}")
    
con.close()


