import psycopg2
from psycopg2 import OperationalError

connection = psycopg2.connect(host="localhost", port=5432, user="postgres", password="password", dbname="demo")
cursor = connection.cursor()

def execute_query(query: str, *args):
    try:
        cursor.execute(query, args) 
        for line in cursor:
            #print(line[0], f" flight(s) for passengers who named {name} from airport ", line[1]['ru'])
            print(line)
    except OperationalError as e:
        print(e)
        connection.close()
                

query = """
SELECT COUNT(*), bookings.airports_data.airport_name FROM bookings.flights
JOIN bookings.airports_data ON bookings.airports_data.airport_code = bookings.flights.departure_airport

WHERE bookings.flights.flight_id IN ( 
SELECT bookings.boarding_passes.flight_id FROM bookings.boarding_passes WHERE bookings.boarding_passes.ticket_no IN ( 
SELECT bookings.tickets.ticket_no FROM bookings.tickets WHERE bookings.tickets.passenger_name SIMILAR TO %s))

GROUP BY bookings.airports_data.airport_name
HAVING COUNT(*) > 5
ORDER BY COUNT(*) DESC
"""
name = "IGOR%"
execute_query(query, name) 

n = 987
while n < 1000:
    query = f"""SELECT * FROM bookings.tickets
                WHERE bookings.tickets.ticket_no = %s"""
    nulls = 6 - len(str(n))
    arg = '0005432' + '0' * nulls + str(n)
    print(arg)
    execute_query(query, arg)
    n += 1

connection.close()
