import psycopg2
from flask import Flask, request, render_template

def get_from_db(query):
    conn = psycopg2.connect(host='localhost', port='5432', user='postgres',
                               password='password', dbname='demo')
    cur = conn.cursor()

    result = []
    try:
        cur.execute(query)
        for row in cur:
            result.append(str(row))
        
    except Exception as e:
        return [e]
    
    return ['No result'] if result == [] else result 


server = Flask("postgres_server", template_folder='templates')

@server.route("/", methods=['POST'])
def send_contacts_list():
    request_body = request.data
    return render_template('Postgres_Flask.html', result_list=get_from_db(request_body))


server.run()
