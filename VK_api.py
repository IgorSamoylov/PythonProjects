import requests
import time
import json
from tqdm import tqdm

HOST = "https://api.vk.com/method/"
VERSION = "5.81"

with open("RESOURCES/vk_access_token1.json", "r", encoding="UTF-8") as f:
    vk_access_token = json.load(f)["token"]
    
r = requests.get(HOST + "users.get", params = { "user_ids" : "377076210, 24119615",
                                               "access_token" : vk_access_token,
                                               "v" : VERSION }) 

print(r.text)
print(r.json())
#print(r.json()['response'][0])
