import psycopg2
from flask import Flask, request, render_template

conn = psycopg2.connect(host='localhost', port='5432', user='postgres',
                               password='password', dbname='demo')
conn.autocommit = True

def get_from_db(query):
    
    cur = conn.cursor()

    result_list = []
    try:
        cur.execute(query)
        for row in cur:
            result_list.append(str(row))
        
    except Exception as e:
        return {'error': str(e)}
    
    return {'data': 'No result'} if result_list == [] else {'data': result_list}


server = Flask("postgres_server", template_folder='templates')

@server.route("/", methods=['GET'])
def show_index_html():
    return render_template('Postgres_Flask_JS.html')

@server.route("/", methods=['POST'])
def send_contacts_list():
    request_body = request.data
    return get_from_db(request_body)


server.run()
