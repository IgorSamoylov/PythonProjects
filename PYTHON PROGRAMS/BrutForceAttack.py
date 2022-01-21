import requests
import json

alphabet = '0123456789abcdefghjklmnoprstquvwxyz'
base = len (alphabet)

length = 0
counter = 0

while True:
    password = ''
    number = counter # Текущая длина генерируемого пароля
    while number > 0:
        
        rest = number % base
        print(counter, ' ', rest, " ", number)
        i = input()
        password = alphabet[rest] + password
        number = number // base #Целочисленное деление 
    
    # Дополняем длину пароля нулями в начале
    while len (password) < length: 
        password = alphabet [0] + password

    response = requests.post ('http://127.0.0.1:5000/auth',
                                                   json = {'login' : 'admin', 'password' : password})
    print('Password: ', password)
    
    if response.status_code == 200:
        print('SUCCESS', result)
        break

    # встретили последний пароль для данной длины
    if alphabet [-1] * length == password: # Т.е. 'z' * длину = zzzz. Обр внимание на запись индекса!   
        length += 1
        counter = 0
    else:
        counter += 1

    if length == 4:
        break
