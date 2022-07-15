import requests
import time
import json
from tqdm import tqdm
from collections import deque

HOST = 'https://api.vk.com/method/'
VERSION = '5.81'
with open("RESOURCES/vk_access_token1.json", "r", encoding="UTF-8") as f:
    vk_access_token = json.load(f)['token']


def get_friends_list(id_user: str):
    r = requests.get(HOST + 'friends.get', params = { 'user_id' : id_user,
                                               'access_token' : vk_access_token,
                                               'v' : VERSION})
                                                #"fields" : "country"})
    print(r.json())
    if 'response' in r.json():
        result = r.json()['response']['items']
        
        return result
    
    return []


def search_friends_graph_bfs(id_start: str, id_end: str):
    queue = deque(get_friends_list(id_start))

    distances = { friend: 1 for friend in queue }
    parents = { friend: id_start for friend in queue }

    parents[id_start] = None 

    while id_end not in distances:
        cur_user = queue.popleft()
        new_friends = get_friends_list(cur_user)
        time.sleep(0.2)
        for user in tqdm(new_friends):
            if user not in distances:
                queue.append(user)
                distances[user] = distances[cur_user] + 1
                parents[user] = cur_user

    path = [id_start]
    parent = parents[id_start]
    while parent is not None:
        path.append[parent]
        parent = parents[parent]
    return path

def main():
    #print(get_friends_list("24119615"))
        
    id_start = '24119615'
    id_end = '1'
    print(search_friends_graph_bfs(id_start, id_end))

if __name__ == '__main__':
    main()
