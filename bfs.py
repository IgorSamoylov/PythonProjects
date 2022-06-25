"""Поиск расстояния от 0-ой вершины графа до каждой из вершин
с использованием BFS"""

import json
from collections import deque

with open('bfs_graph.json', 'r', encoding='UTF-8') as f:
    G = json.load(f)

G = { int(v) : set(G[v]) for v in G }

print("Исходный граф:", G)

def vertex_distances_bfs(G):
    distances = [None] * len(G)
    start_vertex = 0
    distances[start_vertex] = 0
    queue = deque([start_vertex])

    while queue:
        v = queue.popleft() # Вынимаем первую вершину слева
        for neighbour in G[v]: # Перебираем все ее смежные вершины
            if distances[neighbour] is None: # Если эту смежную вершину еще не проверяли ранее
                distances[neighbour] = distances[v] + 1 # + 1 для нее к расстоянию от текущей
                queue.append(neighbour) # Добавляем в конец очереди эту смежную вершину для дальнейшего просмотра 

    return distances

print(vertex_distances_bfs(G))
