import psycopg2
from flask import Flask, request

def get_from_db(query):
    conn = psycopg2.connect(host='localhost', port='5432', user='postgres',
                               password='password', dbname='demo')
    cur = conn.cursor()

    result_str = ''
    try:
        cur.execute(query)
        for row in cur:
            result_str += str(row) + '\n'
        
    except Exception as e:
        return e
    
    return 'No result' if result_str == '' else result_str 


server = Flask("postgres_server")

@server.route("/", methods=['POST'])
def send_contacts_list():
    request_body = request.data
    return get_from_db(request_body)


server.run()
