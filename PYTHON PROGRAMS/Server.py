import json
from flask import Flask, request, Response
import logging


app = Flask(__name__)

# Загрузка json с парами login-password пользователей сервера
with open('users.json') as users_file:
    server_users = json.load(users_file)

stats = {
    'attemps' : 0,
    'success' : 0
}

@app.route('/')
def hello():
    return f'Hello, user! stats = {stats}'

@app.route('/auth', methods=['POST'])
def auth():
    stats['attemps'] += 1

    request_data = request.json
    login = request_data['login']
    password = request_data['password']
    logging.info(login, password)

    #Обратить внимние на login in users - перебор всех users для login
    if login in server_users and server_users[login] == password: 
        status_code = 200
        stats['success'] += 1
    else:
        status_code = 401

    return Response(status=status_code)

if __name__ == '__main__':
    app.run()
