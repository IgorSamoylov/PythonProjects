import json, requests


with open('users.json') as users_file:
        users = json.load (users_file)

print (users)
