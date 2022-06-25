"""Поиск кратчайшего пути (последовательности вершин) от 0-ой вершины графа до указанной вершины
с использованием BFS"""

import json
from collections import deque

with open('bfs_graph.json', 'r', encoding='UTF-8') as f:
    G = json.load(f)
G = { int(v) : set(G[v]) for v in G }

print("Исходный граф:", G)


def vertex_shortest_path_bfs(G, end_vertex):
    start_vertex = 0
    queue = deque([start_vertex])
    
    distances = [None] * len(G)
    distances[start_vertex] = 0
    parents = [None] * len(G)
    
    while queue:
        vertex = queue.popleft() # Вынимаем первую вершину слева
        for neighbour in G[vertex]: # Перебираем все ее смежные вершины
            if distances[neighbour] is None: # Если эту смежную вершину еще не проверяли ранее
                distances[neighbour] = distances[vertex] + 1 # + 1 для нее к расстоянию от текущей
                parents[neighbour] = vertex
                queue.append(neighbour) # Добавляем в конец очереди эту смежную вершину для дальнейшего просмотра 

    path = [end_vertex]
    parent = parents[end_vertex]
    while not parent is None:
        path.append(parent)
        parent = parents[parent]

    return path[::-1]

print(vertex_shortest_path_bfs(G, 9))
